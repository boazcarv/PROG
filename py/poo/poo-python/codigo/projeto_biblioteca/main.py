"""
Projeto integrador — Sistema de Biblioteca.

Junta os 6 tópicos da ementa:
  1. POO (abstração, classes, encapsulamento, composição, herança,
     polimorfismo, classes abstratas)
  2. Modelagem UML (ver diagrama-classes.md)
  3. Tratamento de exceções (biblioteca/excecoes.py)
  4. Modularização e pacotes (biblioteca/, modelos/, servicos/, gui/)
  5. Serialização em JSON (biblioteca/servicos/acervo.py)
  6. Interface gráfica (biblioteca/gui/janela.py)

Uso:
    python3 main.py            -> abre a interface gráfica
    python3 main.py --console  -> roda a demonstração em modo texto
"""

import sys

from biblioteca.excecoes import ErroBiblioteca
from biblioteca.modelos import Livro, DVD
from biblioteca.servicos import Acervo

ARQUIVO = "acervo.json"


def dados_de_exemplo(acervo):
    if len(acervo) == 0:
        acervo.adicionar(Livro("L001", "Dom Casmurro", 1899,
                               "Machado de Assis", 256))
        acervo.adicionar(Livro("L002", "O Cortiço", 1890,
                               "Aluísio Azevedo", 304))
        acervo.adicionar(DVD("D001", "Cidade de Deus", 2002, 130))
    return acervo


def modo_console(acervo):
    print(f"=== Acervo ({len(acervo)} itens) ===")
    for item in acervo:
        print(" ", item)

    print("\n--- Polimorfismo: prazo varia por tipo ---")
    for item in acervo:
        print(f"  {type(item).__name__:6} '{item.titulo}': "
              f"{item.prazo_dias()} dias")

    print("\n--- Empréstimo e tratamento de exceções ---")
    livro = acervo.buscar("L001")
    livro.emprestar()
    print(f"  '{livro.titulo}' emprestado.")
    try:
        livro.emprestar()                      # segunda vez -> erro
    except ErroBiblioteca as e:
        print(f"  Erro esperado: {e}")
    try:
        acervo.buscar("X999")
    except ErroBiblioteca as e:
        print(f"  Erro esperado: {e}")

    print("\n--- Persistência ---")
    acervo.salvar()
    print(f"  Salvo em {acervo.caminho}")
    recarregado = Acervo(ARQUIVO).carregar()
    print(f"  Recarregado: {len(recarregado)} itens, "
          f"{len(recarregado.emprestados())} emprestado(s)")
    livro.devolver()
    acervo.salvar()


def main():
    acervo = dados_de_exemplo(Acervo(ARQUIVO).carregar())

    if "--console" in sys.argv:
        modo_console(acervo)
        return

    try:
        from biblioteca.gui import JanelaBiblioteca
        JanelaBiblioteca(acervo).mainloop()
    except Exception as e:
        print(f"Não foi possível abrir a GUI ({e}).")
        print("Rodando em modo console...\n")
        modo_console(acervo)


if __name__ == "__main__":
    main()

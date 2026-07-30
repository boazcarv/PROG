"""
Capítulo 5 - Serialização e Persistência
Rode com:  python3 cap05_serializacao.py
Os arquivos gerados ficam na subpasta 'dados/'.
"""

import json
import csv
import pickle
import os
from pathlib import Path

PASTA = Path(__file__).parent / "dados"
PASTA.mkdir(exist_ok=True)


# ---------------------------------------------------------------
# 5.1 Persistência de dados em arquivos (texto puro e CSV)
# ---------------------------------------------------------------
def demo_texto():
    caminho = PASTA / "anotacoes.txt"

    # 'w' escreve (apaga o que existia), 'a' acrescenta, 'r' lê
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("Primeira linha\n")
        f.write("Segunda linha\n")

    with open(caminho, "a", encoding="utf-8") as f:
        f.write("Linha acrescentada depois\n")

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()

    print("Conteúdo de anotacoes.txt:")
    print(conteudo, end="")


def demo_csv():
    caminho = PASTA / "produtos.csv"
    produtos = [
        {"nome": "Teclado", "preco": 150.0, "qtd": 3},
        {"nome": "Mouse", "preco": 80.0, "qtd": 10},
    ]

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nome", "preco", "qtd"])
        escritor.writeheader()
        escritor.writerows(produtos)

    with open(caminho, newline="", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            print(f"  {linha['nome']:10} R$ {float(linha['preco']):8.2f} "
                  f"x {linha['qtd']}")


# ---------------------------------------------------------------
# 5.2 Serialização de objetos - JSON
# ---------------------------------------------------------------
class Livro:
    def __init__(self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    # objeto -> dicionário
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "disponivel": self.disponivel,
        }

    # dicionário -> objeto (método de classe = "construtor alternativo")
    @classmethod
    def from_dict(cls, d):
        return cls(d["titulo"], d["autor"], d["ano"], d["disponivel"])

    def __repr__(self):
        status = "disponível" if self.disponivel else "emprestado"
        return f"<Livro {self.titulo!r} ({self.ano}) - {status}>"


def salvar_json(livros, caminho):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump([l.to_dict() for l in livros], f,
                  indent=2, ensure_ascii=False)


def carregar_json(caminho):
    if not os.path.exists(caminho):
        return []
    with open(caminho, encoding="utf-8") as f:
        return [Livro.from_dict(d) for d in json.load(f)]


# ---------------------------------------------------------------
# 5.2 Serialização de objetos - pickle (binário, só Python)
# ---------------------------------------------------------------
def demo_pickle(livros):
    caminho = PASTA / "acervo.pkl"

    with open(caminho, "wb") as f:      # wb = write binary
        pickle.dump(livros, f)

    with open(caminho, "rb") as f:      # rb = read binary
        recuperados = pickle.load(f)

    print("  Objetos recuperados do pickle:", recuperados)
    print("  Tipo preservado?", type(recuperados[0]).__name__ == "Livro")


# ---------------------------------------------------------------
# DEMONSTRAÇÃO
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("--- 5.1 Arquivo de texto ---")
    demo_texto()

    print("\n--- 5.1 Arquivo CSV ---")
    demo_csv()

    print("\n--- 5.2 JSON ---")
    acervo = [
        Livro("Dom Casmurro", "Machado de Assis", 1899),
        Livro("O Cortiço", "Aluísio Azevedo", 1890, disponivel=False),
    ]
    caminho_json = PASTA / "acervo.json"
    salvar_json(acervo, caminho_json)
    print("  Arquivo JSON gerado:")
    print(caminho_json.read_text(encoding="utf-8"))
    print("  Lido de volta:", carregar_json(caminho_json))

    print("\n--- 5.2 Pickle ---")
    demo_pickle(acervo)

    print("\nArquivos criados em:", PASTA)
    for arq in sorted(PASTA.iterdir()):
        print("  -", arq.name, f"({arq.stat().st_size} bytes)")

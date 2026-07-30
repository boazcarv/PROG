"""
Capítulo 4 - Modularização e Pacotes (Namespaces)
Rode a partir da pasta cap04_pacotes:  python3 main.py
"""

import loja
from loja.modelos import Produto, Cliente     # graças ao __init__.py
from loja.servicos import Carrinho

if __name__ == "__main__":
    print(f"Loja v{loja.__version__}\n")

    cliente = Cliente("Ana Souza", "123.456.789-00")
    carrinho = Carrinho(cliente)
    carrinho.adicionar(Produto("Teclado", 150.00, 1))
    carrinho.adicionar(Produto("Mouse", 80.00, 2))
    carrinho.adicionar(Produto("Monitor", 900.00, 1))

    print(carrinho.resumo())

    print("\n--- Namespaces: mesmo nome, pacotes diferentes ---")
    from loja.modelos.produto import Produto as ProdutoModelo
    print("Produto veio de:", ProdutoModelo.__module__)

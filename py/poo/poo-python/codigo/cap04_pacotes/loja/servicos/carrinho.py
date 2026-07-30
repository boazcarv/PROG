"""Serviço de carrinho de compras."""

from ..modelos import Produto     # import RELATIVO (sobe um nível)


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens: list[Produto] = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        return sum(item.subtotal() for item in self.itens)

    def resumo(self):
        linhas = [f"Carrinho de {self.cliente}"]
        linhas += [f"  - {item} = R$ {item.subtotal():.2f}" for item in self.itens]
        linhas.append(f"  TOTAL: R$ {self.total():.2f}")
        return "\n".join(linhas)

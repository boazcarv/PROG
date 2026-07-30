"""Módulo que define o modelo Produto."""


class Produto:
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f} x {self.quantidade})"

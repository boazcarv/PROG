from __future__ import annotations
# ==============================================================================
# EXERCÍCIO 5: Diagrama UML do Sistema Completo (Representação em texto)[cite: 13]
# ==============================================================================
"""
 +-------------------+              +-------------------+
 |      Cliente      |  associa-se  |      Pedido       |
 +-------------------+ ------------>+-------------------+
 | + nome: str       |              | - _itens: list    |
 +-------------------+              +-------------------+
 | + fazer_pedido()  |              | + adicionar()     |
 +-------------------+              | + total()         |
                                    +-------------------+
                                              ◆ (Composição - Losango Fechado)[cite: 3, 4]
                                              |
                                              v
 +-------------------+              +-------------------+
 |      Produto      | ◇----------- |    ItemPedido     |
 +-------------------+ (Agregação)  +-------------------+
 | + nome: str       |              | + quantidade: int |
 | + preco: float    |              +-------------------+
 +-------------------+              | + subtotal()      |
                                    +-------------------+
"""

# ==============================================================================
# TESTANDO O CÓDIGO FUNCIONAL
# ==============================================================================
class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._jogadores: list[Jogador] = []

    def contratar(self, jogador: Jogador) -> None:
        # AGREGAÇÃO: Recebe o jogador já criado de fora
        if jogador not in self._jogadores:
            self._jogadores.append(jogador)

    def vender(self, jogador: Jogador) -> None:
        if jogador in self._jogadores:
            self._jogadores.remove(jogador)

    def listar_elenco(self) -> list[str]:
        return [j.nome for j in self._jogadores]


# Demonstração da troca de time
jogador1 = Jogador("Neymar")

time_a = Time("Time A")
time_b = Time("Time B")

time_a.contratar(jogador1)  
time_a.vender(jogador1)     
time_b.contratar(jogador1) 
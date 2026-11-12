from __future__ import annotations

# ==============================================================================
# SISTEMA DE PEDIDOS (Exercícios 1 e 2)
# ==============================================================================

class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto          # Agregação: produto existe fora do item[cite: 10]
        self.quantidade = quantidade

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente          # Associação com Cliente[cite: 11]
        self._itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        # Composição: o Pedido instancia o ItemPedido[cite: 11, 12]
        item = ItemPedido(produto, quantidade)
        self._itens.append(item)

    @property
    def total(self) -> float:
        return sum(i.subtotal for i in self._itens)

    # Exercício 2: Adicionando __str__ a Pedido[cite: 13]
    def __str__(self) -> str:
        linhas = [f"Pedido de: {self.cliente.nome}", "Itens:"]
        for item in self._itens:
            linhas.append(f"  - {item.produto.nome} x{item.quantidade}: R$ {item.subtotal:.2f}")
        linhas.append(f"Total: R$ {self.total:.2f}")
        return "\n".join(linhas)

class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._pedidos: list[Pedido] = []

    # Exercício 1: Método fazer_pedido()[cite: 13]
    def fazer_pedido(self) -> Pedido:
        # Cliente cria o Pedido internamente
        novo_pedido = Pedido(cliente=self)
        self._pedidos.append(novo_pedido)
        return novo_pedido

# Justificativa do Exercício 1[cite: 13]:
# A relação entre Cliente e Pedido no método 'fazer_pedido' é de Composição[cite: 3, 13], 
# pois o próprio Cliente é responsável por instanciar o objeto Pedido dentro do seu código[cite: 3, 11].


# ==============================================================================
# EXERCÍCIO 3: Prédio composto por Apartamentos (Composição)[cite: 13]
# ==============================================================================

class Apartamento:
    def __init__(self, numero: int, andar: int) -> None:
        self.numero = numero
        self.andar = andar

    def __repr__(self) -> str:
        return f"Apto {self.numero} ({self.andar}º andar)"

class Predio:
    def __init__(self, nome: str, andares: int, aptos_por_andar: int) -> None:
        self.nome = nome
        self._apartamentos: list[Apartamento] = []

        # COMPOSIÇÃO: O Prédio cria os Apartamentos diretamente no seu __init__[cite: 3, 13]
        num_apto = 101
        for andar in range(1, andares + 1):
            for _ in range(aptos_por_andar):
                self._apartamentos.append(Apartamento(numero=num_apto, andar=andar))
                num_apto += 1

    def listar_apartamentos(self) -> list[Apartamento]:
        return self._apartamentos


# ==============================================================================
# EXERCÍCIO 4: Time que agrega Jogadores (Agregação com troca de time)[cite: 13]
# ==============================================================================

class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome = nome

class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._jogadores: list[Jogador] = []

    def contratar(self, jogador: Jogador) -> None:
        # AGREGAÇÃO: Recebe o jogador criado externamente[cite: 6]
        if jogador not in self._jogadores:
            self._jogadores.append(jogador)

    def vender(self, jogador: Jogador) -> None:
        if jogador in self._jogadores:
            self._jogadores.remove(jogador)

    def listar_elenco(self) -> list[str]:
        return [j.nome for j in self._jogadores]


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
if __name__ == "__main__":
    # Teste Ex 1 e 2
    c1 = Cliente("João")
    p1 = c1.fazer_pedido()
    prod1 = Produto("X-Burguer", 20.0)
    prod2 = Produto("Refrigerante", 6.0)
    
    p1.adicionar(prod1, 2)
    p1.adicionar(prod2, 1)
    
    print("--- EXERCÍCIO 1 & 2 ---")
    print(p1)
    
    # Teste Ex 3
    print("\n--- EXERCÍCIO 3 ---")
    predio = Predio("Residencial Central", andares=2, aptos_por_andar=2)
    print(f"Prédio {predio.nome}: {predio.listar_apartamentos()}")

    # Teste Ex 4
    print("\n--- EXERCÍCIO 4 ---")
    j1 = Jogador("Neymar")
    t1 = Time("Santos")
    t2 = Time("PSG")

    t1.contratar(j1)
    print(f"Elenco Santos: {t1.listar_elenco()}")

    t1.vender(j1)
    t2.contratar(j1)
    print(f"Elenco Santos após venda: {t1.listar_elenco()}")
    print(f"Elenco PSG após compra: {t2.listar_elenco()}")
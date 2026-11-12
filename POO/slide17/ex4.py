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


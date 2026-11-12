from __future__ import annotations
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



# Módulo que define o controlador de entregas.
from typing import List, Optional

from entrega import Entrega

from exececao import EntregaInvalidaError, EntregaDuplicadaError

class ControleEntregas:
    def __init__(self) -> None:
        self.entregas: List[Entrega] = []

    def adicionar_entrega(self, entrega: Entrega) -> None:
        if not isinstance(entrega, Entrega):
            raise EntregaInvalidaError("A entrega fornecida não é válida.")

        for e in self.entregas:
            if e.codigo == entrega.codigo:
                raise EntregaDuplicadaError(f"Já existe uma entrega com o código '{entrega.codigo}'.")

        self.entregas.append(entrega)

    def buscar_entrega_por_codigo(self, codigo: str) -> Optional[Entrega]:
     
        for e in self.entregas:
            if e.codigo == codigo:
                return e


    def listar_entregas(self) -> List[Entrega]:
        """Retorna a lista de entregas na ordem de cadastro."""
        return list(self.entregas)

    def listar_entregas_ordenadas_por_data(self) -> List[Entrega]:
        """Retorna as entregas ordenadas pela data prevista (crescente)."""
        return sorted(self.entregas, key=lambda e: e.data_prevista)



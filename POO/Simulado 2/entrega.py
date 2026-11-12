from datetime import date

class Entrega:
    def __init__(self, codigo: str, data_prevista: date, peso: float, valor_frete: float):
        self.codigo = codigo
        self.data_prevista = date
        self._peso = peso
        self._valor_frete = valor_frete

    @property
    def peso(self) -> float:
        return self._peso
    
    @property
    def valor_frete(self):
        return self._valor_frete

    @peso.setter
    def peso(self, novo_peso):
        if novo_peso > 0:
            self._peso = novo_peso
            print("O peso foi alterado com sucesso!")
        else:
            raise ValueError("[ERRO] - O valor está inválido, o peso deve ser maior do que zero!")
    
    @valor_frete.setter
    def valor_frete(self, novo_valor_frete):
        if novo_valor_frete > 0:
            self._valor_frete = novo_valor_frete
        else:
            raise ValueError("[ERRO] - O valor está inválido, o peso deve ser maior do que zero!")
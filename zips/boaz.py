# Questão 1

class ContaBancaria:
    def __init__(self, saldo: float, titular: str):
        self.__saldo = saldo
        self.__titular = titular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def titular(self) -> str:
        return self.__titular

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor: float) -> bool:
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

conta = ContaBancaria(100.0, "Boaz")

conta.depositar(200.0)
print(f"Saldo após depósito: R$ {conta.saldo:.2f}")

conta.sacar(50.0)
print(f"Saldo após saque: R$ {conta.saldo:.2f}")

# Questão 2

from abc import ABC, abstractmethod

class FormaDePagamento(ABC):
    @abstractmethod 
    def processar_pagamento(self, valor: float) -> None:
        pass

class PagamentoPix(FormaDePagamento):
    def processar_pagamento(self, valor: float) -> None:
        valor_com_desconto = valor * 0.95
        print(f"Pagamento Pix de {valor_com_desconto} processado.")

class PagamentoCartao(FormaDePagamento):
    def processar_pagamento(self, valor: float) -> None:
        valor_com_taxa = valor * 0.98
        print(f"Pagamento Cartão de R${valor_com_taxa} processado.")

# Questão 3

class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        return self.salario_base

class Gerente(Funcionario):
    def __init__(self, nome: str, salario_base: float) -> float:
        def super().__init__():

class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, horas_extras: float) -> float:
        def super().__init__():
        






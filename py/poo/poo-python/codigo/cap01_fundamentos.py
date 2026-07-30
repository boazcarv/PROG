"""
Capítulo 1 - Fundamentos de POO
Todos os trechos que aparecem na apostila, reunidos e executáveis.
Rode com:  python3 cap01_fundamentos.py
"""

# ---------------------------------------------------------------
# 1.2 Classes, objetos, atributos e métodos
# ---------------------------------------------------------------
class Cachorro:
    """Molde (classe) para criar cachorros (objetos)."""

    def __init__(self, nome, raca, idade):
        self.nome = nome      # atributo de instância
        self.raca = raca
        self.idade = idade

    def latir(self):
        return f"{self.nome} diz: Au au!"

    def fazer_aniversario(self):
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos."


# ---------------------------------------------------------------
# 1.3 Estado e comportamento
# ---------------------------------------------------------------
class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo          # ESTADO

    def depositar(self, valor):     # COMPORTAMENTO
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True


# ---------------------------------------------------------------
# 1.4 Encapsulamento
# ---------------------------------------------------------------
class ContaSegura:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.__saldo = saldo_inicial     # atributo privado (name mangling)

    @property
    def saldo(self):
        """Getter: leitura liberada."""
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo.")
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco          # passa pelo setter!

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.__preco = valor


# ---------------------------------------------------------------
# 1.5 Composição
# ---------------------------------------------------------------
class Motor:
    def __init__(self, potencia_cv):
        self.potencia_cv = potencia_cv
        self.ligado = False

    def ligar(self):
        self.ligado = True
        return f"Motor de {self.potencia_cv}cv ligado."


class Carro:
    def __init__(self, modelo, potencia_cv):
        self.modelo = modelo
        self.motor = Motor(potencia_cv)   # o Carro TEM-UM Motor

    def ligar(self):
        return f"{self.modelo}: {self.motor.ligar()}"


# ---------------------------------------------------------------
# 1.6 Herança e Polimorfismo
# ---------------------------------------------------------------
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "..."

    def apresentar(self):
        return f"{self.nome} faz: {self.emitir_som()}"


class Gato(Animal):
    def emitir_som(self):
        return "Miau"


class Vaca(Animal):
    def emitir_som(self):
        return "Muuu"


class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"{self.nome}: R$ {self.calcular_salario():.2f}"


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas):
        super().__init__(nome, salario_base)      # reaproveita o pai
        self.total_vendas = total_vendas

    def calcular_salario(self):
        return self.salario_base + self.total_vendas * 0.05


# ---------------------------------------------------------------
# 1.7 Classes abstratas e Interfaces
# ---------------------------------------------------------------
from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        ...

    def descrever(self):
        return (f"{self.__class__.__name__}: "
                f"área={self.area():.2f}, perímetro={self.perimetro():.2f}")


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio


class Imprimivel(ABC):
    """Funciona como uma 'interface': só define o contrato."""
    @abstractmethod
    def imprimir(self): ...


class Exportavel(ABC):
    @abstractmethod
    def exportar_csv(self): ...


class Relatorio(Imprimivel, Exportavel):   # implementa 2 "interfaces"
    def __init__(self, titulo, linhas):
        self.titulo = titulo
        self.linhas = linhas

    def imprimir(self):
        return f"=== {self.titulo} ===\n" + "\n".join(self.linhas)

    def exportar_csv(self):
        return "\n".join(self.linhas)


# ---------------------------------------------------------------
# DEMONSTRAÇÃO
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("--- 1.2 Classes e objetos ---")
    rex = Cachorro("Rex", "Labrador", 3)
    mel = Cachorro("Mel", "Poodle", 5)
    print(rex.latir())
    print(mel.latir())
    print(rex.fazer_aniversario())

    print("\n--- 1.3 Estado e comportamento ---")
    c = ContaBancaria("Ana", 100.0)
    c.depositar(50)
    print("Saldo:", c.saldo, "| Saque de 500 deu certo?", c.sacar(500))

    print("\n--- 1.4 Encapsulamento ---")
    cs = ContaSegura("Bruno", 200)
    cs.depositar(100)
    print("Saldo:", cs.saldo)
    try:
        cs.sacar(9999)
    except ValueError as e:
        print("Erro capturado:", e)
    p = Produto("Caneta", 3.50)
    print("Preço:", p.preco)
    try:
        p.preco = -10
    except ValueError as e:
        print("Erro capturado:", e)

    print("\n--- 1.5 Composição ---")
    print(Carro("Fusca", 65).ligar())

    print("\n--- 1.6 Herança e polimorfismo ---")
    for a in [Gato("Frajola"), Vaca("Mimosa"), Animal("Bicho")]:
        print(a.apresentar())
    for f in [Funcionario("Carlos", 2000), Vendedor("Diana", 1500, 20000)]:
        print(f)

    print("\n--- 1.7 Abstratas e interfaces ---")
    for forma in [Retangulo(3, 4), Circulo(5)]:
        print(forma.descrever())
    try:
        FormaGeometrica()
    except TypeError as e:
        print("Erro esperado:", e)
    print(Relatorio("Vendas", ["jan;100", "fev;150"]).imprimir())

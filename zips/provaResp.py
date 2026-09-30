"""
Avaliacao 4 – Programacao Orientada a Objetos –
T3
Professor: Higor Morais
LEIA-ME:
- Utilizar POO em todas as questoes.
- Entregar em um unico arquivo .py.
- Utilizar nomes significativos para classes, atributos e metodos.
- Atencao ao encapsulamento, heranca e polimorfismo quando solicitado.
"""

"""
Questao 1 (30 pts)
Uma empresa de aluguel de veiculos deseja informatizar parte de seu sistema. Implemente uma
classe Veiculo com atributos marca, modelo, ano e valor_diaria. Crie construtor, exibir_dados() e
calcular_aluguel(qtd_dias). Valide ano>=1990 e diaria>0. Crie tres objetos, solicite os dias de
aluguel e exiba os valores finais.
"""


class Veiculo:
	def __init__(self, marca, modelo, ano, valor_diaria):
		if ano < 1990:
			raise ValueError("O ano deve ser maior ou igual a 1990.")
		if valor_diaria <= 0:
			raise ValueError("O valor da diaria deve ser maior que zero.")

		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.valor_diaria = valor_diaria

	def exibir_dados(self):
		print(f"Marca: {self.marca}")
		print(f"Modelo: {self.modelo}")
		print(f"Ano: {self.ano}")
		print(f"Valor da diaria: R$ {self.valor_diaria:.2f}")

	def calcular_aluguel(self, qtd_dias):
		if qtd_dias <= 0:
			raise ValueError("A quantidade de dias deve ser maior que zero.")
		return self.valor_diaria * qtd_dias


veiculos = [
	Veiculo("Renault", "Sandeiro", 2022, 180.00),
	Veiculo("JEEP", "Renegade", 2021, 120.00),
	Veiculo("Ford car", "Ford", 2023, 200.00),
]

for veiculo in veiculos:
	veiculo.exibir_dados()
	dias = int(input("Informe a quantidade de dias de aluguel: "))
	print(f"Valor final do aluguel: R$ {veiculo.calcular_aluguel(dias):.2f}\n")




"""
Questao 2 (30 pts)
Uma instituicao financeira deseja armazenar informacoes de contas bancarias. Implemente a
classe ContaBancaria com titular (publico), _agencia (protegido) e __saldo (privado). Crie
depositar(), sacar(), exibir_saldo() e getters/setters com @property. Valide saldo e operacoes.
"""


class ContaBancaria:
	def __init__(self, titular, agencia, saldo=0):
		self.titular = titular
		self._agencia = agencia
		self.saldo = saldo

	@property
	def agencia(self):
		return self._agencia

	@agencia.setter
	def agencia(self, valor):
		if not valor:
			raise ValueError("A agencia deve ser informada.")
		self._agencia = valor

	@property
	def saldo(self):
		return self.__saldo

	@saldo.setter
	def saldo(self, valor):
		if valor < 0:
			raise ValueError("O saldo nao pode ser negativo.")
		self.__saldo = valor

	def depositar(self, valor):
		if valor <= 0:
			raise ValueError("O valor do deposito deve ser maior que zero.")
		self.__saldo += valor

	def sacar(self, valor):
		if valor <= 0:
			raise ValueError("O valor do saque deve ser maior que zero.")
		if valor > self.__saldo:
			raise ValueError("Saldo insuficiente.")
		self.__saldo -= valor

	def exibir_saldo(self):
		print(f"Titular: {self.titular}")
		print(f"Agencia: {self._agencia}")
		print(f"Saldo: R$ {self.__saldo:.2f}")
"""
Questao 3 (40 pts)
Uma empresa de tecnologia deseja modelar Funcionario, Desenvolvedor e Designer. Implemente
heranca e sobrescrita de calcular_bonus(). Funcionario=5%, Desenvolvedor=15%, Designer=10%.
Utilize polimorfismo percorrendo uma lista de objetos.

"""
class Funcionario:
	def __init__(self, nome, salario):
		if salario <= 0:
			raise ValueError("O salario deve ser maior que zero.")
		self.nome = nome
		self.salario = salario
		self.cargo = "Funcionario"

	def calcular_bonus(self):
		return self.salario * 0.05


class Desenvolvedor(Funcionario):
	def __init__(self, nome, salario):
		super().__init__(nome, salario)
		self.cargo = "Desenvolvedor"

	def calcular_bonus(self):
		return self.salario * 0.15


class Designer(Funcionario):
	def __init__(self, nome, salario):
		super().__init__(nome, salario)
		self.cargo = "Designer"

	def calcular_bonus(self):
		return self.salario * 0.10

funcionarios = [
	Funcionario("Osmundo", 3000.00),
	Desenvolvedor("Vivian", 5000.00),
	Designer("Rosimere", 4000.00),
]

for funcionario in funcionarios:
	print(
		f"Nome: {funcionario.nome} - "
		f"Cargo: {funcionario.cargo} - "
		f"Salário: R$ {funcionario.salario:.2f} - "
		f"Bônus: "
		f"R$ {funcionario.calcular_bonus():.2f}"
	)
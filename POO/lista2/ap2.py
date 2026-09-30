class SalarioInvalidoError(Exception):
	pass


class EmailInvalidoError(Exception):
	pass


class Funcionario:
	SALARIO_MINIMO = 1412.00

	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario

	@property
	def salario(self):
		return self._salario

	@salario.setter
	def salario(self, valor):
		if valor < self.SALARIO_MINIMO:
			raise SalarioInvalidoError(
				f"O salário não pode ser menor que R$ {self.SALARIO_MINIMO:.2f}."
			)
		self._salario = valor

	def aumentar(self, percentual):
		if not 0 < percentual <= 30:
			raise ValueError("O percentual deve estar entre 0 e 30.")
		self.salario *= 1 + percentual / 100


class Email:
	def __init__(self, endereco):
		self.endereco = endereco

	@property
	def endereco(self):
		return self._endereco

	@endereco.setter
	def endereco(self, valor):
		if "@" not in valor or "." not in valor:
			raise EmailInvalidoError("O e-mail deve conter '@' e '.'.")
		self._endereco = valor


if __name__ == "__main__":
	try:
		Funcionario("Boaz", 1000)
	except SalarioInvalidoError as erro:
		print(erro)

	funcionario = Funcionario("Boaz", 2000)
	try:
		funcionario.aumentar(31)
	except ValueError as erro:
		print(erro)

	try:
		Email("boazgmail.com")
	except EmailInvalidoError as erro:
		print(erro)

	try:
		Email("boaz@gmailcom")
	except EmailInvalidoError as erro:
		print(erro)

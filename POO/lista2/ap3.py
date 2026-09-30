class ErroDeConta(Exception):
	"""Exceção base para erros da conta bancária."""

class ValorInvalidoError(ErroDeConta):
	pass

class SaldoInsuficienteError(ErroDeConta):
	pass

class LimiteExcedidoError(ErroDeConta):
	pass

class ContaBancaria:
	LIMITE_SAQUE = 1000.0

	def __init__(self, saldo=0.0):
		self._saldo = 0.0
		if saldo != 0:
			self.depositar(saldo)

	@property
	def saldo(self):
		return self._saldo

	def depositar(self, valor):
		self._validar_valor(valor)
		self._saldo += valor

	def sacar(self, valor):
		self._validar_valor(valor)
		if valor > self.LIMITE_SAQUE:
			raise LimiteExcedidoError("O limite de saque é R$ 1.000,00.")
		if valor > self._saldo:
			raise SaldoInsuficienteError("Saldo insuficiente.")
		self._saldo -= valor

	@staticmethod
	def _validar_valor(valor):
		if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor <= 0:
			raise ValorInvalidoError("O valor deve ser um número positivo.")

def caixa_eletronico():
	conta = ContaBancaria()
	while True:
		print("\n1 - Depositar\n2 - Sacar\n3 - Saldo\n4 - Sair")
		try:
			opcao = input("Escolha uma opção: ").strip()
			if opcao == "1":
				valor = float(input("Valor do depósito: ").replace(",", "."))
				conta.depositar(valor)
				print("Depósito realizado.")
			elif opcao == "2":
				valor = float(input("Valor do saque: ").replace(",", "."))
				conta.sacar(valor)
				print("Saque realizado.")
			elif opcao == "3":
				print(f"Saldo: R$ {conta.saldo:.2f}")
			elif opcao == "4":
				break
			else:
				print("Opção inválida.")
		except ErroDeConta as erro:
			print(f"Erro: {erro}")
		except (ValueError, TypeError, EOFError, KeyboardInterrupt):
			print("Entrada inválida.")


if __name__ == "__main__":
	caixa_eletronico()

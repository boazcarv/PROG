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
    def __init__(self, marca: str, modelo: str, ano: int, valor_diaria: float):
        if ano < 1990:
            raise ValueError("Ano deve ser maior ou igual a 1990.")
        if valor_diaria <= 0:
            raise ValueError("Valor da diária deve ser maior que zero.")    
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
       


    def exibir_dados(self) -> None:
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Valor Diária: {self.valor_diaria}")

    def calcular_aluguel(self, qtd_dias):
        aluguel = qtd_dias * self.valor_diaria
        print(f"O valor do aluguel para {qtd_dias} dias é: {aluguel}")
    


"""
Questao 2 (30 pts)
Uma instituicao financeira deseja armazenar informacoes de contas bancarias. Implemente a
classe ContaBancaria com titular (publico), _agencia (protegido) e __saldo (privado). Crie
depositar(), sacar(), exibir_saldo() e getters/setters com @property. Valide saldo e operacoes.
"""
class ContaBancaria:
    def __init__(self, titular: str, agencia, saldo=0):
        self.titular = titular
        self._agencia = agencia
        self.__saldo = saldo

    def exibir_titular(self):
        return self.titular
    
    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, valor):
        if not valor:
            raise ValueError("A agencia deve ser informada.")
        self._agencia = valor

    @property
    def exibir_saldo(self):
        return self.__saldo

    def depositar(self, valor) -> None:
        if self.__saldo >= 0 and valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com muito êxito!")
        else:
            print("Erro ao realizar o depósito!")

    def sacar(self, valor) -> None:
        if self.__saldo > 0 and valor > 0:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com muito êxito!")
        else:
            print("O valor para o saque deve ser maior do que zero!")


pessoa1 = ContaBancaria("Boaz Carvalho", 11022, saldo = 3000)
pessoa1.depositar(100)

"""
Questao 3 (40 pts)
Uma empresa de tecnologia deseja modelar Funcionario, Desenvolvedor e Designer. Implemente
heranca e sobrescrita de calcular_bonus(). Funcionario=5%, Desenvolvedor=15%, Designer=10%.
Utilize polimorfismo percorrendo uma lista de objetos.
"""

class Funcionario:
    def __init__(self, nome: str, salario=0):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.05

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15

class Design(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

funcionarios = [
    Desenvolvedor("Boaz Carvalho", 12500),
    Design("Vivian Varela", 5000)
]

for funcionario in funcionarios:
    print(f"Funcionário: {funcionario.nome} | Salário: {funcionario.salario} | Bonus: {funcionario.calcular_bonus():.2f}")
    

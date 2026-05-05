

# Questão 1 - Imposto de Renda
salario = float(input("Q1) Digite o salário (R$): "))

if salario <= 1903.98:
    aliquota = 0.0
elif salario <= 2826.65:
    aliquota = 0.075
elif salario <= 3751.05:
    aliquota = 0.15
elif salario <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275


imposto = salario * aliquota
print(f"Imposto a pagar: R$ {imposto:.2f}")
#TEMOS OUTRA OPÇÃO DE DISFECHAR O PROBLEMA, USANDO O VALOR DO IMPOSTO PARA CADA FAIXA, COMO MOSTRA O CÓDIGO ABAIXO:
#salario = float(input("Salário: R$ "))


# Questão 2 - Ano bissexto
ano = int(input("\nQ2) Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano informado é bissexto.")
else:
    print("O ano informado não é bissexto.")


# Questão 3 - Número entre 1 e 10
num = int(input("\nQ3) Digite um número entre 1 e 10: "))

if 1 <= num <= 10:
    print("O número digitado está DENTRO da faixa solicitada.")
else:
    print("O número digitado está FORA da faixa solicitada.")


# Questão 4 - Maior entre dois valores
v1 = float(input("\nQ4) Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

if v1 > v2:
    print(f"O maior valor é: {v1:.2f}")
elif v2 > v1:
    print(f"O maior valor é: {v2:.2f}")
else:
    print("Os dois valores são iguais.")


# Questão 5 - Diferença entre maior e menor (inteiros)

num1 = int(input("\nQ5) Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
if num1 > num2:
    difenca = num1 - num2
else:
    difenca = num2 - num1
print(f"A diferença entre o maior e o menor número é: {difenca}")



# 1
salario = float(input("Digite o valor do salário: R$ "))

if salario <= 1903.98:
    print("Isento de imposto de renda.")
elif salario <= 2826.65:
    print(f"Imposto: R$ {salario * 0.075:.2f}")
elif salario <= 3751.05:
    print(f"Imposto: R$ {salario * 0.15:.2f}")
elif salario <= 4664.68:
    print(f"Imposto: R$ {salario * 0.225:.2f}")
else:
    print(f"Imposto: R$ {salario * 0.275:.2f}")


# 2
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("É bissexto.")
else:
    print("Não é bissexto.")


# 3
numero = float(input("Digite um número entre 1 e 10: "))

if 1 <= numero <= 10:
    print("O número digitado está DENTRO da faixa solicitada.")
else:
    print("O número digitado está FORA da faixa solicitada.")


# 4
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("Maior valor:", valor1)
elif valor2 > valor1:
    print("Maior valor:", valor2)
else:
    print("Os dois valores são iguais.")


# 5
inteiro1 = int(input("Digite o primeiro valor inteiro: "))
inteiro2 = int(input("Digite o segundo valor inteiro: "))

print("Diferença:", abs(inteiro1 - inteiro2))


# 6
v1 = int(input("Digite o 1º valor inteiro: "))
v2 = int(input("Digite o 2º valor inteiro: "))
v3 = int(input("Digite o 3º valor inteiro: "))

valores = [v1, v2, v3]
valores.sort()
print("Ordem crescente:", valores)


# 7
a = int(input("Digite o 1º valor inteiro: "))
b = int(input("Digite o 2º valor inteiro: "))
c = int(input("Digite o 3º valor inteiro: "))

lista = [a, b, c]
ordem = input("Digite C para crescente ou D para decrescente: ").strip().upper()

if ordem == "C":
    lista.sort()
    print("Ordem crescente:", lista)
elif ordem == "D":
    lista.sort(reverse=True)
    print("Ordem decrescente:", lista)
else:
    print("Opção inválida.")


# 8
l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 == l3:
        print("Triângulo equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Não forma triângulo.")

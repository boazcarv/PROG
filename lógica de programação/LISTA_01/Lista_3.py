# 1
for i in range(1, 101):
	print(i)


# 2
for i in range(100, 0, -1):
	print(i)


# 3
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio > fim:
	inicio, fim = fim, inicio

soma_intervalo = 0
for i in range(inicio, fim + 1):
	print(i)
	soma_intervalo += i

print("Somatório do intervalo:", soma_intervalo)


# 4
soma_10 = 0
for _ in range(10):
	numero = float(input("Digite um número: "))
	soma_10 += numero

print("Somatório dos 10 números:", soma_10)


# 5
soma_menores_10 = 0
for _ in range(5):
	valor = float(input("Digite um valor: "))
	if valor < 10:
		soma_menores_10 += valor

print("Somatório dos valores menores que 10:", soma_menores_10)


# 6
soma_entre_10_e_20 = 0
for _ in range(5):
	valor = float(input("Digite um valor: "))
	if 10 <= valor < 20:
		soma_entre_10_e_20 += valor

print("Somatório dos valores >= 10 e < 20:", soma_entre_10_e_20)


# 7
soma_pares = 0
for _ in range(5):
	valor = int(input("Digite um valor inteiro: "))
	if valor % 2 == 0:
		soma_pares += valor

print("Somatório dos valores pares digitados:", soma_pares)


# 8 
quantidade = int(input("Quantos valores você vai digitar? "))
cont_pares = 0

for _ in range(quantidade):
	valor = int(input("Digite um valor inteiro: "))
	if valor % 2 == 0:
		cont_pares += 1

print("Quantidade de números pares digitados:", cont_pares)


# 9
soma_pos_impares = 0
soma_pos_pares = 0

for posicao in range(1, 11):
	valor = float(input(f"Digite o {posicao}º valor: "))
	if posicao % 2 != 0:
		soma_pos_impares += valor
	else:
		soma_pos_pares += valor

print("Soma das posições ímpares:", soma_pos_impares)
print("Soma das posições pares:", soma_pos_pares)

if soma_pos_impares > soma_pos_pares:
	print("O somatório das posições ímpares é MAIOR.")
elif soma_pos_impares < soma_pos_pares:
	print("O somatório das posições ímpares é MENOR.")
else:
	print("Os somatórios são IGUAIS.")


# 10
soma_valores_pares = 0
soma_valores_impares = 0

for _ in range(10):
	valor = int(input("Digite um valor inteiro: "))
	if valor % 2 == 0:
		soma_valores_pares += valor
	else:
		soma_valores_impares += valor

print("Soma dos números pares:", soma_valores_pares)
print("Soma dos números ímpares:", soma_valores_impares)

if soma_valores_impares > soma_valores_pares:
	print("Somatório dos ímpares é MAIOR.")
elif soma_valores_impares < soma_valores_pares:
	print("Somatório dos ímpares é MENOR.")
else:
	print("Somatórios IGUAIS.")


# 11
total = int(input("Digite o total de números a serem somados: "))
numeros = []

for _ in range(total):
	n = int(input("Digite um número: "))
	numeros.append(n)

expressao = "+".join(str(x) for x in numeros)
resultado = sum(numeros)
print(f"{expressao}={resultado}")
# soma = 0
# expressao = ""
# for i in range(total):
#    n = int(input("Digite um número: "))
#    soma += n
#    expressao += str(n) + ("+" if i < total - 1 else "")
#
#print(f"{expressao}={soma}")
#------------------------------------------------------------------------------
# 12
lista_div7 = []
for i in range(1000, 3001):
	if i % 7 == 0 and i % 5 != 0:
		lista_div7.append(str(i))

print(";".join(lista_div7))


# 13
num_tabuada = int(input("Digite um número para a tabuada: "))
saida_tabuada = []

for i in range(1, 11):
	saida_tabuada.append(f"{i}x{num_tabuada}={i * num_tabuada}")

print(";".join(saida_tabuada) + ";")


# 14
def imprimir_triangulo(tamanho):
	# Primeiro imprime as linhas crescentes e depois as decrescentes para formar o triângulo
	for i in range(1, tamanho + 1):
		print("* " * i)
	for i in range(tamanho - 1, 0, -1):
		print("* " * i)


t1 = int(input("Digite o primeiro tamanho do triângulo: "))
t2 = int(input("Digite o segundo tamanho do triângulo: "))

imprimir_triangulo(t1)
print()
imprimir_triangulo(t2)


# 15
pares = 0
impares = 0

while True:
	valor = int(input("Digite um número (negativo para parar): "))
	if valor < 0:
		break

	if valor % 2 == 0:
		pares += 1
	else:
		impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)


# 16
limite = int(input("Digite um valor inteiro: "))
sequencia = []

for i in range(1, limite + 1):
	if i % 3 == 0 and i % 7 == 0:
		sequencia.append("POW")
	elif i % 3 == 0:
		sequencia.append("PI")
	elif i % 7 == 0:
		sequencia.append("PA")
	else:
		sequencia.append(str(i))

print(" ".join(sequencia))

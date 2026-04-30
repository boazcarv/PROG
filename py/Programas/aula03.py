import math


def exercicio_1_calculadora_simples():
	print("\n1) Calculadora Simples")
	valor1 = float(input("Digite o primeiro valor: "))
	valor2 = float(input("Digite o segundo valor: "))

	soma = valor1 + valor2
	subtracao = valor1 - valor2
	multiplicacao = valor1 * valor2
	divisao = valor1 / valor2 if valor2 != 0 else None

	print(f"Soma: {soma}")
	print(f"Subtração: {subtracao}")
	print(f"Multiplicação: {multiplicacao}")
	if divisao is None:
		print("Divisão: não é possível dividir por zero.")
	else:
		print(f"Divisão: {divisao}")


def exercicio_2_conversor_temperatura():
	print("\n2) Conversor de Temperatura")
	celsius = float(input("Digite a temperatura em Celsius: "))
	fahrenheit = (celsius * 9 / 5) + 32
	print(f"Temperatura em Fahrenheit: {fahrenheit}")


def exercicio_3_area_circulo():
	print("\n3) Área do Círculo")
	raio = float(input("Digite o raio do círculo: "))
	area = math.pi * (raio ** 2)
	print(f"Área do círculo: {area}")


def exercicio_4_area_triangulo():
	print("\n4) Área do Triângulo")
	base = float(input("Digite a base do triângulo: "))
	altura = float(input("Digite a altura do triângulo: "))
	area = (base * altura) / 2
	print(f"Área do triângulo: {area}")


def exercicio_5_volume_esfera():
	print("\n5) Volume da Esfera")
	raio = float(input("Digite o raio da esfera: "))
	volume = (4 / 3) * math.pi * (raio ** 3)
	print(f"Volume da esfera: {volume}")


def exercicio_6_media_aritmetica():
	print("\n6) Calculadora de Média Aritmética")
	nota1 = float(input("Digite a nota 1: "))
	nota2 = float(input("Digite a nota 2: "))
	nota3 = float(input("Digite a nota 3: "))

	media = (nota1 + nota2 + nota3) / 3

	print(f"Notas digitadas: {nota1}, {nota2}, {nota3}")
	print(f"Média aritmética: {media}")


def exercicio_7_media_ponderada():
	print("\n7) Calculadora de Média Ponderada")
	nota1 = float(input("Digite a nota 1: "))
	peso1 = float(input("Digite o peso da nota 1: "))

	nota2 = float(input("Digite a nota 2: "))
	peso2 = float(input("Digite o peso da nota 2: "))

	nota3 = float(input("Digite a nota 3: "))
	peso3 = float(input("Digite o peso da nota 3: "))

	nota4 = float(input("Digite a nota 4: "))
	peso4 = float(input("Digite o peso da nota 4: "))

	soma_pesos = peso1 + peso2 + peso3 + peso4
	if soma_pesos == 0:
		print("Não é possível calcular média ponderada com soma de pesos igual a zero.")
		return

	media_ponderada = (
		(nota1 * peso1)
		+ (nota2 * peso2)
		+ (nota3 * peso3)
		+ (nota4 * peso4)
	) / soma_pesos

	print(f"Média ponderada: {media_ponderada}")


def exercicio_8_equacao_segundo_grau():
	print("\n8) Equação de Segundo Grau (y = ax² + bx + c)")
	a = float(input("Digite o valor de a: "))
	b = float(input("Digite o valor de b: "))
	c = float(input("Digite o valor de c: "))
	x = float(input("Digite o valor de x: "))

	y = a * (x ** 2) + b * x + c
	print(f"Valor de y: {y}")


def exercicio_9_imc():
	print("\n9) Calculadora de IMC")
	peso = float(input("Digite o peso (kg): "))
	altura = float(input("Digite a altura (m): "))

	if altura <= 0:
		print("Altura deve ser maior que zero.")
		return

	imc = peso / (altura ** 2)
	print(f"IMC calculado: {imc}")


def exercicio_10_tabuada():
	print("\n10) Tabuada")
	numero = float(input("Digite um número para ver a tabuada: "))

	for i in range(1, 11):
		resultado = numero * i
		print(f"{numero} x {i} = {resultado}")


def exercicio_11_segundos_para_hms():
	print("\n11) Conversão de Segundos para HORA:MINUTO:SEGUNDO")
	total_segundos = int(input("Digite a quantidade de segundos: "))

	horas = total_segundos // 3600
	restante = total_segundos % 3600
	minutos = restante // 60
	segundos = restante % 60

	print(f"Formato HORA:MINUTO:SEGUNDO = {horas:02d}:{minutos:02d}:{segundos:02d}")


def mostrar_menu():
	print("\n===== LISTA DE EXERCÍCIOS =====")
	print("1 - Calculadora Simples")
	print("2 - Conversor de Temperatura")
	print("3 - Área do Círculo")
	print("4 - Área do Triângulo")
	print("5 - Volume da Esfera")
	print("6 - Média Aritmética")
	print("7 - Média Ponderada")
	print("8 - Equação de Segundo Grau")
	print("9 - IMC")
	print("10 - Tabuada")
	print("11 - Segundos para H:M:S")
	print("0 - Sair")


def executar_exercicio(opcao):
	if opcao == 1:
		exercicio_1_calculadora_simples()
	elif opcao == 2:
		exercicio_2_conversor_temperatura()
	elif opcao == 3:
		exercicio_3_area_circulo()
	elif opcao == 4:
		exercicio_4_area_triangulo()
	elif opcao == 5:
		exercicio_5_volume_esfera()
	elif opcao == 6:
		exercicio_6_media_aritmetica()
	elif opcao == 7:
		exercicio_7_media_ponderada()
	elif opcao == 8:
		exercicio_8_equacao_segundo_grau()
	elif opcao == 9:
		exercicio_9_imc()
	elif opcao == 10:
		exercicio_10_tabuada()
	elif opcao == 11:
		exercicio_11_segundos_para_hms()
	elif opcao == 0:
		print("Encerrando programa...")
	else:
		print("Opção inválida. Tente novamente.")


def main():
	while True:
		mostrar_menu()
		try:
			opcao = int(input("Escolha uma opção: "))
		except ValueError:
			print("Digite um número inteiro válido.")
			continue

		if opcao == 0:
			executar_exercicio(opcao)
			break

		executar_exercicio(opcao)


if __name__ == "__main__":
	main()

# --------------------- Questão 01 ---------------------
# código da questão aqui
preco_base = 30.00
total = 0
preco_quarta = total * 0.20

idade = int(input("Digite sua idade: "))
if idade > 120:
    print("Idade Inválida!")
elif idade < 0:
    print("Idade Inválida!")

  

if idade <= 12:
    total = preco_base * 0.50
    print(f"Preço total para criança é: {total}")
elif 13 <= idade <= 25:
    total = preco_base * 0.30
    print(f"Preço total para estudante é: {total}")
elif idade >= 60:
    total = preco_base * 0.40
    print(f"Preço total para idosos é: {total}")
else:
    print("Sem desconto")

dia_semana = (input("Digite para qual dia da semana serão os ingressos: "))

if dia_semana == "Segunda" or "segunda":
    dia_semana = "segunda"
elif dia_semana == "Terça" or "terça":
    dia_semana = "terça"
elif dia_semana == "Quarta" or "quarta":
    preco_quarta = total * 0.20
    print(f"O preço referente a este dia da semana é: {preco_quarta}")
elif dia_semana == "Quinta" or "quinta":
    dia_semana = "quinta"
elif dia_semana == "Sexta" or "sexta":
    dia_semana = "sexta"
elif dia_semana == "Sábado" or "sábado":
    dia_semana = "sexta"
else:
    dia_semana = "domingo"

print(f"Sua idade é {idade} anos, o dia escolhido para ver o filme foi {dia_semana}, e o preço será: {total:.2f}")
    

# --------------------- Questão 02 ---------------------
print("Avaliação de Desempenho dos Vendedores (1º Trimestre)")

# Início: cabeçalho que informa o propósito do programa ao usuário
# Este bloco pede ao usuário a quantidade de vendedores que serão avaliados
# e valida se o número está entre 2 e 8 (inclusive).

while True:
	# Solicita repetidamente até o usuário informar um valor válido
	n = int(input("Informe a quantidade de vendedores (2 a 8): "))
	# Validação: aceitar apenas entre 2 e 8
	if 2 <= n <= 8:
		break
	# Mensagem de erro caso o valor esteja fora do intervalo permitido
	print("Erro: a quantidade de vendedores deve estar entre 2 e 8.")

qtd_destaque = 0      # Contador de vendedores com classificação "Destaque"
maior_media = 0.0     # Guarda a maior média mensal encontrada
total_geral_vendas = 0.0  # Soma de todas as vendas do grupo

for vendedor in range(1, n + 1):
	# Indica ao usuário qual vendedor está sendo informado
	print(f"\nVendedor {vendedor}")

	# Leitura e validação das vendas de janeiro
	while True:
		janeiro = float(input("Venda de Janeiro: R$ "))
		# Garante que o valor não seja negativo
		if janeiro >= 0:
			break
		print("Erro: o valor da venda deve ser maior ou igual a 0.")

	# Leitura e validação das vendas de fevereiro
	while True:
		fevereiro = float(input("Venda de Fevereiro: R$ "))
		if fevereiro >= 0:
			break
		print("Erro: o valor da venda deve ser maior ou igual a 0.")

	# Leitura e validação das vendas de março
	while True:
		marco = float(input("Venda de Março: R$ "))
		if marco >= 0:
			break
		print("Erro: o valor da venda deve ser maior ou igual a 0.")

	# Cálculo do total do vendedor e média mensal
	total_vendedor = janeiro + fevereiro + marco
	media_mensal = total_vendedor / 3

	# Classificação e cálculo de bônus conforme média mensal
	if media_mensal >= 5000:
		classificacao = "Destaque"
		bonus = total_vendedor * 0.10  # 10% de bônus
		qtd_destaque += 1
	elif media_mensal >= 2000:
		classificacao = "Regular"
		bonus = total_vendedor * 0.05  # 5% de bônus
	else:
		classificacao = "Abaixo da Meta"
		bonus = 0.0

	# Atualiza maior média encontrada e soma total das vendas
	if vendedor == 1 or media_mensal > maior_media:
		maior_media = media_mensal
	total_geral_vendas += total_vendedor

	# Exibe os resultados deste vendedor
	print(f"Média mensal: R$ {media_mensal:.2f}")
	print(f"Classificação: {classificacao}")
	print(f"Bônus: R$ {bonus:.2f}")


print("\n Resumo Geral ")
# Resumo final com os principais indicadores calculados
print(f"Quantidade de vendedores Destaque: {qtd_destaque}")
print(f"Maior média do grupo: R$ {maior_media:.2f}")
print(f"Total geral de vendas: R$ {total_geral_vendas:.2f}")

# --------------------- Questão 03 ---------------------
# código da questão aqui


# --------------------- Questão ... ---------------------
# código da questão aqui

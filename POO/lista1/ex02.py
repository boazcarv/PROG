# Exercício 02 - Estruturas sequenciais
# Lê a idade em anos, meses e dias e a converte para dias
# (1 ano = 365 dias, 1 mês = 30 dias).

anos = int(input('Quantos anos? '))
meses = int(input('Quantos meses? '))
dias = int(input('Quantos dias? '))

total_dias = anos * 365 + meses * 30 + dias
print(f'A idade expressa em dias é: {total_dias} dias')

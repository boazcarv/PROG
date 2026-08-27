'''
Questao 04 - Estruturas sequenciais
Salário do funcionário: por cada filho, 3% a mais sobre
o salário bruto
'''
nome = input('Nome completo do funcionário: ')
horas = float(input('Horas trabalhadas por mês: '))
valor_hora = float(input('Valor por hora trabalhada (R$): '))
filhos = int(input('Número de filhos: '))

salario_bruto = horas * valor_hora
salario_final = salario_bruto * (1 + 0.03 * filhos)

print(f'Funcionário: {nome}')
print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'Salário final ({filhos} filho(s), 3% cada): R$ {salario_final:.2f}')

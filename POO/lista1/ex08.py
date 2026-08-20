# Exercício 08 - Estruturas sequenciais
# Custo ao consumidor = custo de fábrica + 28% (distribuidor)
# + 45% (impostos), ambos aplicados ao custo de fábrica.

custo_fabrica = float(input('Custo de fábrica do carro (R$): '))
distribuidor = 0.28
impostos = 0.45

custo_final = custo_fabrica * (1 + distribuidor + impostos)
print(f'Custo final ao consumidor: R$ {custo_final:.2f}')

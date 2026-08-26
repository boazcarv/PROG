'''
Questao 05 - Estruturas sequenciais
18 W por m²; lâmpadas de 60 W. Quantas são necessárias?
'''
import math

largura = float(input('Largura da sala (m): '))
profundidade = float(input('Profundidade da sala (m): '))

area = largura * profundidade
potencia_necessaria = area * 18
lampadas = math.ceil(potencia_necessaria / 60)

print(f'Área da sala: {area:.2f} m²')
print(f'Potência total necessária: {potencia_necessaria:.0f} W')
print(f'Quantidade de lâmpadas de 60 W: {lampadas}')

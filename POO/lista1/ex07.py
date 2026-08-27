'''
Questao 07 - Estruturas sequenciais
Conversão de Fahrenheit para Celsius: C = (F - 32) * 5/9
'''
fahrenheit = float(input('Temperatura em graus Fahrenheit: '))
celsius = (fahrenheit - 32) * 5 / 9

print(f'{fahrenheit:.2f} °F correspondem a {celsius:.2f} °C.')

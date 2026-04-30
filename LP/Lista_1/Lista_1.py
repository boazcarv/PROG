



# Questão 1 - Calculadora Simples

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Questão 2 - Conversor de Temperatura

c = float(input('Digite a temperatura em grau Celsius: '))
f = (c * 1.8 + 32)
print('A temperatura em Fahrenheit é:', f)

# Questão 3 - Área do Círculo

r = float(input('Digite o raio do círculo: '))
a = 3.14 * r**2
print('A área do círculo é:', a)

# Questão 4 - Área do Triângulo

b = float(input('Digite a base do triângulo: '))
h = float(input('Digite a altura do triângulo: '))
a = (b * h) / 2
print('A área do triângulo é:', a)

# Questão 5 - Volume da Esfera

r = float(input('Digite o raio da esfera: '))
v = (4/3) * 3.14 * r**3
print('O volume da esfera é:', v)

# Questão 6 - Calculadora de Média Aritmética

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
print('A média aritmética é:', media)

# Questão 7 - Calculadora de Média Ponderada

n1 = float(input('Digite a primeira nota: '))
p1 = float(input('Digite o peso da primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
p2 = float(input('Digite o peso da segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
p3 = float(input('Digite o peso da terceira nota: '))
media_ponderada = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
print('A média ponderada é:', media_ponderada) 

# Questão 8 - Equação de Segundo Grau

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))
delta = b**2 - 4*a*c
if delta < 0:
    print('A equação não possui raízes reais.')
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print('As raízes da equação são:', x1, 'e', x2)

# Questão 9 - Calculadora de IMC

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura**2)
print('Seu IMC é:', imc)
if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif imc < 25:
    print('Classificação: Peso normal')
elif imc < 30:
    print('Classificação: Sobrepeso')
else:
    print('Classificação: Obesidade')

# Questão 10 - Tabuada

n = int(input('Digite um número para a tabuada: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

# Questão 11 - Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO

segundos = int(input('Digite o número de segundos: '))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segs = segundos % 60
print(f'{horas:02d}:{minutos:02d}:{segs:02d}')

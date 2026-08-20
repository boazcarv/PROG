# ============================================================
# Exercício 10 - Estruturas condicionais
# Informa qual dos dois valores é o maior.
# ============================================================

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

if a > b:
    print(f'{a} é o maior valor.')
elif b > a:
    print(f'{b} é o maior valor.')
else:
    print('Os dois valores são iguais.')

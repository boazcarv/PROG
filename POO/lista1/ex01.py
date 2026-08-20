# Exercício 01 - Estruturas sequenciais
# Leia 4 notas, mostre as notas digitadas e a média aritmética.

notas = []
for i in range(1, 5):
    notas.append(float(input(f'Digite a nota {i}: ')))

print('Notas digitadas:', notas)
media = sum(notas) / len(notas)
print(f'Média aritmética: {media:.2f}')

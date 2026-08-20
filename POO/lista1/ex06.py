# ============================================================
# Exercício 06 - Estruturas sequenciais
# Percentual de votos brancos, nulos e válidos sobre o total
# de eleitores.
# ============================================================

brancos = int(input('Votos brancos: '))
nulos = int(input('Votos nulos: '))
validos = int(input('Votos válidos: '))

total = brancos + nulos + validos

print(f'Brancos: {brancos / total * 100:.2f}%')
print(f'Nulos:   {nulos / total * 100:.2f}%')
print(f'Válidos: {validos / total * 100:.2f}%')

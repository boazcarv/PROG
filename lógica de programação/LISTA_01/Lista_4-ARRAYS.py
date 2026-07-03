# ============================================================
# EXERCÍCIO 1 — Contagem de Valores Pares
# ============================================================
print("--- EXERCÍCIO 1: Contagem de Valores Pares ---")
print("Digite 10 valores inteiros separados por espaço:")
valores = input().split()
lista = [0] * 10
i = 0
while i < 10:
    lista[i] = int(valores[i])
    i = i + 1

qtd_par = 0
i = 0
while i < 10:
    if lista[i] != 0 and lista[i] % 2 == 0:
        qtd_par = qtd_par + 1
    i = i + 1

print("Qtd valores par:", qtd_par)

# ============================================================
# EXERCÍCIO 2 — Soma de Pares e Ímpares de Duas Listas
# ============================================================
print("Digite o tamanho das listas:")
n = int(input())
lista1 = [int(x) for x in input(f"Digite os {n} valores da lista 1:\n").split()]
lista2 = [int(x) for x in input(f"Digite os {n} valores da lista 2:\n").split()]

soma_par1 = soma_par2 = soma_impar1 = soma_impar2 = 0

for i in range(n):
    if lista1[i] % 2 == 0:
        soma_par1 += lista1[i]
    else:
        soma_impar1 += lista1[i]
    if lista2[i] % 2 == 0:
        soma_par2 += lista2[i]
    else:
        soma_impar2 += lista2[i]

print(f"Soma listaPar1: {soma_par1}")
print(f"Soma listaPar2: {soma_par2}")
if soma_par1 > soma_par2:
    print(f"listaPar1 > listaPar2")
elif soma_par1 < soma_par2:
    print(f"listaPar1 < listaPar2")
else:
    print(f"listaPar1 = listaPar2")

print(f"Soma listaImpar1: {soma_impar1}")
print(f"Soma listaImpar2: {soma_impar2}")
if soma_impar1 > soma_impar2:
    print(f"listaImpar1 > listaImpar2")
elif soma_impar1 < soma_impar2:
    print(f"listaImpar1 < listaImpar2")
else:
    print(f"listaImpar1 = listaImpar2")

# ============================================================
# EXERCÍCIO 3 — Contagem de Valores Primos
# ============================================================
print("Digite 10 valores inteiros separados por espaço:")
valores = input().split()
lista = [0] * 10
i = 0
while i < 10:
    lista[i] = int(valores[i])
    i = i + 1

qtd_primos = 0
i = 0
while i < 10:
    num = lista[i]
    if num <= 1:
        pass
    else:
        eh_primo = True
        j = 2
        while j * j <= num:
            if num % j == 0:
                eh_primo = False
            else:
                j = j + 1
        if eh_primo == True:
            qtd_primos = qtd_primos + 1
    i = i + 1

print("Quantidade de valores primos:", qtd_primos)

# ============================================================
# EXERCÍCIO 4 — Intercalação de Duas Listas
# ============================================================
print("--- EXERCÍCIO 4: Intercalação de Duas Listas ---")
print("Digite o tamanho das listas:")
n = int(input())
print("Digite os", n, "valores da lista 1:")
vals1 = input().split()
print("Digite os", n, "valores da lista 2:")
vals2 = input().split()

lista1 = []
lista2 = []
lista3 = [None] * (n * 2)

i = 0
while i < n:
    v1 = vals1[i]
    if v1 == "True":
        lista1[i] = True
    elif v1 == "False":
        lista1[i] = False
    else:
        try:
            lista1[i] = int(v1)
        except:
            lista1[i] = v1.strip("'")

    v2 = vals2[i]
    if v2 == "True":
        lista2[i] = True
    elif v2 == "False":
        lista2[i] = False
    else:
        try:
            lista2[i] = int(v2)
        except:
            lista2[i] = v2.strip("'")
    i = i + 1

 # Intercalar
i = 0
k = 0
while i < n:
    lista3[k] = lista1[i]
    lista3[k + 1] = lista2[i]
    k = k + 2
    i = i + 1

 # Formatar saída - lista1
resultado1 = "["
i = 0
while i < n:
    if type(lista1[i]) == str:
        resultado1 = resultado1 + "'" + str(lista1[i]) + "'"
    else:
        resultado1 = resultado1 + str(lista1[i])
    if i < n - 1:
        resultado1 = resultado1 + ", "
    i = i + 1
resultado1 = resultado1 + "]"

# Formatar saída - lista2
resultado2 = "["
i = 0
while i < n:
    if type(lista2[i]) == str:
        resultado2 = resultado2 + "'" + str(lista2[i]) + "'"
    else:
        resultado2 = resultado2 + str(lista2[i])
    if i < n - 1:
        resultado2 = resultado2 + ", "
    i = i + 1
resultado2 = resultado2 + "]"

# Formatar saída - lista3
resultado3 = "["
i = 0
while i < n * 2:
    if type(lista3[i]) == str:
        resultado3 = resultado3 + "'" + str(lista3[i]) + "'"
    else:
        resultado3 = resultado3 + str(lista3[i])
    if i < n * 2 - 1:
        resultado3 = resultado3 + ", "
    i = i + 1
resultado3 = resultado3 + "]"

print("lista1 =", resultado1)
print("lista2 =", resultado2)
print("lista3 =", resultado3)

# ============================================================
# EXERCÍCIO 5 — Menor, Maior e Média Aritmética
# ============================================================
print("Digite a quantidade de valores:")
n = int(input())
print("Digite os", n, "valores:")
valores = input().split()
lista = [0] * n
i = 0
while i < n:
    lista[i] = int(valores[i])
    i = i + 1

menor = lista[0]
maior = lista[0]
soma = 0

i = 0
while i < n:
    if lista[i] < menor:
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
    soma = soma + lista[i]
    i = i + 1

media = soma // n

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Média aritmética:", media)

# ============================================================
# EXERCÍCIO 6 — Substituição em Índices Ímpares
# ============================================================
print("Digite os números separados por espaço:")
valores = input().split()
print("Digite a string de mesmo comprimento:")
texto = input()

n = len(valores)

resultado = []
for i in range(n):
    if i % 2 != 0:
        resultado.append(texto[i])
    else:
        resultado.append(valores[i])

print(" ".join(resultado))

# ============================================================
# EXERCÍCIO 7 — Moda e Mediana
# ============================================================

print("Digite a quantidade de valores:")
n = int(input())
print("Digite os", n, "valores:")
valores = input().split()
lista = [0] * n
i = 0
while i < n:
    lista[i] = int(valores[i])
    i = i + 1

    # Ordenar (Bubble Sort) para mediana
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp
        j = j + 1
    i = i + 1

    # Mediana
if n % 2 != 0:
    mediana = lista[n // 2]
else:
    mediana = (lista[n // 2 - 1] + lista[n // 2]) // 2

    # Moda
moda = lista[0]
max_freq = 0
i = 0
while i < n:
    freq = 0
    j = 0
    while j < n:
        if lista[j] == lista[i]:
            freq = freq + 1
        j = j + 1
    if freq > max_freq:
        max_freq = freq
        moda = lista[i]
    i = i + 1

if max_freq == 1:
    print("Moda: amodal")
else:
    print("Moda:", moda)

print("Mediana:", mediana)

# ============================================================
# EXERCÍCIO 8 — Soma das Posições Ímpares
# ============================================================

print("--- EXERCÍCIO 8: Soma das Posições Ímpares ---")
print("Digite os números separados por espaço:")
entrada = input()
partes = entrada.split()

n = 0
while True:
    try:
        _ = partes[n]
        n = n + 1
    except:
        break

lista = [0] * n
i = 0
while i < n:
    lista[i] = int(partes[i])
    i = i + 1

soma = 0
expressao = ""
i = 0
while i < n:
    if i % 2 != 0:
        soma = soma + lista[i]
        if expressao != "":
            expressao = expressao + "+"
        expressao = expressao + str(lista[i])
    i = i + 1

print(expressao, "=", soma)

# ============================================================
# EXERCÍCIO 9 — Ocorrência de Palavras
# ============================================================

print("--- EXERCÍCIO 9: Ocorrência de Palavras ---")
print("Digite o texto:")
texto = input()
partes = texto.split()

n = 0
while True:
    try:
        _ = partes[n]
        n = n + 1
    except:
        break

    # Limpar pontuação
palavras = [""] * n
i = 0
while i < n:
    palavra = ""
    j = 0
    while j < len(partes[i]):
        c = partes[i][j]
        if c != "." and c != "," and c != "!" and c != "?" and c != ";":
            palavra = palavra + c
        j = j + 1
    palavras[i] = palavra
    i = i + 1

    # Contar ocorrências únicas
palavras_unicas = [""] * n
contagens = [0] * n
qtd_unicas = 0

i = 0
while i < n:
    ja_existe = False
    j = 0
    while j < qtd_unicas:
        if palavras_unicas[j] == palavras[i]:
            ja_existe = True
        j = j + 1
    if not ja_existe:
        palavras_unicas[qtd_unicas] = palavras[i]
        cont = 0
        k = 0
        while k < n:
            if palavras[k] == palavras[i]:
                cont = cont + 1
            k = k + 1
        contagens[qtd_unicas] = cont
        qtd_unicas = qtd_unicas + 1
    i = i + 1

resultado = ""
i = 0
while i < qtd_unicas:
    resultado = resultado + palavras_unicas[i] + "=" + str(contagens[i])
    if i < qtd_unicas - 1:
        resultado = resultado + "; "
    i = i + 1

print(resultado)

# ============================================================
# EXERCÍCIO 10 — Matriz 3x3 e Valores Ímpares
# ============================================================
print("--- EXERCÍCIO 10: Matriz 3x3 - Valores Ímpares ---")
print("Digite 9 valores inteiros separados por espaço:")
valores = input().split()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
k = 0
i = 0
while i < 3:
    j = 0
    while j < 3:
        matriz[i][j] = int(valores[k])
        k = k + 1
        j = j + 1
    i = i + 1

qtd_impar = 0
i = 0
while i < 3:
    j = 0
    while j < 3:
        if matriz[i][j] % 2 != 0:
            qtd_impar = qtd_impar + 1
        j = j + 1
    i = i + 1

print("Matriz:")
i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 3:
        linha = linha + str(matriz[i][j])
        if j < 2:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

print("Quantidade de números ímpares:", qtd_impar)

# ============================================================
# EXERCÍCIO 11 — Soma por Linhas
# ============================================================
print("--- EXERCÍCIO 11: Soma por Linhas ---")
print("Digite as dimensões da matriz (m n):")
dims = input().split()
m = int(dims[0])
n = int(dims[1])
print("Digite os", m * n, "valores:")
valores = input().split()

matriz = [[0] * n for _ in range(m)]
k = 0
i = 0
while i < m:
    j = 0
    while j < n:
        matriz[i][j] = int(valores[k])
        k = k + 1
        j = j + 1
    i = i + 1

i = 0
while i < m:
    linha = ""
    soma = 0
    j = 0
    while j < n:
        linha = linha + str(matriz[i][j])
        soma = soma + matriz[i][j]
        if j < n - 1:
            linha = linha + " "
        j = j + 1
    print(linha, "=", soma)
    i = i + 1

# ============================================================
# EXERCÍCIO 12 — Soma por Colunas
# ============================================================
print("--- EXERCÍCIO 12: Soma por Colunas ---")
print("Digite as dimensões da matriz (m n):")
dims = input().split()
m = int(dims[0])
n = int(dims[1])
print("Digite os", m * n, "valores:")
valores = input().split()

matriz = [[0] * n for _ in range(m)]
k = 0
i = 0
while i < m:
    j = 0
    while j < n:
        matriz[i][j] = int(valores[k])
        k = k + 1
        j = j + 1
    i = i + 1

    # Imprimir matriz
i = 0
while i < m:
    linha = ""
    j = 0
    while j < n:
        linha = linha + str(matriz[i][j])
        if j < n - 1:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

    # Soma por colunas
j = 0
while j < n:
    soma = 0
    i = 0
    while i < m:
        soma = soma + matriz[i][j]
        i = i + 1
    print("Coluna" + str(j + 1) + ": " + str(soma))
    j = j + 1

# ============================================================
# EXERCÍCIO 13 — Matriz de Maiores Valores
# ============================================================
print("--- EXERCÍCIO 13: Matriz de Maiores Valores ---")
print("Digite 3 linhas, cada uma com 6 valores (3 da matriz A + 3 da matriz B):")

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

i = 0
while i < 3:
    valores = input().split()
    j = 0
    while j < 3:
        A[i][j] = int(valores[j])
        B[i][j] = int(valores[j + 3])
        j = j + 1
    i = i + 1

    # Maior valor por posição
i = 0
while i < 3:
    j = 0
    while j < 3:
        if A[i][j] > B[i][j]:
            C[i][j] = A[i][j]
        else:
            C[i][j] = B[i][j]
        j = j + 1
    i = i + 1

i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 3:
        linha = linha + str(C[i][j])
        if j < 2:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

# ============================================================
# EXERCÍCIO 14 — Soma Linha Ímpar e Coluna Par (4x4)
# ============================================================
print("--- EXERCÍCIO 14: Soma Linha Ímpar e Coluna Par ---")
print("Digite 4 linhas, cada uma com 4 valores:")

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

i = 0
while i < 4:
    valores = input().split()
    j = 0
    while j < 4:
        matriz[i][j] = int(valores[j])
        j = j + 1
    i = i + 1

soma = 0
expressao = ""
i = 0
while i < 4:
    j = 0
    while j < 4:
        if i % 2 != 0 and j % 2 != 0:
            soma = soma + matriz[i][j]
            if expressao != "":
                expressao = expressao + " + "
            expressao = expressao + str(matriz[i][j])
        j = j + 1
    i = i + 1

print("Resultado:")
print(expressao, "=", soma)

# ============================================================
# EXERCÍCIO 15 — Matriz Aleatória — Menor e Maior
# ============================================================
print("--- EXERCÍCIO 15: Matriz Aleatória - Menor e Maior ---")
print("Digite as dimensões (m n), de 2 a 10:")
dims = input().split()
m = int(dims[0])
n = int(dims[1])

if m < 2:
    m = 2
elif m > 10:
    m = 10
if n < 2:
    n = 2
elif n > 10:
    n = 10

matriz = [[0] * n for _ in range(m)]
i = 0
while i < m:
    j = 0
    while j < n:
        matriz[i][j] = 100 + (i * n + j)
        j = j + 1
    i = i + 1

    # Imprimir
i = 0
while i < m:
    linha = ""
    j = 0
    while j < n:
        linha = linha + str(matriz[i][j])
        if j < n - 1:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

menor = matriz[0][0]
maior = matriz[0][0]
pos_menor_i = 0
pos_menor_j = 0
pos_maior_i = 0
pos_maior_j = 0

i = 0
while i < m:
    j = 0
    while j < n:
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor_i = i
            pos_menor_j = j
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior_i = i
            pos_maior_j = j
        j = j + 1
    i = i + 1

print("Menor valor:", menor, "(" + str(pos_menor_i) + ",", str(pos_menor_j) + ")")
print("Maior valor:", maior, "(" + str(pos_maior_i) + ",", str(pos_maior_j) + ")")

# ============================================================
# EXERCÍCIO 16 — Produto Matricial 3x3
# ============================================================
print("--- EXERCÍCIO 16: Produto Matricial 3x3 ---")
print("Digite 9 valores para a matriz A:")
vals_a = input().split()
print("Digite 9 valores para a matriz B:")
vals_b = input().split()

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

k = 0
i = 0
while i < 3:
    j = 0
    while j < 3:
        A[i][j] = int(vals_a[k])
        B[i][j] = int(vals_b[k])
        k = k + 1
        j = j + 1
    i = i + 1

    # Produto C = A * B
i = 0
while i < 3:
    j = 0
    while j < 3:
        soma = 0
        k = 0
        while k < 3:
            soma = soma + A[i][k] * B[k][j]
            k = k + 1
        C[i][j] = soma
        j = j + 1
    i = i + 1

print("Matriz A:")
i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 3:
        linha = linha + str(A[i][j])
        if j < 2:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

print("Matriz B:")
i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 3:
        linha = linha + str(B[i][j])
        if j < 2:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

print("Matriz Resultante:")
i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 3:
        linha = linha + str(C[i][j])
        if j < 2:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

# ============================================================
# EXERCÍCIO 17 — Produto Matricial j×k · m×n
# ============================================================
print("--- EXERCÍCIO 17: Produto Matricial j×k · m×n ---")
print("Dimensões da Matriz A (j k):")
dims_a = input().split()
j = int(dims_a[0])
k = int(dims_a[1])

print("Dimensões da Matriz B (m n):")
dims_b = input().split()
m_b = int(dims_b[0])
n_b = int(dims_b[1])

print("Digite os", j * k, "valores da Matriz A:")
valores_a = input().split()

    # Ler Matriz A
A = [[0] * k for _ in range(j)]
p = 0
i = 0
while i < j:
    c = 0
    while c < k:
        A[i][c] = int(valores_a[p])
        p = p + 1
        c = c + 1
    i = i + 1

print("Digite os", m_b * n_b, "valores da Matriz B:")
valores_b = input().split()

    # Ler Matriz B
B = [[0] * n_b for _ in range(m_b)]
p = 0
i = 0
while i < m_b:
    c = 0
    while c < n_b:
        B[i][c] = int(valores_b[p])
        p = p + 1
        c = c + 1
    i = i + 1

print("Matriz A:")
i = 0
while i < j:
    linha = ""
    c = 0
    while c < k:
        linha = linha + str(A[i][c])
        if c < k - 1:
            linha = linha + " "
        c = c + 1
    print(linha)
    i = i + 1

print("Matriz B:")
i = 0
while i < m_b:
    linha = ""
    c = 0
    while c < n_b:
        linha = linha + str(B[i][c])
        if c < n_b - 1:
            linha = linha + " "
        c = c + 1
    print(linha)
    i = i + 1

if k != m_b:
    print("Impossível realizar o produto matricial!")
    print("Número de colunas de A (" + str(k) + ") != Número de linhas de B (" + str(m_b) + ")")
else:
    C = [[0] * n_b for _ in range(j)]
    i = 0
    while i < j:
        c = 0
        while c < n_b:
            soma = 0
            p = 0
            while p < k:
                soma = soma + A[i][p] * B[p][c]
                p = p + 1
            C[i][c] = soma
            c = c + 1
        i = i + 1

    print("Matriz Resultante:")
    i = 0
    while i < j:
        linha = ""
        c = 0
        while c < n_b:
            linha = linha + str(C[i][c])
            if c < n_b - 1:
                linha = linha + " "
            c = c + 1
        print(linha)
        i = i + 1

# ============================================================
# EXERCÍCIO 18 — Matriz 3x6 Análise Completa
# ============================================================
print("--- EXERCÍCIO 18: Matriz 3x6 - Análise Completa ---")
print("Digite 18 valores reais separados por espaço:")
valores = input().split()

matriz = [[0.0] * 6 for _ in range(3)]
original = [[0.0] * 6 for _ in range(3)]

k = 0
i = 0
while i < 3:
    j = 0
    while j < 6:
        matriz[i][j] = float(valores[k])
        original[i][j] = matriz[i][j]
        k = k + 1
        j = j + 1
    i = i + 1

    # Soma das colunas ímpares (colunas 1, 3, 5 → índices 0, 2, 4)
soma_col_impar = 0.0
j = 0
while j < 6:
    if j % 2 == 0:
        i = 0
        while i < 3:
            soma_col_impar = soma_col_impar + matriz[i][j]
            i = i + 1
    j = j + 1

print("Soma das colunas ímpares:", soma_col_impar)

    # Média das colunas 2 e 4 (índices 1 e 3)
soma_col2 = 0.0
soma_col4 = 0.0
i = 0
while i < 3:
    soma_col2 = soma_col2 + matriz[i][1]
    soma_col4 = soma_col4 + matriz[i][3]
    i = i + 1

media_col2 = soma_col2 / 3
media_col4 = soma_col4 / 3
print("Média da coluna 2:", media_col2)
print("Média da coluna 4:", media_col4)

    # Substituir coluna 6 (índice 5) pela soma das colunas 4 e 5 (índices 3 e 4)
i = 0
while i < 3:
    matriz[i][5] = matriz[i][3] + matriz[i][4]
    i = i + 1

print("\nMatriz Original:")
i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 6:
        linha = linha + str(original[i][j])
        if j < 5:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1

print("\nMatriz Modificada:")
i = 0
while i < 3:
    linha = ""
    j = 0
    while j < 6:
        linha = linha + str(matriz[i][j])
        if j < 5:
            linha = linha + " "
        j = j + 1
    print(linha)
    i = i + 1
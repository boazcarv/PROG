# ============================================================
# Lista 05 - Coleções: Tuplas, Conjuntos e Dicionários
# Disciplina: Introdução à Lógica e Programação
# Professor: Higor Morais
# OBS: Nenhuma função definida pelo usuário foi utilizada.
# ============================================================


# ======================= TUPLAS =============================
# Tuplas são coleções ORDENADAS e IMUTÁVEIS (não podem ser alteradas).
# Usam parênteses: (1, 2, 3)
# Acesso por índice: tupla[0], tupla[1], etc.
# ============================================================


# Questão 1 - Criação e acesso a tupla
# O programa cria uma tupla com dados pessoais (nome, idade, estado)
# e depois acessa cada elemento individualmente pelo índice.

nome = input()       # le o nome digitado pelo usuário
idade = input()      # le a idade digitada pelo usuário
estado = input()     # le o estado (UF) digitado pelo usuário

# cria uma tupla com os três valores lidos
# tuplas são imutáveis e usam parênteses ()
dados = (nome, idade, estado)

# acessa cada elemento da tupla pelo seu índice (começa em 0)
# dados[0] = nome, dados[1] = idade, dados[2] = estado
print(f"Nome: {dados[0]}")    # imprime o nome (posição 0 da tupla)
print(f"Idade: {dados[1]}")   # imprime a idade (posição 1 da tupla)
print(f"Estado: {dados[2]}")  # imprime o estado (posição 2 da tupla)


# Questão 2 - Desempacotamento: distância entre dois pontos
# O programa recebe 4 valores inteiros (x1, y1, x2, y2) que formam
# dois pontos no plano cartesiano. Usa desempacotamento de tupla
# para separar as coordenadas e calcula a distância euclidiana.

entrada1 = input().split()  # le a linha "Ponto 1" e separa por espaço → ['1', '3']
entrada2 = input().split()  # le a linha "Ponto 2" e separa por espaço → ['1', '8']

# desempacota os valores convertendo para inteiro
# cada par forma as coordenadas de um ponto
x1, y1 = int(entrada1[0]), int(entrada1[1])  # x1=1, y1=3
x2, y2 = int(entrada2[0]), int(entrada2[1])  # x2=1, y2=8

# cria tuplas representando os pontos no plano cartesiano
ponto1 = (x1, y1)  # tupla com as coordenadas do ponto 1
ponto2 = (x2, y2)  # tupla com as coordenadas do ponto 2

# calcula a distância euclidiana: d = √((x2-x1)² + (y2-y1)²)
# acessa as coordenadas via índice da tupla
distancia = ((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2) ** 0.5

# se a distância for um número inteiro (ex: 5.0), imprime sem decimais
# caso contrário, imprime com 2 casas decimais (ex: 7.07)
if distancia == int(distancia):
    print(f"Distância: {int(distancia)}")   # ex: "distância: 5"
else:
    print(f"Distância: {distancia:.2f}")    # ex: "distância: 7.07"


# Questão 3 - Concatenação de tuplas
# O programa lê duas listas de itens (frutas e vegetais) no formato
# texto (ex: "Uva, banana e maçã"), transforma cada uma em tupla
# e depois concatena as duas em uma única tupla.

frutas_input = input()    # le a linha de frutas: ex: "Uva, banana e maçã"
vegetais_input = input()  # le a linha de vegetais: ex: "Cenoura e batata"

# Transforma " e " em ", " para padronizar o separador
# Depois divide a string pela vírgula, gerando uma lista de palavras
frutas_str = frutas_input.replace(' e ', ', ').split(', ')  # ['Uva', 'banana', 'maçã']

# Converte cada palavra para minúsculo e cria uma tupla
frutas = tuple(f.lower() for f in frutas_str)  # ('uva', 'banana', 'maçã')

# Mesmo processo para os vegetais
vegetais_str = vegetais_input.replace(' e ', ', ').split(', ')  # ['Cenoura', 'batata']
vegetais = tuple(v.lower() for v in vegetais_str)  # ('cenoura', 'batata')

# Concatena as duas tuplas com o operador +
# O resultado é uma nova tupla com todos os elementos
alimentos = frutas + vegetais  # ('uva', 'banana', 'maçã', 'cenoura', 'batata')

print("Alimentos:")
print(alimentos)  # Imprime a tupla concatenada


# Questão 4 - Conversão de Lista para Tupla com slice
# O programa recebe uma lista de números, converte para tupla,
# depois usa slice (fatiamento) para pegar os 3 primeiros elementos.

lista_input = input()  # Lê a lista no formato: [1,2,3,4,5]

# eval() converte a string de entrada em um objeto Python real
# "[1,2,3,4,5]" vira a lista [1, 2, 3, 4, 5]
lista = eval(lista_input)

# converte a lista para tupla usando tuple()
# listas são mutáveis [], tuplas são imutáveis ()
tupla = tuple(lista)  # (1, 2, 3, 4, 5)

# usa slice (fatiamento) para obter os 3 primeiros elementos
# sintaxe: tupla[início:fim] — o índice 'fim' é exclusivo
# [:3] significa "do início até o índice 3 (não incluso)"
slice_tupla = tupla[:3]  # (1, 2, 3)

print(f"Tupla: {tupla}")          # imprime a tupla completa
print(f"Slice da tupla: {slice_tupla}")  # imprime os 3 primeiros elementos


# Questão 5 - Troca de posições em tuplas
# como tuplas são imutáveis, não podemos alterar seus elementos diretamente.
# a estratégia é: tupla → lista (mutável) → troca → tupla novamente.

tupla_input = input()  # le a tupla no formato: (1,2,3,4,5)
pos1 = int(input())    # le a primeira posição a ser trocada
pos2 = int(input())    # le a segunda posição a ser trocada

# converte a string de entrada em uma tupla Python
tupla = eval(tupla_input)  # (1, 2, 3, 4, 5)

# converte a tupla para lista para poder modificar os elementos
# tuplas NÃO permitem atribuição por índice (tupla[0] = x dá erro)
lista = list(tupla)  # [1, 2, 3, 4, 5]

# troca os valores das duas posições usando atribuição múltipla do Python
# ex: pos1=2, pos2=4 → troca lista[2] com lista[4]
# antes: [1, 2, 3, 4, 5] → Depois: [1, 2, 5, 4, 3]
lista[pos1], lista[pos2] = lista[pos2], lista[pos1]

# converte a lista de volta para tupla
nova_tupla = tuple(lista)  # (1, 2, 5, 4, 3)

print(f"Tupla A: {tupla}")      # imprime a tupla original (inalterada)
print(f"Tupla B: {nova_tupla}")  # imprime a tupla com as posições trocadas


# ===================== CONJUNTOS ============================
# Conjuntos são coleções NÃO ORDENADAS de elementos ÚNICOS (sem duplicatas).
# Usam chaves: {1, 2, 3}
# Suportam operações matemáticas: união, interseção, diferença.
# ============================================================


# Questão 6 - Criação de conjuntos a partir de listas
# O programa recebe uma lista com duplicatas, converte para conjunto
# (que elimina duplicatas automaticamente), depois adiciona o dobro do maior valor do conjunto.

lista_input = input()  # le a lista: ex: [1, 1, 2, 3, 3, 4, 4]

# converte a string em uma lista Python
lista = eval(lista_input)  # [1, 1, 2, 3, 3, 4, 4]

# converte a lista para conjunto com set()
# conjuntos NÃO aceitam elementos duplicados, então eles são removidos
conj = set(lista)  # {1, 2, 3, 4} — duplicatas eliminadas

# encontra o maior valor do conjunto com max()
maior = max(conj)  # 4

# add ao conjunto o dobro do maior valor
# conj.add() insere um novo elemento no conjunto
conj.add(maior * 2)  # Adiciona 8 → {1, 2, 3, 4, 8}

print(f"Lista: {lista}")  # imprime a lista original (com duplicatas)
print(f"Conj: {conj}")    # imprime o conjunto final (sem duplicatas + dobro do maior)


# Questão 7 - União e diferença de conjuntos
# O programa lê 3 conjuntos (A, B, C) e calcula:
# - União: A ∪ B (todos os elementos de A e B, sem repetir)
# - Diferença: (A ∪ B) - C (elementos da união que NÃO estão em C)

a_input = input()  # Lê os valores de A: ex: "1,2,3,4"
b_input = input()  # Lê os valores de B: ex: "2,5,7,9"
c_input = input()  # Lê os valores de C: ex: "1,4,7,6"

# Separa a string por vírgula e converte cada parte para inteiro
# Depois cria um conjunto com esses valores
A = set(int(x) for x in a_input.split(','))  # {1, 2, 3, 4}
B = set(int(x) for x in b_input.split(','))  # {2, 5, 7, 9}
C = set(int(x) for x in c_input.split(','))  # {1, 4, 7, 6}

# union() retorna um novo conjunto com todos os elementos de A e B
# Equivalente a: A | B
uniao = A.union(B)  # {1, 2, 3, 4, 5, 7, 9}

# difference() retorna os elementos que estão na união mas NÃO em C
# Equivalente a: uniao - C
diferenca = uniao.difference(C)  # {2, 3, 5, 9}  (removeu 1, 4, 7)

print(f"União: {uniao}")       # Imprime o resultado da união A ∪ B
print(f"Diferença: {diferenca}")  # Imprime o resultado de (A ∪ B) - C


# Questão 8 - Remoção Condicional em Conjuntos
# O programa recebe uma sequência de inteiros e um divisor.
# Cria um conjunto com os valores e outro contendo apenas
# os números que são divisíveis pelo divisor informado.

valores_input = input()  # Lê os valores: ex: "1, 9, 3, 2, 3, 6, 4"
divisor = int(input())   # Lê o divisor: ex: 3

# Separa a string por vírgula, remove espaços extras e converte para int
valores = [int(x.strip()) for x in valores_input.split(',')]  # [1, 9, 3, 2, 3, 6, 4]

# Cria um conjunto a partir da lista — duplicatas são removidas
conj1 = set(valores)  # {1, 2, 3, 4, 6, 9}  (o 3 repetido foi eliminado)

# Cria um novo conjunto apenas com os números divisíveis pelo divisor
# x % divisor == 0 verifica se x é divisível (resto da divisão é zero)
conj2 = set(x for x in conj1 if x % divisor == 0)  # {9, 3, 6}

print(f"Conj 1: {conj1}")  # Imprime o conjunto original (sem duplicatas)
print(f"Conj 2: {conj2}")  # Imprime o conjunto filtrado (só divisíveis)


# Questão 9 - Operações em Conjuntos (subconjunto e diferença)
# O programa recebe dois conjuntos A e B (podem ter tipos mistos:
# int e str), verifica se B é subconjunto de A e cria um conjunto C
# com os elementos de A que NÃO estão em B.

a_input = input()  # Lê o conjunto A: ex: "{1, 'a', 8, '4'}"
b_input = input()  # Lê o conjunto B: ex: "{'4', 8}"

# eval() converte a string em um objeto set Python real
# Isso funciona pois a entrada já vem no formato de conjunto
A = eval(a_input)  # {1, 'a', 8, '4'}
B = eval(b_input)  # {'4', 8}

# issubset() verifica se TODOS os elementos de B estão em A
# Retorna True se B ⊆ A, False caso contrário
if B.issubset(A):
    print("B é subconjunto de A")      # Se B está contido em A
else:
    print("B não é subconjunto de A")  # Se B tem algum elemento fora de A

# difference() cria um novo conjunto com elementos de A que não estão em B
# Equivalente a: A - B
C = A.difference(B)  # Remove de A os elementos que também estão em B

print(f"A: {A}")  # Imprime o conjunto A original
print(f"B: {B}")  # Imprime o conjunto B original
print(f"C: {C}")  # Imprime o conjunto C = A - B


# Questão 10 - Presença de valores em Conjuntos
# O programa lê valores para um conjunto (usando o operador | para adicionar)
# e valores para uma lista. Depois verifica quais itens da lista
# estão presentes no conjunto. A entrada termina quando o usuário digita '$$'.

conjunto = set()  # Inicializa um conjunto vazio

# Loop para ler valores do conjunto até o usuário digitar '$$'
while True:
    valor = input()       # Lê um valor
    if valor == '$$':     # Verifica se é o marcador de fim
        break             # Sai do loop
    # Adiciona o valor ao conjunto usando o operador | (união)
    # {valor} cria um conjunto temporário com um único elemento
    # conjunto | {valor} retorna a união (conjunto + novo elemento)
    conjunto = conjunto | {valor}

lista = []  # Inicializa uma lista vazia

# Loop para ler valores da lista até o usuário digitar '$$'
while True:
    valor = input()       # Lê um valor
    if valor == '$$':     # Verifica se é o marcador de fim
        break             # Sai do loop
    lista.append(valor)   # Adiciona o valor ao final da lista

# Imprime o conjunto formado
print(f"Conjunto: {conjunto}")

# Para cada valor na lista, verifica se está no conjunto
# join() junta os resultados com ", " entre eles
# "v in conjunto" retorna True se v existe no conjunto, False caso contrário
# Usa operador ternário: "Sim" se presente, "Não" se ausente
resultado = ", ".join(f"{v}:Sim" if v in conjunto else f"{v}:Não" for v in lista)
print(f"Lista: {resultado}")  # Ex: "1:Sim, 4:Não, 7:Sim"


# ==================== DICIONÁRIOS ===========================
# Dicionários são coleções de pares CHAVE:VALOR.
# Usam chaves: {'nome': 'Ana', 'idade': 20}
# Chaves são únicas; valores podem ser qualquer tipo.
# Acesso por chave: dicionario['nome'] → 'Ana'
# ============================================================


# Questão 11 - Contagem de palavras em dicionário
# O programa recebe um texto com várias palavras, remove pontuação,
# normaliza para minúsculas e conta quantas vezes cada palavra aparece.
# O resultado é armazenado em um dicionário {palavra: contagem}.

import string  # Módulo com constantes de pontuação (.,;:!?"' etc.)

texto = []  # Lista para armazenar todas as linhas do texto

# Lê todas as linhas até o fim da entrada (EOF)
# EOF (End Of File) ocorre quando não há mais dados para ler
while True:
    try:
        linha = input()       # Tenta ler uma linha
        texto.append(linha)   # Adiciona à lista de linhas
    except EOFError:          # Quando não houver mais entrada
        break                 # Sai do loop

# Junta todas as linhas em uma única string, separadas por espaço
texto_completo = " ".join(texto)

# Remove TODOS os sinais de pontuação do texto
# Percorre cada caractere de pontuação (.,;:!?) e substitui por ""
for pontuacao in string.punctuation:
    texto_completo = texto_completo.replace(pontuacao, "")

# Converte todo o texto para minúsculas e separa em palavras
# .lower() garante que "Lorem" e "lorem" sejam tratadas como iguais
# .split() divide a string por espaços, gerando uma lista de palavras
palavras = texto_completo.lower().split()

contagem = {}  # Dicionário vazio para armazenar {palavra: número_de_vezes}

# Percorre cada palavra do texto
for palavra in palavras:
    if palavra in contagem:       # Se a palavra já existe no dicionário
        contagem[palavra] += 1    # Incrementa a contagem
    else:                         # Se é a primeira ocorrência
        contagem[palavra] = 1     # Inicializa com 1

print("Contagem de palavras:")
print(contagem)  # Imprime o dicionário: {'lorem': 2, 'ipsum': 1, ...}


# Questão 12 - Agrupamento de tuplas por nome e soma de valores
# O programa recebe uma lista de tuplas (fruta, quantidade) e
# agrupa as quantidades por nome de fruta, somando os valores.
# O resultado é um dicionário {fruta: soma_total}.

itens_input = input()  # Lê a lista de tuplas: ex: [('banana', 3), ('uva', 5), ...]

# eval() converte a string em uma lista de tuplas Python
itens = eval(itens_input)  # [('banana', 3), ('uva', 5), ('uva', 2), ('banana', 2), ('pêra', 2)]

valores = {}  # Dicionário vazio para acumular as somas por fruta

# Percorre cada tupla da lista, desempacotando nome e valor
for nome, valor in itens:
    if nome in valores:          # Se a fruta já existe no dicionário
        valores[nome] += valor   # Soma o novo valor ao existente
    else:                        # Se é a primeira vez que a fruta aparece
        valores[nome] = valor    # Cria a entrada com o valor inicial

# Exemplo: banana aparece com 3 e depois com 2 → banana: 5
#          uva aparece com 5 e depois com 2 → uva: 7

print(f"Lista: {itens}")  # Imprime a lista original de tuplas
print("Valores:")
print(valores)  # Imprime o dicionário com as somas: {'banana': 5, 'uva': 7, 'pêra': 2}


# Questão 13 - Inversão de dicionário (nota → aluno)
# O programa recebe um dicionário {aluno: nota} e inverte para {nota: aluno}.
# Quando dois ou mais alunos têm a mesma nota, o valor vira uma LISTA
# com todos os nomes dos alunos que tiraram aquela nota.

aluno_nota_input = input()  # Lê o dicionário: ex: {'Ana':70, 'José':80, 'João':20, 'Rita':20}

# eval() converte a string em um dicionário Python
aluno_nota = eval(aluno_nota_input)  # {'Ana': 70, 'José': 80, 'João': 20, 'Rita': 20}

nota_aluno = {}  # Dicionário vazio para o resultado invertido

# Percorre cada par chave-valor do dicionário original
# aluno = nome do aluno (chave), nota = nota do aluno (valor)
for aluno, nota in aluno_nota.items():
    if nota in nota_aluno:
        # Se a nota JÁ EXISTE como chave no novo dicionário,
        # significa que outro aluno já tirou essa nota
        if type(nota_aluno[nota]) == list:
            # Se o valor já é uma lista, basta adicionar o novo nome
            nota_aluno[nota].append(aluno)
        else:
            # Se o valor é uma string (1º aluno), transforma em lista
            # com os dois nomes: o que já estava + o novo
            nota_aluno[nota] = [nota_aluno[nota], aluno]
    else:
        # Primeira vez que a nota aparece — valor é apenas o nome (string)
        nota_aluno[nota] = aluno

# Resultado: {70: 'Ana', 80: 'José', 20: ['João', 'Rita']}
# Nota 20 tem dois alunos, então vira lista. As outras notas ficam como string.

print("nota_aluno:")
print(nota_aluno)


# Questão 14 - Combinação de estoque de duas lojas
# O programa recebe dois dicionários representando o estoque de
# duas lojas e cria um dicionário combinado, somando as quantidades
# dos itens que aparecem em ambas as lojas. Itens exclusivos de
# uma loja mantêm a quantidade original.

loja1_input = input()  # Lê o estoque da Loja 1: ex: {'Item 1':10, 'Item 2':5, 'Item 3':10}
loja2_input = input()  # Lê o estoque da Loja 2: ex: {'Item 1':10, 'Item 2':2, 'Item 4':10}

# Converte as strings em dicionários Python
loja1 = eval(loja1_input)  # {'Item 1': 10, 'Item 2': 5, 'Item 3': 10}
loja2 = eval(loja2_input)  # {'Item 1': 10, 'Item 2': 2, 'Item 4': 10}

estoque = {}  # Dicionário vazio para o estoque total combinado

# Primeiro: copia todos os itens da Loja 1 para o estoque
for item, qtd in loja1.items():
    estoque[item] = qtd  # Adiciona cada item com sua quantidade

# Depois: percorre os itens da Loja 2
for item, qtd in loja2.items():
    if item in estoque:
        # Se o item já existe no estoque (veio da Loja 1),
        # SOMA as quantidades das duas lojas
        estoque[item] += qtd  # Ex: Item 1 → 10 + 10 = 20
    else:
        # Se o item só existe na Loja 2, mantém a quantidade original
        estoque[item] = qtd   # Ex: Item 4 → 10

# Resultado: {'Item 1': 20, 'Item 2': 7, 'Item 3': 10, 'Item 4': 10}
# Item 1 e Item 2 apareceram em ambas → somados
# Item 3 só na Loja 1 → mantido
# Item 4 só na Loja 2 → mantido

print(f"Loja 1: {loja1}")    # Imprime o estoque da Loja 1
print(f"Loja 2: {loja2}")    # Imprime o estoque da Loja 2
print(f"Estoque: {estoque}") # Imprime o estoque combinado


# Questão 15 - Relatório de vendas por vendedor no trimestre
# O programa lê os nomes dos vendedores, depois solicita as vendas
# de cada um em 3 meses. Calcula o total de vendas, cria um
# dicionário {vendedor: total} e uma lista de tuplas ordenada
# pelo valor de vendas em ordem decrescente.

# Lê a lista de nomes dos vendedores separados por vírgula
vendedores_input = input()  # Ex: "Ana, José, Maria"

# Separa os nomes pela vírgula e remove espaços extras com strip()
vendedores = [v.strip() for v in vendedores_input.split(',')]  # ['Ana', 'José', 'Maria']

vendas = {}  # Dicionário vazio para armazenar {vendedor: total_vendas}

# Para cada vendedor, solicita as vendas dos 3 meses do trimestre
for vendedor in vendedores:
    mes1 = float(input(f"{vendedor} - Mês 1: "))  # Lê vendas do mês 1
    mes2 = float(input(f"{vendedor} - Mês 2: "))  # Lê vendas do mês 2
    mes3 = float(input(f"{vendedor} - Mês 3: "))  # Lê vendas do mês 3

    # Soma as vendas dos 3 meses e armazena no dicionário
    vendas[vendedor] = mes1 + mes2 + mes3

# Cria uma lista de tuplas (vendedor, total_vendas) a partir do dicionário
# vendas.items() retorna pares (chave, valor) do dicionário
# sorted() ordena a lista
# key=lambda x: x[1] define que a ordenação é pelo 2º elemento da tupla (total)
# reverse=True indica ordem DECRESCENTE (do maior para o menor)
lista_ordenada = sorted(vendas.items(), key=lambda x: x[1], reverse=True)

# Exibe o relatório completo
print(f"Relatório de vendas: {vendas}")  # Dicionário com totais por vendedor
print(f"Ranking: {lista_ordenada}")      # Lista ordenada do maior para o menor vendedor

ab = float(input("Distância A→B: "))
ac = float(input("Distância A→C: "))
bd = float(input("Distância B→D: "))
be = float(input("Distância B→E: "))
cf = float(input("Distância C→F: "))
cg = float(input("Distância C→G: "))

# calcula os 4 caminhos possiveis
dist_abd = ab + bd
dist_abe = ab + be
dist_acf = ac + cf
dist_acg = ac + cg

menor = dist_abd
caminho = "A → B → D"

if dist_abe < menor:
    menor = dist_abe
    caminho = "A → B → E"

if dist_acf < menor:
    menor = dist_acf
    caminho = "A → C → F"

if dist_acg < menor:
    menor = dist_acg
    caminho = "A → C → G"

print(f"Caminho percorrido: {caminho}")
print(f"Distância percorrida: {menor}")
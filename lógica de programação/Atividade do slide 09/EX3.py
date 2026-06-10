inicio = float(input("Digite o início do intervalo: "))
fim = float(input("Digite o fim do intervalo: "))
valor = float(input("Digite o terceiro valor: "))

if valor >= inicio and valor <= fim:
    print("O valor está DENTRO do intervalo.")
elif valor < inicio:
    print("O valor está FORA do intervalo (parte inferior).")
else:
    print("O valor está FORA do intervalo (parte superior).")
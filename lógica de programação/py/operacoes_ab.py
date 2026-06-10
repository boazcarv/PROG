A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


print(f"A + B --> {A + B}")
print(f"A * B --> {A * B}")
print(f"A - B --> {A - B}")

if B != 0:
    print(f"A / B --> {A / B}")
else:
    print("A / B --> não é possível (divisão por zero)")


print(f"A > B --> {A > B}")
print(f"A <= B --> {A <= B}")
print(f"A != B --> {A != B}")
print(f"A == B --> {A == B}")

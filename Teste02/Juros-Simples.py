C = float(input("Informe a capital inicial: "))
i = float(input("Informe a taxa de juros mensal: ")) /100
t = float(input("Informe quantos meses: "))

J = C * i * t
M = C + J

print(f"O valor do Juros é: {J}")
print(f"E o montante final é {M}")
# C = capital inicial
# i = taxa de juros
# t = tempo
# M = montante final
# J = valor dos juros


C = float(input("Informe a capital inicial: "))
i = float(input("Informe a taxa de juros mensal: ")) / 100
t = float(input("Informe quantos meses: "))

M = C * (1 + i) ** t
J = M - C

print(f"O valor do Montante Final é: {M:.2f}")
print(f"E o valor do Juros é {J:.2f}")
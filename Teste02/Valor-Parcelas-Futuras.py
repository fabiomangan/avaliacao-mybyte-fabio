# VP = valor presente
# VF = valor futuro
# i = taxa de juros
# t = tempo


VF = float(input("Informe o valor futuro da parcela: "))
i = float(input("Informe a taxa de juros mensal: ")) / 100
t = float(input("Informe quantos meses: "))

VP = VF / (1 + i) ** t

print(f"O valor presente da parcela é: {VP:.2f}")

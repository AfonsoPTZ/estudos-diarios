
alturas = []
idades = []
acima = []
for i in range(3):
    alt = float(input(f"Digite a altura do {i+1}º aluno: "))
    ida = int(input(f"Digit a idade do {i+1}º aluno: "))
    alturas.append(alt)
    idades.append(ida)
média = sum(alturas)/len(alturas)
for i, idad in enumerate(idades):
    if idad >= 13:
        if alturas[i] < média:
            acima.append(alturas[i])
print(len(acima))




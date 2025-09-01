acima = []
notas = []
for o in range(10):
    for i in range(4):
        n1 = float(input(f"Digite a {i+1}º nota do {o+1}ºaluno: "))
        nota1 = []
        nota1.append(n1)
    m1 = sum(nota1)/len(nota1)
    notas.append(m1)
for i in notas:
    if i >= 7:
        acima.append(i)
print(f"A quantidade de alunos acima ou igual á média é {len(acima)}.")
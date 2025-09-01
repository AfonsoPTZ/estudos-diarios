
notas = []
acima = []
abaixo = []
inversa = []
while True:
    nota = float(input("Digite uma nota: "))
    if nota == -1:
        break
    notas.append(nota)
print(f"Quantidade de valores lidos: {len(notas)}")
print(notas)

for i in reversed(notas):
    print(i)
print(f"Soma: {sum(notas)}")
print(f"Média: {sum(notas) / len(notas)}")
for i in notas:
    if i > sum(notas) / len(notas):
        acima.append(i)
print(f"Existem {len(acima)} valores acima da média")
for i in notas:
    if i < 7:
        abaixo.append(i)
print(f"Existem {len(abaixo)} valores abaixo de 7")
print("Programa encerrado")
idades = []
alturas = []
for i in range(5):
    n1 = int(input("digite sua idade: "))
    n2 = float(input("digite sua altura: "))
    idades.append(n1)
    alturas.append(n2)
idades.sort(reverse=True)
alturas.sort(reverse=True)
print(idades)
print(alturas)

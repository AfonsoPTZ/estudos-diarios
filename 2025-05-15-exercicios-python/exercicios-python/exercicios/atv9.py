potencia = []
list1 = []
soma = []
for i in range(3):
    n = int(input("Digite um numero: "))
    list1.append(n)
for n1 in list1:
    quadrados = n1**2
    potencia.append(quadrados)
soma = sum(potencia)
print(soma)
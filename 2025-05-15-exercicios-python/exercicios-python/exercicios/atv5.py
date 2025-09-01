par = []
impar = []
numeros = []
for i in range(20):
    n = int(input("Digite um numero:"))
    numeros.append(n)
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(par)
print(impar)
print(numeros)
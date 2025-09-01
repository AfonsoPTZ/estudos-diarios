# Faça um programa, com uma função que receba um número e retorne 'M' se for múltiplo de 3, e 'N' caso contrário.

def verifica_multiplo(numero):
    if numero % 3 == 0:
        return 'M'
    else:
        return 'N'

numero = 9
resultado = verifica_multiplo(numero)
print(f"O resultado para o número {numero} é: {resultado}")
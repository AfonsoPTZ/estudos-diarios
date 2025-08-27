# Faça um programa, com uma função que receba um número e retorne 'P' se for positivo, e 'N' se for zero ou negativo.

def verifica_numero(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'


numero = float(input("Digite um número: "))
resultado = verifica_numero(numero)
print(f"O resultado é: {resultado}")
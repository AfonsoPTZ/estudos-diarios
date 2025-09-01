# Faça um programa, com uma função que receba um número e retorne 'A' se for maior que 100, e 'B' caso contrário.

def verifica_numero(numero):
    if numero > 100:
        return 'A'
    else:
        return 'B'

resultado = verifica_numero(150)
print(resultado)  

resultado = verifica_numero(50)
print(resultado)  
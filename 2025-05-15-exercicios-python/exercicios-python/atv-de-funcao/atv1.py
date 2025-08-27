# Faça um programa, com uma função que receba um número inteiro e retorne 'P' se for par e 'I' se for ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'P'
    else:
        return 'I'

numero = int(input("Digite um número inteiro: "))
resultado = par_ou_impar(numero)
print(f"O número {numero} é {'par' if resultado == 'P' else 'ímpar'}.")
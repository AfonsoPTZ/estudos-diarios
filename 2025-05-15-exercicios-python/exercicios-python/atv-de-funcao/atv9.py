# Faça um programa, com uma função que receba um número e retorne 'P' se for primo, e 'N' caso contrário.

def eh_primo(numero):
    if numero <= 1:
        return 'N'
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return 'N'
    return 'P'


numero = 7  
resultado = eh_primo(numero)
print(f"O número {numero} é {'primo' if resultado == 'P' else 'não primo'}.")
# Faça um programa, com uma função que receba um caractere e retorne 'V' se for uma vogal, e 'C' se for uma consoante.

def verifica_caractere(caractere):
    vogais = "aeiouAEIOU"
    if caractere in vogais:
        return 'V'
    else:
        return 'C'


resultado = verifica_caractere('a')
print(resultado)  

resultado = verifica_caractere('b')
print(resultado)  
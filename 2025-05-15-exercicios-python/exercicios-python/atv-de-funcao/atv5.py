# Faça um programa, com uma função que receba a idade de uma pessoa e retorne 'M' se for maior de idade (18 anos ou mais), e 'm' se for menor de idade.

def verifica_idade(idade):
    if idade >= 18:
        return 'M'
    else:
        return 'm'
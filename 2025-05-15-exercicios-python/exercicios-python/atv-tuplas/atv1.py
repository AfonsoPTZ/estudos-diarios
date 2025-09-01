# Crie um programa que cadastre múltiplos usuários, solicitando CPF, RG e nome para cada um.
# Ao final, exiba todos os usuários cadastrados mostrando CPF, RG e nome de cada um.


users = []
while True:
    cpf = input("Digite seu CPF:")
    rg = input("Digite seu RG:")
    nome = input("Digite seu Nome:")
    pessoa = (cpf, rg, nome)
    users.append(pessoa)
    if input("Quer adicionar mais usuarios (s/n)").lower() == "n":
        break
for cpf, rg, nome in users:
    print(f"CPF: {cpf} ; RG: {rg} ; Nome: {nome}")
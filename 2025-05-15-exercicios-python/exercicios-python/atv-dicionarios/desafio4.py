# Crie um programa que cadastre usuários, solicitando CPF, nome e idade para cada um.
# Ao final, exiba a lista completa de usuários cadastrados.

users = []
while True:
    if input("Deseja add um usuario?").lower() == "n":
        break
    cpf = input("Digite o CPF: ")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    user = {
        "CPF" : cpf,
        "Nome" : nome,
        "idade" : idade
    }
    users.append(user)
print(users)
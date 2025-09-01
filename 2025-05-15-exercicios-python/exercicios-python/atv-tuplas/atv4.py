# Crie uma função que receba uma lista de usuários (cada um com CPF, nome e idade) e uma informação de busca (CPF ou nome).
# A função deve imprimir os dados do usuário correspondente se encontrado, ou exibir "Usuário não encontrado." caso contrário.


users = (
    {"cpf": "12345678901", "nome": "João", "idade": 30},
    {"cpf": "98765432100", "nome": "Maria", "idade": 25},
    {"cpf": "45678912345", "nome": "Pedro", "idade": 40},
)
info = input("Qual user você deseja buscar? ")
for user in users:
    if user["cpf"] == info or user["nome"] == info:
        print(user)
    else:
        print("Usuário não encontrado.")
        break
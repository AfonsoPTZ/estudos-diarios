# Crie um programa que cadastre funcionários, solicitando matrícula, nome e os nomes de um ou mais chefes para cada funcionário.
# Ao final, exiba todos os funcionários cadastrados, mostrando matrícula, nome e todos os chefes de cada um.


funcionarios = []
while True:
    matricula = input("Digite sua matricula: ")
    nome = input("Digite seu nome: ")
    dependentes = ()
    while True:
        chefes = input("Digite o nome do chefe: ")
        dependentes += (chefes,)
        if input("Deseja adicionar mais chefes (s/n)? ") == "n":
            break
    f1 = {
        "Nome": nome,
        "Matricula": matricula,
        "Chefes": ", ".join(dependentes)  # Converte a tupla em uma string separada por vírgulas
    }
    funcionarios.append(f1)
    if input("Deseja adicionar mais usuários (s/n)? ") == "n":
        break


for user in funcionarios:
    for key, value in user.items():
        print(f"{key}: {value}")
    print("-----------------------------")
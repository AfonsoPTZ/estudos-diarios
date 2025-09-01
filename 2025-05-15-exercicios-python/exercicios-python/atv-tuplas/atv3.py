# Criar um programa que efetua cadastro de produtos e preços. Caso o
# produto já existe, pergunta se o usuário pretende atualizar o valor.
# Imprimir o dicionário ao final do programa em formato de lista.
produtos = []
while True:
    p = input("Digite o produto: ")
    v = float(input("Digite o valor: "))
    produto = {
        p : v
    }
    for i in produtos:
        if p in i:
            if input("quer mudar o valor?") == "s":
                i[p] = v
                break
    else:
        produtos.append(produto)
    if input("deseja add mais produtos?") == "n":
        break
print(produtos)

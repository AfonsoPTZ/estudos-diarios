# Crie um programa que simule o sistema de pedidos de uma lanchonete.
# O programa deve exibir o cardápio, permitir que o usuário faça pedidos e verificar se há ingredientes suficientes no estoque para cada lanche.
# Se houver estoque, o pedido é realizado e os ingredientes são descontados; caso contrário, informe qual ingrediente está em falta.


estoque = {'pao': 1, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 1}
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
for key, valuers in cardapio.items():
        print(f"Lanche: {key} - Ingredientes: {", ".join(valuers)}")
        print("--------------------------------------------------------------------")
while True:
    pedido = input('Digite o lanche desejado.\nDigite "0" para encerrar: ').lower()
    if pedido == "0":
       break
    if pedido not in cardapio:
        print(f"{pedido} não esta no cardapio. Tente outro pedido")
    else:
        tem_estoque = True
        for ingrediente in cardapio[pedido]:
            if estoque[ingrediente] < 1:
                print(f"Desculpe, não temos {ingrediente} suficiente para fazer o pedido.")
                tem_estoque = False
        if tem_estoque:
            for ingrediente in cardapio[pedido]:
                estoque[ingrediente] -= 1
            print(f"Um {pedido} saindo no capricho!!!")
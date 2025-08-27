# Crie um programa que simule a síntese de compostos químicos a partir de um estoque de elementos.
# O programa deve solicitar o nome do composto desejado, verificar se a receita existe e descontar os elementos do estoque conforme a fórmula.
# Caso o composto não exista, informe ao usuário. Permita encerrar a simulação digitando "0".


estoque = {
    'hidrogenio': 5,
    'oxigenio': 4,
    'carbono': 3,
    'nitrogenio': 2,
    'enxofre': 2
}

receitas = {
    'agua': ['hidrogenio', 'hidrogenio', 'oxigenio'],
    'dioxido de carbono': ['carbono', 'oxigenio', 'oxigenio'],
    'amonia': ['nitrogenio', 'hidrogenio', 'hidrogenio', 'hidrogenio'],
    'acido sulfurico': ['hidrogenio', 'hidrogenio', 'enxofre', 'oxigenio', 'oxigenio', 'oxigenio', 'oxigenio']
}
composto = input("Qual composto deseja sintetizar? (digite 0 para sair)")
while True:
    if composto == "0":
        print("Encerrando simulação laboratorial...")
        break
    if composto not in receitas.keys():
            print("Composto desconhecido no banco de fórmulas!")
            break
    if composto in receitas.keys():
        for i in receitas[composto]:
             estoque[i] -= 1

        break

situaçao = []
print("""
Situações dos mouses:
1- necessita da esfera.
2- necessita de limpeza. 
3- necessita troca do cabo ou conector.
4- quebrado ou inutilizado.
Digite 0 para encerrar o programa
""")
while True:
    n = input(f"""
Qual a situação do {len(situaçao) + 1}° mouse?
""")
    if n == "0":
        break
    elif n in ["1", "2", "3", "4"]:
        situaçao.append(n)
    else:
        print("Digite uma situação válida (1, 2, 3, 4 ou 0).")
mouses = len(situaçao)
print(f"""
Quantidade de mouses: {mouses}
Situação                                        Quantidade                     Percentual
1- necessita da esfera.                         {situaçao.count("1")}                              {((situaçao.count("1") / mouses) * 100,)}%
2- necessita de limpeza.                        {situaçao.count("2")}                              {((situaçao.count("2") / mouses) * 100,)}%
3- necessita troca do cabo ou conector.         {situaçao.count("3")}                              {((situaçao.count("3") / mouses) * 100,)}%
4- quebrado ou inutilizado.                     {situaçao.count("4")}                              {((situaçao.count("4") / mouses) * 100,)}%
""")
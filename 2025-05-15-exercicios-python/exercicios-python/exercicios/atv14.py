Resposta = []
print("Responda as seguintes perguntas com ""'sim'"" ou ""'não'""!")
Resposta.append(input("a)Telefonou para a vítima?" ))
Resposta.append(input("b)Esteve no local do crime?" ))
Resposta.append(input("c)Mora perto da vítima?" ))
Resposta.append(input("d)Devia para a vítima?" ))
Resposta.append(input("e)Já trabalhou com a vítima?" ))
sim = Resposta.count("sim")
if sim == 5:
    print("Você é o assassino.")
elif 3 <= sim <= 4:
    print("Você é cúmplice.")
elif sim == 2:
    print("Você é suspeito.")
else:
    print("Você é inocente.")

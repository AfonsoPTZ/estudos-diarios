saltos = []
while True:
    atleta = input("Digite o nome do atleta(so e permitido letras e espaços): ")
    if atleta.replace(" ", "").isalpha():
        break
    else:
        print("Digite um nome válido")
saltos.append(float(input("Digite o primeiro salto do atleta: ")))
saltos.append(float(input("Digite o segundo salto do atleta: ")))
saltos.append(float(input("Digite o terceiro salto do atleta: ")))
saltos.append(float(input("Digite o quarto salto do atleta: ")))
saltos.append(float(input("Digite o quinto salto do atleta: ")))
print(f"Reseultado final do atleta {atleta}:")
print(f"Saltos: {saltos}")
print(f"Média: {sum(saltos)/len(saltos)}")

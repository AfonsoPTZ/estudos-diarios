carros = []
gasolina = []
for i in range(5):
    while True:
        carro = input(f"Digite o nome do {i+1}° carro (Só é permitido letras e espaços): ")
        if carro.replace(" ", "").isalpha():
            carros.append(carro)
            break
        else:
            print("Digite um nome válido")
for i in range(5):
    while True:
        try:
            consumo = float(input(f"Digite a quantidade de km por litro do {carros[i]}: "))
            if consumo > 0:
                gasolina.append(consumo)
                break
            else:
                print("O consumo deve ser maior que zero.")
        except ValueError:
            print("Digite um numero valido.")
print("A comparação entre os carros é:")
for i in range(5):
    litros = 1000 / gasolina[i]
    custo = litros * 2.25
    print(f"""
Veículo {i+1}
Nome: {carros[i]}
Km/l: {gasolina[i]}
Consumo em 1000 km: {litros:.2f} litros
Custo em 1000 km: R${custo:.2f}
""")
lugar = gasolina.index(max(gasolina))
print(f"O carro mais econômico é o {carros[lugar]}")


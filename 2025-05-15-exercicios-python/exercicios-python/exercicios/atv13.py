meses = ["Janeiro" , "Feveriro" , "Março"  ,"Abril" , "Maio" , "Junho" , "Julho" , "Agosto" , "Setembro" , "Outubro" , "Novembro" , "Dezembro"]
temperaturas = []
for mes in meses:
    n1 = float(input(f"Digite a temperatura média de {mes}: "))
    temperaturas.append(n1)
média = sum(temperaturas)/len(temperaturas)
for i, temp in enumerate(temperaturas):
    if temp > média:
        print(f"{meses[i]}: {temp}°C")
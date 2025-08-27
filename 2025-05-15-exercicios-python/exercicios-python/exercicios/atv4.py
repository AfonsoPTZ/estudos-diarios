list1 = []
consoante = []
for i in range(10):
    letra = (input("Digite uma letra: "))
    list1.append(letra)
for letra in list1:
    if letra not in ('aeiou'):
        consoante.append(letra)
print(f"Existem `{len(consoante)} consoantes e elas são: {consoante}")


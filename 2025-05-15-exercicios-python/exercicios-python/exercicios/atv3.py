list1 = []
for i in range(4):
    n = int(input("Digite a nota: "))
    list1.append(n)
media = sum(list1)/len(list1)
print(media)
list1 = []
list2 = []
list3 = []
for i in range(10):
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    list1.append(n1)
    list2.append((n2))
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)

list1 = []
list2 = []
list3 = []
list4 = []
for i in range(10):
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))
    list1.append(n1)
    list2.append(n2)
    list3.append(n3)
for i in range(len(list1)):
    list4.append(list1[i])
    list4.append(list2[i])
    list4.append(list3[i])
print(list4)
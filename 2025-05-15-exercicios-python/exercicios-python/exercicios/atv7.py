list1 = []
for i in range(5):
    n = int(input("digite um numero:"))
    list1.append(n)
soma = sum(list1)
multi = 1
for i in list1:
    multi *= i
print(soma)
print(multi)
print(list1)
# Faça um programa, com uma função que receba um número e retorne 'F' se for um número de Fibonacci, e 'N' caso contrário.

def verifica_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return 'F' if b == n or n == 0 else 'N'


numero = 8  
resultado = verifica_fibonacci(numero)
print(f"O número {numero} é da sequência de Fibonacci? {resultado}")
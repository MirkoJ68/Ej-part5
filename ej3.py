a = 0
b = 1
n = int(input("Ingresa un numero entero positivo: "))

for i in range(n):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente

print("Secuencia Fibonacci:")
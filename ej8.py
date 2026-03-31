import random

longitud = int(input("Ingresa la longitud: "))
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
password = ""

for i in range(longitud):
    password += random.choice(caracteres)

print("Contraseña:", password)
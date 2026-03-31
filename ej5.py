import random

numero_secreto = random.randint(1, 100)

intentos = 0
adivinanza = 0

print("Adivina el número entre 1 y 100")

while adivinanza != numero_secreto:
    adivinanza = int(input("Ingresa tu número: "))
    intentos += 1

    if adivinanza < numero_secreto:
        print("Muy bajo")
    elif adivinanza > numero_secreto:
        print("Muy alto")
    else:
        print("Ese")
        print(f"Le pegaste en {intentos} intentos")
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura * altura)

print("Tu IMC es:", imc)

if imc < 18.5:
    print("Talla S")
elif imc < 20:
    print("Talla M")
elif imc < 22:
    print("Talla L")
elif imc < 25:
    print("Talla XL")
elif imc < 28:
    print("Talla 2XL")

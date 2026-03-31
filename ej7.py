precio = float(input("Ingresa el precio original: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

final = precio - (precio * (descuento / 100))

print(f"Precio final: {final}")
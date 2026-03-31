password = input("Crea una contraseña: ")

hay_mayuscula = False
hay_minuscula = False
hay_numero = False
hay_especial = False

especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

for c in password:
    if c.isupper():
        tiene_mayuscula = True
    elif c.islower():
        tiene_minuscula = True
    elif c.isdigit():
        tiene_numero = True
    elif c in especiales:
        tiene_especial = True

if (len(password) >= 8 and hay_mayuscula and 
    hay_minuscula and hay_numero and hay_especial):
    print("Contraseña válida")
else:
    print("Contraseña inválida")
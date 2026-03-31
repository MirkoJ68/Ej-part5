tareas = []

while True:
    print("\n1. Agregar")
    print("2. Ver")
    print("3. Completar")
    print("4. Eliminar")
    print("5. Salir")

    op = input("Opción: ")

    if op == "1":
        desc = input("Tarea: ")
        fecha = input("Fecha: ")
        tareas.append([desc, fecha, False])

    elif op == "2":
        for i in range(len(tareas)):
            estado = "Terminada" if tareas[i][2] else "Pendiente"
            print(i, "-", tareas[i][0], tareas[i][1], estado)

    elif op == "3":
        num = int(input("Número: "))
        if num < len(tareas):
            tareas[num][2] = True

    elif op == "4":
        num = int(input("Número: "))
        if num < len(tareas):
            tareas.pop(num)

    elif op == "5":
        break
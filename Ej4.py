acciones = []
deshechas = []

def nueva_accion():
    accion = input("Escribe una acción (escribir, borrar, copiar, pegar, etc.): ")
    acciones.append(accion)
    deshechas.clear()
    print("Acción guardada.\n")

def deshacer():
    if acciones:
        accion = acciones.pop()
        deshechas.append(accion)
        print(f"Deshacer: {accion}\n")
    else:
        print("No hay acciones para deshacer.\n")

def rehacer():
    if deshechas:
        accion = deshechas.pop()
        acciones.append(accion)
        print(f"Rehacer: {accion}\n")
    else:
        print("No hay acciones para rehacer.\n")

def mostrar_historial():
    print("\nHistorial de acciones:")
    for i, a in enumerate(acciones, 1):
        print(f"{i}. {a}")
    print()

while True:
    print("1. Nueva acción")
    print("2. Deshacer")
    print("3. Rehacer")
    print("4. Ver historial")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nueva_accion()
    elif opcion == "2":
        deshacer()
    elif opcion == "3":
        rehacer()
    elif opcion == "4":
        mostrar_historial()
    elif opcion == "5":
        print("Saliendo del editor.")
        break
    else:
        print("Opción no válida.\n")

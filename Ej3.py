pacientes = []

def agregar_paciente():
    nombre = input("Nombre completo: ")
    edad = int(input("Edad: "))
    sintoma = input("Síntoma principal: ")
    prioridad = int(input("Prioridad (1 a 5): "))
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "sintoma": sintoma,
        "prioridad": prioridad
    }
    pacientes.append(paciente)
    print("Paciente agregado.\n")

def mostrar_pacientes():
    if not pacientes:
        print("No hay pacientes en la lista.\n")
    else:
        print("\nLista de pacientes en orden de llegada:")
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. {p['nombre']} - Edad: {p['edad']} - Síntoma: {p['sintoma']} - Prioridad: {p['prioridad']}")
        print()

def atender_paciente():
    if not pacientes:
        print("No hay pacientes para atender.\n")
    else:
        paciente = pacientes.pop(0)
        print(f"Paciente atendido: {paciente['nombre']}\n")

while True:
    print("1. Agregar paciente")
    print("2. Mostrar pacientes")
    print("3. Atender siguiente paciente")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        mostrar_pacientes()
    elif opcion == "3":
        atender_paciente()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida.\n")

def ingresar_estudiantes(estudiantes):
    while True:
        print("\nIngresando nuevo estudiante:")
        estudiante = {
            "carnet": input("Carnet: "),
            "nombres": input("Nombres: "),
            "apellidos": input("Apellidos: "),
            "peso": float(input("Peso (kg): ")),
            "estatura en metros": float(input("Estatura en metros: ")),
            "sexo": input("Sexo (M/F): "),
            "promedio académico": float(input("Promedio académico: "))
        }
        estudiantes.append(estudiante)
        
        continuar = input("\n¿Deseas ingresar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            break


def mostrar_estudiantes(estudiantes):
    for est in estudiantes:
        print(est)


def calcular_promedios_generales(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    suma_peso = sum(e["peso"] for e in estudiantes)
    suma_estatura = sum(e["estatura en metros"] for e in estudiantes)
    suma_promedio = sum(e["promedio académico"] for e in estudiantes)
    cantidad = len(estudiantes)

    promedio_peso = suma_peso / cantidad
    promedio_estatura = suma_estatura / cantidad
    promedio_academico = suma_promedio / cantidad

    print("\nPromedios generales del grupo:")
    print(f"Peso promedio: {promedio_peso:.2f} kg")
    print(f"Estatura promedio: {promedio_estatura:.2f} m")
    print(f"Promedio académico general: {promedio_academico:.2f}")


def ordenar_estudiantes(estudiantes):
    campos = [
        "carnet",
        "nombres",
        "apellidos",
        "peso",
        "estatura en metros",
        "sexo",
        "promedio académico"
    ]

    for campo in campos:
        print(f"\nEstudiantes ordenados por {campo}:")
        estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[campo])
        mostrar_estudiantes(estudiantes_ordenados)


def main():
    estudiantes = []
    
    while True:
        print("\nMenú:")
        print("1. Ingresar estudiantes")
        print("2. Mostrar promedios generales")
        print("3. Ordenar y mostrar estudiantes")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            ingresar_estudiantes(estudiantes)
        elif opcion == '2':
            calcular_promedios_generales(estudiantes)
        elif opcion == '3':
            if estudiantes:
                ordenar_estudiantes(estudiantes)
            else:
                print("Primero debes ingresar estudiantes.")
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

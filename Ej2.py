estaciones = []
tiempos = []

n = int(input("¿Cuántas estaciones tiene la ruta? "))
for i in range(n):
    estacion = input(f"Nombre de la estación {i+1}: ")
    estaciones.append(estacion)
    if i > 0:
        tiempo = int(input(f"Tiempo en minutos de {estaciones[i-1]} a {estacion}: "))
        tiempos.append(tiempo)

print("\nEstaciones en la ruta:")
for i, estacion in enumerate(estaciones):
    print(f"{i+1}. {estacion}")

origen = input("\nIngrese estación de origen: ")
destino = input("Ingrese estación de destino: ")

try:
    idx_origen = estaciones.index(origen)
    idx_destino = estaciones.index(destino)
    
    if idx_origen < idx_destino:
        tiempo_estimado = sum(tiempos[idx_origen:idx_destino])
        print(f"\nTiempo estimado de {origen} a {destino}: {tiempo_estimado} minutos")
    elif idx_origen > idx_destino:
        print("\nError: El destino está antes del origen en la ruta.")
    else:
        print("\nYa estás en la estación de destino.")
except ValueError:
    print("\nError: Estación no encontrada.")


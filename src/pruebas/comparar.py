import csv

def comparar(resultados_totales, nombre_archivo = "resultados_algoritmos.csv"):
    cabecera = ["Algoritmo", "Puntaje total", "Lineas eliminadas", 
                "Altura maxima", "Cantidad huecos", "Tetrises", "Nivel alcanzado", "Tiempo promedio"]

    with open(nombre_archivo, mode="w", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter="|")
        escritor.writerow(cabecera)

        for resultado in resultados_totales:
            algoritmo = resultado[0]
            datos = resultado[1]

            fila = [
                algoritmo,
                datos["puntaje obtenido"],
                datos["lineas eliminadas"],
                datos["altura maxima"],
                datos["cantidad de huecos"],
                datos["cantidad de tetrises"],
                datos["nivel alcanzado"],
                datos["tiempo promedio toma decision"]
            ]

            escritor.writerow(fila)

    print(f"Archivo CSV guardado como: {nombre_archivo}")
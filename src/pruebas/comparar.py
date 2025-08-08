import csv

def comparar(resultados_totales, nombre_archivo = "resultados_algoritmos.csv"):
    cabecera = ["Algoritmo", "Puntaje total", "Lineas eliminadas", 
                "Altura maxima", "Cantidad huecos", "Tetrises", "Nivel alcanzado", 
                "Tiempo promedio", "Singles", "Dobles", "Triples"]

    with open(nombre_archivo, mode="w", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter="|")
        escritor.writerow(cabecera)

        for resultado in resultados_totales:
            algoritmo = resultado[0]
            datos = resultado[1]

            fila = [
                algoritmo,
                datos.get("puntaje obtenido",0),
                datos.get("lineas eliminadas",0),
                datos.get("altura maxima",0),
                datos.get("cantidad de huecos",0),
                datos.get("cantidad de tetrises",0),
                datos.get("nivel alcanzado",0),
                datos.get("tiempo promedio toma decision",0),
                datos.get("singles",0),
                datos.get("doubles",0),
                datos.get("triples",0)
            ]

            escritor.writerow(fila)

    print(f"Archivo CSV guardado como: {nombre_archivo}")
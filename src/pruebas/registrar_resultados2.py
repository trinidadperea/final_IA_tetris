import csv
import json

def registrar_resultados2(resultados_totales, nombre_archivo = "resultados_algoritmos2.csv"):
    cabecera = [
        "Algoritmo", "Iteracion", "Piezas totales", "Puntaje", "Tiempo promedio",
        "Lineas eliminadas", "Altura max", "Huecos",
        "Singles", "Doubles", "Triples", "Tetrises", "Nivel",
        "Alturas parciales"
    ]

    with open(nombre_archivo, mode="w", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter="|")
        escritor.writerow(cabecera)

        for resultado in resultados_totales:
            algoritmo = resultado[0]
            iter = resultado[1]
            datos = resultado[2]

            alturas = datos.get("alturas_parciales", [])

            fila = [
                algoritmo,
                iter,
                datos.get("piezas totales", 0),
                datos.get("puntaje obtenido", 0),
                datos.get("tiempo promedio toma decision", 0),
                datos.get("lineas eliminadas", 0),
                datos.get("altura maxima", 0),
                datos.get("cantidad de huecos", 0),
                datos.get("singles", 0),
                datos.get("doubles", 0),
                datos.get("triples", 0),
                datos.get("tetrises", 0),
                datos.get("nivel alcanzado", 0),
                json.dumps(alturas)  # guarda la lista como string
            ]

            escritor.writerow(fila)

    print(f"Archivo CSV guardado como: {nombre_archivo}")

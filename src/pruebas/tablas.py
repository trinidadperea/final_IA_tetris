import pandas as pd

def promedios():
    # Visualizamos que algoritmo es mas eficiente en cada metrica

    # Cargar datos sin la columna Iteracion
    df = pd.read_csv("resultados_algoritmos.csv", sep='|', usecols=lambda col: col != 'Iteracion')

    # Calcular promedios
    tabla_promedios = (
        df.groupby("Algoritmo")
        .mean(numeric_only=True)
        .reindex(["Hill Climbing", "Simulated Annealing", "Genetico"])  # fuerza el orden
        .T
    )

    # Poner índice
    tabla_promedios.index.name = "Métrica"

    # Guardar CSV
    tabla_promedios.to_csv("tabla_promedio_metricas.csv")

def relacion_piezas_lineas():
    # Relacion entre cantidad de piezas y lienas eliminadas
    # que tan efecitivas son las decisiones

    df = pd.read_csv("resultados_algoritmos.csv", sep='|')

    tabla = df.groupby("Algoritmo").agg({
        'Piezas totales': 'first',
        'Lineas eliminadas': 'sum'
    }).reset_index()

    tabla['Lineas/pieza'] = tabla['Lineas eliminadas'] / tabla['Piezas totales']

    tabla = tabla[['Algoritmo', 'Piezas totales', 'Lineas eliminadas', 'Lineas/pieza']]

    tabla.to_csv("tabla_piezas_lineas.csv", index=False)

def promedio_de_eliminaciones():
    # visualizamos el estilo de juego de cada algoritmo
    
    df = pd.read_csv("resultados_algoritmos.csv", sep='|')

    eliminaciones = ['Singles', 'Doubles', 'Triples', 'Tetrises']

    prom = df.groupby("Algoritmo")[eliminaciones].mean()

    tabla = prom.T

    tabla.index.name = 'Métrica'

    tabla.to_csv("tabla_promedio_eliminaciones.csv")

def consistencia():
    # promedio, desv estandarm coeficiente de variacion de los puntajes
    # cv bajo = resultados mas consistentes

    df = pd.read_csv("resultados_algoritmos.csv", sep='|')

    metricas = ["Puntaje", "Lineas eliminadas"]

    tabla = df.groupby("Algoritmo")

    filas = []

    for algoritmo, datos in tabla:
        for metrica in metricas:
            promedio = datos[metrica].mean()
            desv = datos[metrica].std()
            cv = (desv / promedio) * 100 if promedio != 0 else 0
            
            filas.append({
                'Algoritmo': algoritmo,
                'Métrica': metrica,
                'Promedio': round(promedio,2),
                'Desv. Estandar': round(desv, 2),
                'Cv%': f"{round(cv, 2)}%" 
            })

    tabla_consistencia = pd.DataFrame(filas)

    tabla_consistencia.to_csv("tabla_consistencia.csv", index = False)

    
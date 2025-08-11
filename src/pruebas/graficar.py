import os
import matplotlib.pyplot as plt
import numpy as np

def graficar(resultados_totales):
    # creo carpeta
    carpeta_dir = "images_test" 
    os.makedirs(carpeta_dir, exist_ok=True)

    #gráfico de dispersión con Puntaje vs Tiempo promedio por algoritmo. 
    grafico_dispersion(resultados_totales, os.path.join(carpeta_dir, "puntaje_vs_tiempo.png"))
    grafico_puntaje_total(resultados_totales, os.path.join(carpeta_dir, "puntaje_total.png"))
    grafico_nivel_puntaje(resultados_totales, os.path.join(carpeta_dir, "nivel_vs_puntaje.png"))
    grafico_lineas_eliminadas(resultados_totales, os.path.join(carpeta_dir, "lineas_eliminadas.png"))

def grafico_dispersion(resultados, imagen):
    algoritmos = []
    puntajes = []
    tiempos = []

    for nombre, _, datos in resultados:
        algoritmos.append(nombre)
        puntajes.append(datos['puntaje obtenido'])
        tiempos.append(datos['tiempo promedio toma decision'])

    # Crear gráfico
    plt.figure(figsize=(8, 6))
    plt.scatter(tiempos, puntajes)

    # Etiquetar puntos
    for i, nombre in enumerate(algoritmos):
        plt.text(tiempos[i], puntajes[i] + 10, nombre.upper(), ha='center')

    # Ejes y título
    plt.xlabel('Tiempo promedio de decisión (s)')
    plt.ylabel('Puntaje obtenido')
    plt.title('Comparación de Puntaje vs Tiempo por Algoritmo')
    plt.grid(True)
    plt.tight_layout()

    # Guardar imagen
    plt.savefig(imagen)
    plt.close()


def grafico_puntaje_total(resultados, imagen):
    # Datos
    algoritmos = []
    puntajes = []

    for nombre, _, datos in resultados:
        algoritmos.append(nombre)
        puntajes.append(datos['puntaje obtenido'])

    # Crear gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(algoritmos, puntajes, color='skyblue', edgecolor='black')

    # Etiquetas y título
    plt.xlabel('Algoritmo')
    plt.ylabel('Puntaje obtenido')
    plt.title('Comparación de Puntaje Total por Algoritmo')

    # Etiquetas encima de cada barra
    for i, v in enumerate(puntajes):
        plt.text(i, v + 5, str(v), ha='center', fontweight='bold')

    # Guardar imagen
    plt.tight_layout()
    plt.savefig(imagen)
    plt.close()

def grafico_nivel_puntaje(resultados, imagen):
    #datos
    algoritmos = []
    niveles = []
    puntajes = []

    for nombre, _, datos in resultados:
        algoritmos.append(nombre)
        niveles.append(datos['nivel alcanzado'])
        puntajes.append(datos['puntaje obtenido'])

    # Crear gráfico
    plt.figure(figsize=(8, 6))
    plt.scatter(niveles, puntajes, c='blue', edgecolors='black', s=100)

    # Etiquetas sobre los puntos
    for i, nombre in enumerate(algoritmos):
        plt.text(niveles[i], puntajes[i] + 10, nombre.upper(), ha='center')

    # Configuración de ejes y título
    plt.xlabel('Nivel alcanzado')
    plt.ylabel('Puntaje obtenido')
    plt.title('Nivel alcanzado vs Puntaje por Algoritmo')
    plt.grid(True)
    plt.tight_layout()

    # Guardar imagen
    plt.savefig(imagen)
    plt.close()

def grafico_lineas_eliminadas(resultados, imagen):
    # Datos
    algoritmos = []
    singles = []
    doubles = []
    triples = []

    for nombre, _, datos in resultados:
        algoritmos.append(nombre)
        singles.append(datos.get('singles',0))
        doubles.append(datos.get('doubles',0))
        triples.append(datos.get('triples',0))

    # Configuración para barras agrupadas
    x = np.arange(len(algoritmos))
    ancho = 0.25

    plt.figure(figsize=(8, 6))
    plt.bar(x - ancho, singles, width=ancho, label='Singles', color='skyblue')
    plt.bar(x, doubles, width=ancho, label='Doubles', color='orange')
    plt.bar(x + ancho, triples, width=ancho, label='Triples', color='green')

    # Etiquetas y título
    plt.xlabel('Algoritmos')
    plt.ylabel('Cantidad de líneas eliminadas')
    plt.title('Comparación de Singles, Doubles y Triples por Algoritmo')
    plt.xticks(x, algoritmos)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Guardar gráfico
    plt.savefig(imagen)
    plt.close()


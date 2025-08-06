import matplotlib.pyplot as plt
import numpy as np

def graficar(resultados_totales):

    #gráfico de dispersión con Puntaje vs Tiempo promedio por algoritmo.

    algoritmos = []
    puntajes = []
    tiempos = []

    for nombre, datos in resultados_totales:
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
    plt.savefig("puntaje_vs_tiempo.png")
    plt.close()
    print("Gráfico guardado como 'puntaje_vs_tiempo.png'.")

# este es un grafico con todos los datos en uno mismo
''' 
# grafico araña
def graficar(resultados_totales):
    # Métricas a mostrar (excluyendo "Algoritmo")
    etiquetas = ["Puntaje total", "Lineas eliminadas", "Altura maxima",
                 "Cantidad huecos", "Tetrises", "Nivel alcanzado", "Tiempo promedio"]

    # Número de variables
    num_vars = len(etiquetas)

    # Ángulos para el gráfico radar (completo un círculo)
    angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angulos += angulos[:1]  # para cerrar el círculo

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

    for algoritmo, datos in resultados_totales:
        valores = [
            datos["puntaje obtenido"],
            datos["lineas eliminadas"],
            datos["altura maxima"],
            datos["cantidad de huecos"],
            datos["cantidad de tetrises"],
            datos["nivel alcanzado"],
            datos["tiempo promedio toma decision"]
        ]
        valores += valores[:1]  # cerrar el círculo

        ax.plot(angulos, valores, label=algoritmo)
        ax.fill(angulos, valores, alpha=0.25)

    # Configuraciones
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.set_thetagrids(np.degrees(angulos[:-1]), etiquetas)

    # Limpiar eje radial
    ax.set_ylim(0, max(
        max([
            datos["puntaje obtenido"] for _, datos in resultados_totales
        ]) * 1.1,  # multiplicar por 1.1 para margen
        1
    ))

    ax.grid(True)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.title("Comparación de algoritmos (múltiples métricas)")
    plt.show()
''' 

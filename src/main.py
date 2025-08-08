from controlador import *
from pruebas.graficar import graficar
from pruebas.comparar import comparar
import random

def main():
    # semilla para misma secuencia de piezas
    semilla = random.randint(0,100)
    # algoritmos
    algoritmos = ["Hill Climbing", "Simulated Annealing", "Genetico"]
    resultados_totales = []
    for algoritmo in algoritmos:
        resultado = controlador(algoritmo, semilla)
        resultados_totales.append((algoritmo,resultado))
    print("Res total: ",resultados_totales)
    graficar(resultados_totales)
    comparar(resultados_totales)

if __name__ == "__main__":
    main()


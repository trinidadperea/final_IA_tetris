from controlador import *
from pruebas.graficar import graficar
from pruebas.comparar import comparar
import random

def main():
    
    # algoritmos
    algoritmos = ["Hill Climbing", "Simulated Annealing", "Genetico"]
    resultados_totales = []
    semillas = random.sample(range(0,1000000),1)

    for i in range(len(semillas)):
    
        for algoritmo in algoritmos:
            resultado = controlador(algoritmo, semillas[i])
            resultados_totales.append((algoritmo, i+1, resultado))

    print("Res total: ",resultados_totales)
    graficar(resultados_totales)
    comparar(resultados_totales)

if __name__ == "__main__":
    main()


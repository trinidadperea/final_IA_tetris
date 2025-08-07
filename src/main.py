from controlador import *
from pruebas.graficar import graficar
from pruebas.comparar import comparar

def main():
    # algoritmos
    algoritmos = ["Hill Climbing", "Simulated Annealing", "Genetico"]
    resultados_totales = []
    for algoritmo in algoritmos:
        #print("Ejecutando algoritmo: ", algoritmo)
        resultado = controlador(algoritmo)
        resultados_totales.append((algoritmo,resultado))
    print("Res total: ",resultados_totales)
    graficar(resultados_totales)
    comparar(resultados_totales)

if __name__ == "__main__":
    main()


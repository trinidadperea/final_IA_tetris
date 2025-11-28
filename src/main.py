from controlador import *
from pruebas.graficar import graficar
from pruebas.registrar_resultados import *
from pruebas.registrar_resultados2 import *
import pruebas.tablas as tabla
import random

def main():
    
    # algoritmos + genetico nuevo
    algoritmos = ["Hill Climbing", "Simulated Annealing", "Genetico", "Genetico nuevo"]
    
    piezas_totales = 400
    resultados_totales = []
    semillas = random.sample(range(0,1000000),15)
    
    for i in range(len(semillas)):
        
        for algoritmo in algoritmos:
            print(f"Algoritmo {algoritmo}, iteracion: {i}")
            resultado = controlador(algoritmo, semillas[i], piezas_totales)
            resultados_totales.append((algoritmo, i+1, resultado))
        print("")

    print("Res total: ",resultados_totales)
    #registrar_resultados(resultados_totales)
    registrar_resultados2(resultados_totales)
    tabla.consistencia()
    tabla.promedio_de_eliminaciones()
    #agregado
    tabla.estadisticas_eliminaciones()
    #agregado
    tabla.tabla_promedio_desviacion_nivel_puntaje()
    tabla.relacion_piezas_lineas()
    #agregado
    tabla.tabla_puntaje_tiempo()
    tabla.promedios()
    
    graficar()
    

if __name__ == "__main__":
    main()


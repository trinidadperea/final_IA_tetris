from tetris import *
from busqueda_local.heuristica import * 


def genetico(juego:Tetris, it: int, rango_mutacion: int):

    # Minimo 10 posibles jugadas 
    # Maximo 40 posibles jugadas
    # entre 10 y 19 combinaciones posibles -> tamaño_poblacion < 20
    # entre 20 y 40 -> tamaño_poblacion = 20

    combinaciones = combinaciones_validas(juego)

    tamaño_poblacion = min(len(combinaciones), 20)
    
    # poblacion = {(pos,rot) = fitness}
    poblacion = random.sample(combinaciones, tamaño_poblacion)

    #
    mejor_estado = mejor_fitness(poblacion)

    elite_size = int(tamaño_poblacion * 0.1)
    h_variation = []

    i = 0
    while it > 0:
        # Selecciono los individuos mas aptos 
        seleccion = seleccionar_individuos(poblacion)

        # Genero la poblacion nueva haciendo cruce entre los mas aptos
        poblacion_nueva = cruce(seleccion)

    



def mejor_fitness(combinaciones: {(tuple)}): #si varias tienen el mejor fitness se queda con la primera
    #sum_fitness = 0
    mejor_fitness = float("-inf")
    mejor_combinacion = None
    combinaciones = {}

    for (pos,rot), fitness in combinaciones.items():
        #sum_fitness += mejor_fitness

        if fitness > mejor_fitness:
            mejor_combinacion = (pos,rot)
            mejor_fitness = fitness

    return mejor_combinacion


# Seleccionamos por metodo de torneo sencillo
def seleccionar_individuos(poblacion):
    individuos = []

    # Determino el tamaño de los grupos
    if len(poblacion) % 2 == 0:
        n = 2
    else:
        n = 3

    grupos= agrupar_random(poblacion,n)
    # [{(pos1,rot1):fitness1, (pos2,rot2): fitness2}, {():f, ():f},...]

    # Se toma de cada grupo el individuo con mejor fitness
    for grupo in grupos:
        mejor_fitness = max(grupo.items())
        mejor_ind = [combinacion for combinacion, fitness in grupo.items() if fitness == mejor_fitness]

        if (len(mejor_ind)) > 1:
            k = random.randint(0,1)

            individuos.append(mejor_ind[k])
        else:
            individuos.append(mejor_ind[0])
    
    return individuos


def agrupar_random(poblacion, n):
    items = list(poblacion.items())
    random.shuffle(items)

    return [dict(items[i:i + n]) for i in range(0,len(items), n)]

def cruce(seleccion: list[(tuple)]):
    nueva_poblacion = []

    #cruce entre individuos que coincidan en algun elemento de la tupla





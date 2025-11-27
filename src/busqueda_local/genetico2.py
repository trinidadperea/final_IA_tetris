from tetris import *
from busqueda_local.heuristica import * 


def genetico2(juego:Tetris, iteraciones: int):

    # [(pos,rot,fit), ...]
    combinaciones = combinaciones_validas(juego, "GA")

    tamaño_poblacion = min(len(combinaciones), 20)
    
    # poblacion = {(pos,rot,fit), ...}
    poblacion = random.sample(combinaciones, tamaño_poblacion)

    # (pos,rot)
    mejor_estado = mejor_fitness(poblacion)

    return mejor_estado[:2]


# combinaciones = {(pos,rot,fit)}
def mejor_fitness(combinaciones: dict): #si varias tienen el mejor fitness se queda con la primera

    #sum_fitness = 0
    mejor_fitness = float("-inf")
    mejor_combinacion = None
    
    for (pos,rot,fit) in combinaciones:
        #sum_fitness += mejor_fitness

        if fit > mejor_fitness:
            mejor_combinacion = (pos,rot,fit)
            mejor_fitness = fit

    return mejor_combinacion
    

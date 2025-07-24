from tetris import *
from heuristica import *


#evaluar todos los vecinos (combinaciones posicion-movimiento)

def hill_climbing(juego:Tetris):

    juego_copia = juego.copy()

    vecinos = {}

    columna = 0
    
    while columna < juego.tablero.columnas:
        if juego_copia.mover_si_valido(juego_copia.pieza_actual,columna,0):
            puntaje_max = float("-inf")

            rotacion = 0

            # Buscamos para cada pos la mejor rotacion y el mejor puntaje
            while rotacion < len(juego.pieza_actual.formas):

                if juego_copia.rotar_si_valido():
                    puntaje_parcial = heuristica(juego_copia) #le paso la copia para obtener los resultados parciales de cada mov

                    if puntaje_parcial > puntaje_max:
                        rot = juego_copia.pieza_actual.rotacion
                        puntaje_max = puntaje_parcial

                rotacion += 1
            
            vecinos[(columna,rot)] = puntaje_max

        columna += 1
    
    puntaje_max = max(vecinos.values())

    # pueden haber mas vecinos 
    mejor_vecino = [vecino for vecino, puntaje in vecinos.items() if puntaje == puntaje_max]

    if len(mejor_vecino) > 1:
        return mejor_vecino[random.randint(0,len(mejor_vecino)-1)]

    return mejor_vecino[0]

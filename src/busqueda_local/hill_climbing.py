from tetris import *
from busqueda_local.heuristica import *


#evaluar todos los vecinos (combinaciones posicion-movimiento)

def hill_climbing(juego:Tetris):

    juego_copia = juego.copy()

    vecinos = {}

    columna = 0
    
    while columna < juego.tablero.columnas:

        hay_vecino = False

        #juego_copia.pieza_actual.rotar() #coloco la pieza en 90°

        if mover_a_columna(juego_copia,columna):
            
            puntaje_max = float("-inf")

            rotacion = 0

            # Buscamos para cada pos la mejor rotacion y el mejor puntaje
            while rotacion < 4:
                juego_copia = juego.copy()
                
                print(f"pieza actual antes de heuristica:{juego_copia.pieza_actual.pieza}")
            
                if juego_copia.rotar_si_valido():
                    puntaje_parcial = heuristica(juego_copia) #le paso la copia para obtener los resultados parciales de cada mov
                    print(f"pieza actual despues de heuristica:{juego_copia.pieza_actual.pieza}")
                    if puntaje_parcial > puntaje_max:
                        hay_vecino = True
                        rot = juego_copia.pieza_actual.rotacion
                        puntaje_max = puntaje_parcial

                rotacion += 1

            if hay_vecino: 
                vecinos[(columna,rot)] = puntaje_max

        columna += 1
    
    puntaje_max = max(vecinos.values())

    # pueden haber mas vecinos 
    mejor_vecino = [vecino for vecino, puntaje in vecinos.items() if puntaje == puntaje_max]

    if len(mejor_vecino) > 1:
        return mejor_vecino[random.randint(0,len(mejor_vecino)-1)]

    return mejor_vecino[0]

def mover_a_columna(juego: Tetris, destino):
    x_act = juego.pieza_actual.x
    desplazamiento = destino - x_act

    if desplazamiento > 0:
        dx = 1
    else:
        dx = -1

    for _ in range(abs(desplazamiento)):
        if not juego.mover_si_valido(juego.pieza_actual,dx,0):
            return False
    return True

def hill_climbing1(juego:Tetris):
    vecinos = {}

    for columna in range(juego.tablero.columnas):

        hay_vecino = False
        puntaje_max = float("-inf")

        for rotacion in range(len(juego.pieza_actual.formas)):
            simulacion = juego.copy()

            for _ in range(rotacion):
                
                if not simulacion.rotar_si_valido():
                    break
            else: 
                
                if mover_a_columna(simulacion, columna):
                    puntaje = heuristica(simulacion)

                    if puntaje > puntaje_max:
                        hay_vecino = True
                        mejor_rot = rotacion
                        mejor_pos = columna
        
        if hay_vecino:
            vecinos[(mejor_pos, mejor_rot)] = puntaje
        
    puntaje_max = max(vecinos.values())

    # pueden haber mas vecinos 
    mejor_vecino = [vecino for vecino, puntaje in vecinos.items() if puntaje == puntaje_max]

    if len(mejor_vecino) > 1:
        return mejor_vecino[random.randint(0,len(mejor_vecino)-1)]

    return mejor_vecino[0]



from tetris import *
from busqueda_local.heuristica import *

def hill_climbing(juego:Tetris):
    vecinos = {}

    for columna in range(juego.tablero.columnas):

        hay_vecino = False
        puntaje_max = float("-inf")

        for rotacion in range(len(juego.pieza_actual.formas)):
            simulacion = juego.copy()
            pieza = juego.pieza_actual.pieza
            
            while simulacion.pieza_actual.y < 0:
                simulacion.pieza_actual.mover(0,1)

            for _ in range(rotacion):
                if not simulacion.rotar_si_valido():
                    #print(f"rotacion no valida: pieza = {pieza}, rotacion = {rotacion}, columna = {columna}, x = {juego.pieza_actual.x}, y = {juego.pieza_actual.y}")
                    break
            else:
                
                #print(f"combinacion({columna, simulacion.pieza_actual.rotacion})")
                if mover_a_columna(simulacion, columna):
                    bajar_pieza(simulacion)
                    rot = simulacion.pieza_actual.rotacion
                    pos_x = simulacion.pieza_actual.x
                    pos_y = simulacion.pieza_actual.y
                    
                    simulacion.actualizar_estado()
                    #print(f"Calculo funcion heuristica para: pos_x = {pos_x}, pos_y = {pos_y}, pieza = {pieza}")
                    #print(f"Cant de huecos actualizada: {simulacion.tablero.cant_huecos}")
                    puntaje = heuristica(simulacion)
                    #print(f"resultado heuristica: {puntaje,pos_x,pos_y,rot,pieza}")
                    
                    if puntaje > puntaje_max:
                       #print(f"puntaje:p{puntaje}, puntaje_max: {puntaje_max}, pieza: {pieza}, rotacion: {rot}")
                        hay_vecino = True
                        mejor_rot = rot
                        mejor_pos_x = pos_x
                        mejor_pos_y = pos_y
                        puntaje_max = puntaje
                        
                    #print(" ")
        if hay_vecino:
            vecinos[(mejor_pos_x, mejor_pos_y, mejor_rot)] = puntaje_max
                    
    puntaje_max = max(vecinos.values())
    
    #print("")
    
    #print(f"vecinos: {vecinos}")
    #print("")
    
    # [(x,y,rot), (), ...]
    mejor_vecino = [vecino for vecino, puntaje in vecinos.items() if puntaje == puntaje_max]

    mejor_y = max(mejor_vecino, key = lambda t: t[1])[1]
    #print(f"mejor y = {mejor_y}")

    if len(mejor_vecino) > 1:
        mejor_vecino = [vecino for vecino in mejor_vecino if vecino[1] == mejor_y]
        #print("")
        #print(f"vecinos con mejor y: {mejor_vecino}")
        if len(mejor_vecino) > 1:
            return mejor_vecino[random.randint(0,len(mejor_vecino)-1)]
    

    #print(" ")
    #print(f"mejor_vecino = {mejor_vecino}")
    return mejor_vecino[0]






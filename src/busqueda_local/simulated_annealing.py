from tetris import *
import math 
import random
from tetris import *
from busqueda_local.heuristica import *


def simulated_annealing(juego: Tetris, enfriamiento=0.95, T_min=0.1, max_iter=100):
    
    pieza = juego.pieza_actual.pieza
    #print(f"Pieza actual: ", pieza)

    # Temperaruras ------
    T_inicial = -4 / math.log(0.6) # si delta = -4 la probabilidad de aceptacion es del 60%
    T_max = T_inicial

    iteracion = 0

    # Lista de combinaciones validas (pos,rot,heuritica)
    combinaciones = combinaciones_validas(juego)
    vecinos = combinaciones
    #print(f"Vecinos: ",vecinos)

    estado_actual = random.choice(vecinos)
    h_estado_actual = estado_actual[-1]
    #print(f"Movimiento a realizar: ", estado_actual)

    while T_max > T_min and iteracion < max_iter:
                
        estado_nuevo = random.choice(combinaciones)
        h_estado_nuevo = estado_nuevo[-1]

        delta = h_estado_nuevo - h_estado_actual
        #print(f"Delta: (puntaje vecino - puntaje actual): ", delta)

        if delta > 0 or random.random() < math.exp(delta / T_max):
            
            estado_actual = estado_nuevo[:2]
            h_estado_actual = h_estado_nuevo

        
        T_max *= enfriamiento
        iteracion += 1
        #print(f"Temperatura actualizada: ",T_max)
        #print(f"Estado actual = {estado_actual}, heuristica = {h_estado_actual}")
        #print(f"Iteracion: ", iteracion)

        #print(" ")

    return estado_actual[:2]

'''

# funciones probabilidades
def logarithmic(k):
    return 100 / (1 + k)

def exponential(k, n):
    t0 = 10 * n
    alpha = 0.95
    return t0 * (alpha ** k) '''
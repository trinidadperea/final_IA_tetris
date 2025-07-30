from tetris import *
import math 
import random
from tetris import *
from busqueda_local.heuristica import *
from busqueda_local.hill_climbing import *

def simulated_annealing(juego: Tetris, T_max=1000, enfriamiento=0.99, T_min=0.1, max_iter=100):
    
    estado_actual = juego.copy()
    pieza = estado_actual.pieza_actual.pieza
    print(f"Pieza actual: ", pieza)
    puntaje_actual = heuristica(estado_actual)
    print(f"Puntaje actual: ",puntaje_actual)
    mejor_movimiento = None
    mejor_puntaje = float("-inf")

    iteracion = 0

    while T_max > T_min and iteracion < max_iter:
        #genero todos los vecinos posibles actuales
        vecinos = calcular_vecino(estado_actual)
        print(f"Vecinos: ",vecinos)

        if not vecinos:
            break
        
        #a diferencia de hc, se elige un vecino random, no el mejor, y se evalua
        movimiento = random.choice(vecinos)
        print(f"Movimiento a realizar: ", movimiento)

        estado_vecino = aplicar_movimiento(estado_actual, movimiento)
        puntaje_vecino = heuristica(estado_vecino)
        print(f"Puntaje vecino: ", puntaje_vecino)

        #calculo el cambio de puntaje
        delta = puntaje_vecino - puntaje_actual
        print(f"Delta: (puntajr vecino . puntajr actual): ", delta)

        # funcion probabilidad
        # si el delta es mejor acepto, sino lo acpto con la funcion de probabilidad
        if delta > 0 or random.random() < math.exp(delta / T_max):
            #estado_actual = estado_vecino
            #puntaje_actual = puntaje_vecino

            if puntaje_vecino > mejor_puntaje:
                mejor_puntaje = puntaje_vecino
                mejor_movimiento = movimiento

        T_max *= enfriamiento
        print(f"Temperatura actualizada: ",T_max)
        iteracion += 1
        print(f"Iteracion: ", iteracion)

        print(" ")
    return mejor_movimiento

def calcular_vecino(juego: Tetris):
    vecinos = []

    for rotacion in range(len(juego.pieza_actual.formas)):
        for columna in range(juego.tablero.columnas):
            simulador = juego.copy()

            simulador.pieza_actual.rotacion = 0
            for _ in range(rotacion):
                simulador.rotar_si_valido()
            
            if not mover_a_columna(simulador, columna):
                continue

            mover_a_columna(simulador, columna)
            #if simulador.mover_si_valido(simulador.pieza_actual,0,1,"vertical"):
            vecinos.append([columna,rotacion])
    return vecinos

def aplicar_movimiento(juego: Tetris, movimiento):
    x, rot = movimiento
    simulador = juego.copy()

    simulador.pieza_actual.rotacion = 0
    for _ in range(rot):
        simulador.rotar_si_valido()

    mover_a_columna(simulador, x)

    #while simulador.mover_si_valido(simulador.pieza_actual,0,1,"vertical"):
    #    continue
    # fijar y actualizar estado
    simulador.actualizar_estado()

    puntaje = heuristica(simulador)

    print(f"Aplicando movimiento: x={x}, rot={rot}, puntaje={puntaje}")

    return simulador


                         
'''

# funciones probabilidades
def logarithmic(k):
    return 100 / (1 + k)

def exponential(k, n):
    t0 = 10 * n
    alpha = 0.95
    return t0 * (alpha ** k) '''
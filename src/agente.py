from tetris import *
from busqueda_local.hill_climbing import *
from busqueda_local.simulated_annealing import *
from busqueda_local.genetico import *

class Agente():
        
    def jugar(self, juego:Tetris, algoritmo):

        if algoritmo == "Hill Climbing":
            (mejor_pos,_,mejor_rot) = hill_climbing(juego)
        
        if algoritmo == "Genetico":
            (mejor_pos,mejor_rot) = genetico(juego, 100)

        if algoritmo == "Simulated Annealing":
            (mejor_pos,mejor_rot) = simulated_annealing(juego)

        
        while juego.pieza_actual.y < 0:
                juego.pieza_actual.mover(0,1)
        
        #print(f"Agente: moviendo a x={mejor_pos}, rot={mejor_rot}")
        #print("")
        
        #roto hasta la mejor pos
        cont = 0
        while juego.pieza_actual.rotacion != mejor_rot and cont < len(juego.pieza_actual.formas):
            if juego.rotar_si_valido():
                cont += 1
            else:
                break
                
        pos_actual = juego.pieza_actual.x

        while pos_actual > mejor_pos:
            if not juego.mover_si_valido(juego.pieza_actual,-1,0, "horizontal"):
                break
            pos_actual -= 1
        
        while pos_actual < mejor_pos:
            if not juego.mover_si_valido(juego.pieza_actual, 1,0, "horizontal"):
                break
            pos_actual += 1
        
        #print(f"Pos actual: {juego.pieza_actual.x}, rot: {juego.pieza_actual.rotacion}")


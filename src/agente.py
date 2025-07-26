from tetris import *
from busqueda_local.hill_climbing import *


class Agente():

    def jugar(self, juego: Tetris):
        (mejor_pos,mejor_rot) = hill_climbing1(juego)

        
        print(f"Agente: moviendo a x={mejor_pos}, rot={mejor_rot}")


        cont = 0
        while juego.pieza_actual.rotacion != mejor_rot and cont < len(juego.pieza_actual.formas):
            if juego.rotar_si_valido():
                cont += 1
            else:
                break
                
        pos_actual = juego.pieza_actual.x

        while pos_actual > mejor_pos:
            if not juego.mover_si_valido(juego.pieza_actual,-1,0):
                break
            pos_actual -= 1
        
        while pos_actual < mejor_pos:
            if not juego.mover_si_valido(juego.pieza_actual, 1,0):
                break
            pos_actual += 1
        
        print(f"Pos actual: {juego.pieza_actual.x}, rot: {juego.pieza_actual.rotacion}")

        


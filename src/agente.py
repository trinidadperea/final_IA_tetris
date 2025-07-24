from tetris import *
from busqueda_local.hill_climbing import *


class Agente():

    def __init__ (self, juego: Tetris):
        self.juego = juego

    def jugar(self):
        (mejor_rot, mejor_pos) = hill_climbing(self.juego)

        pos_actual = self.juego.pieza_actual.x

        while pos_actual > mejor_pos:
            self.juego.pieza_actual.mover(-1,0)
            pos_actual -= 1

        while pos_actual < mejor_pos:
            self.juego.pieza_actual.mover(1,0)
            pos_actual += 1
        
        while self.juego.pieza_actual.rotacion != mejor_rot:
            self.juego.pieza_actual.rotar()

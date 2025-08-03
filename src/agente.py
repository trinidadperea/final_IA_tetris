from tetris import *
from busqueda_local.hill_climbing import *
from busqueda_local.simulated_annealing import *
from busqueda_local.genetico import *

class Agente():
        
    # para jugar con hill climbing
    def jugar(self, juego:Tetris):
        
        #(mejor_pos,mejor_rot) = simulated_annealing(juego)

        (mejor_pos,mejor_rot,_) = genetico(juego, 9)

        #(mejor_pos,_,mejor_rot) = hill_climbing(juego)

        while juego.pieza_actual.y < 0:
                juego.pieza_actual.mover(0,1)
        
        print(f"Agente: moviendo a x={mejor_pos}, rot={mejor_rot}")
        
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
        
        print(f"Pos actual: {juego.pieza_actual.x}, rot: {juego.pieza_actual.rotacion}")

    # para jugar con simulated annealing
"""def jugarSA(self, juego: Tetris):

        movimiento = simulated_annealing(juego)
        print(f"Movimiento sugerido: ", movimiento)

        #no hay movimientos validos
        if movimiento is None: 
            return
        
        x, rot = movimiento

        # Reiniciamos rotación
        juego.pieza_actual.rotacion = 0
        for _ in range(rot):
            juego.rotar_si_valido()

        # Mover a la columna deseada
        mover_a_columna(juego, x)

        # Fijar y actualizar el estado
        juego.actualizar_estado()
        print(f"estado del juego: ",juego.actualizar_estado())
        

    def jugar(self, juego, metodo):
        if metodo == "HC":
            self.jugarHC(juego)
        elif metodo == "SA":
            self.jugarSA(juego)"""
# main.py

from tetris import Tetris
from tetromino import Tetromino
from tablero import Tablero
from interfaz import *
import pygame

import pygame

def main():
    pygame.init()
    
    ancho = 300  # 10 columnas * 30px (ajustá según tu tablero)
    alto = 660   # 20 filas * 30px
    
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Tetris")
    
    # Crear tablero y juego
    tablero = Tablero(22,10,30) 
    tablero.estadoActual = tablero.generarMatriz()
    juego = Tetris(tablero)
    juego.actualizar_estado()
    
    # Crear interfaz (asumiendo que la tenés)
    interfaz = Interfaz(juego, screen)
    
    reloj = pygame.time.Clock()
    corriendo = True
    
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                
            # Aquí podés manejar teclado para mover/rotar la pieza
            # if evento.type == pygame.KEYDOWN:
            #     if evento.key == pygame.K_LEFT:
            #         juego.mover_izquierda()
            #     ...
        
        # Actualizá lógica del juego (bajar pieza, colisiones, etc)
        # juego.actualizar()  # Si tenés un método así
        
        # Dibujá todo
        interfaz.dibujar_gui()  # Implementá esto en tu clase Interfaz
        
        pygame.display.update()
        reloj.tick(60)  # 60 FPS

        
    
    pygame.quit()
    


if __name__ == "__main__":
    main()



# rotar pieza probando

"""def main():
    # Crear el tablero
    tablero = Tablero()
    tablero.estadoActual = tablero.generarMatriz()  # Matriz vacía (todo ceros)

    # Crear instancia de Tetris con el tablero y bag vacío (por ahora)
    juego = Tetris(tablero, [])

    # Crear y asignar una pieza 'I'
    juego.pieza_actual = Tetromino('L')

    print("Forma inicial:")
    juego.pieza_actual.imprimir_pieza()

    # Intentar rotar la pieza
    if juego.moverPieza():
        print("Forma luego de rotar:")
        juego.pieza_actual.imprimir_pieza()
    else:
        print("Rotación inválida, no se rotó la pieza.")

if __name__ == "__main__":
    main() """


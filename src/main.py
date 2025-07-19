from tetris import Tetris
from tetromino import Tetromino
from tablero import Tablero
from interfaz import *
import pygame

def main():
    pygame.init()
    
    # Screen
    ancho = 300 + 150 # 10 columnas * 30px + 150 del panel
    alto = 660   # 20 filas * 30px
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Tetris")
    
    # Estado incial del juego
    tablero = Tablero(22,10,30) 
    tablero.estado_actual = tablero.generarMatriz()
    juego = Tetris(tablero)
    juego.agregar_pieza_nueva()
    
    # Interfaz
    interfaz = Interfaz(juego, screen)
    
    # Tiempos
    reloj = pygame.time.Clock()
    corriendo = True
    tiempo_ultimo_movimiento = pygame.time.get_ticks()
    intervalo_bajada = juego.vel_caida  # ms

    while corriendo:
        
        ahora = pygame.time.get_ticks()
        if ahora - tiempo_ultimo_movimiento > intervalo_bajada:
            
            juego.actualizar_estado()
            tiempo_ultimo_movimiento = ahora

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            # muevo la pieza con las teclas izq, der
            if evento.type == pygame.KEYDOWN:
                # si quieremos que acelere el tiempo podemos dejar que toque para abajo, sino lo sacamos
                #if evento.key == pygame.K_DOWN:
                #    juego.pieza_actual.mover_si_valido(0,-1,juego.tablero) 
                if evento.key == pygame.K_LEFT:
                    juego.mover_si_valido(-1,0)
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
                if evento.key == pygame.K_RIGHT:
                    juego.mover_si_valido(1,0)
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
                # si quiero rotar la pieza toco espacio
                if evento.key == pygame.K_SPACE:
                    juego.rotar_si_valido()
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
            
        
        # Actualizá lógica del juego (bajar pieza, colisiones, etc)
        # juego.actualizar()  # Si tenés un método así
        
        
        interfaz.dibujar_gui() 
        
        pygame.display.update()
        reloj.tick(60)  # 60 FPS

        
    
    pygame.quit()
    


if __name__ == "__main__":
    main()



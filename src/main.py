from tetris import Tetris
from tetromino import Tetromino
from tablero import Tablero
from interfaz import *
import pygame

def main():
    pygame.init()
    
    ancho = 300 + 150 # 10 columnas * 30px + 150 del panel
    alto = 660   # 20 filas * 30px
    
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Tetris")
    
    tablero = Tablero(22,10,30) 
    tablero.estadoActual = tablero.generarMatriz()
    juego = Tetris(tablero)
    juego.actualizar_estado()
    
    #tiempo_inicio = pygame.time.get_ticks()

    interfaz = Interfaz(juego, screen)
    
    reloj = pygame.time.Clock()
    corriendo = True

    tiempo_ultimo_movimiento = pygame.time.get_ticks()
    intervalo_bajada = 500  # ms
    while corriendo:
        # aca manejo que vaya bajando con un tiempo de 500 ms
        ahora = pygame.time.get_ticks()
        if ahora - tiempo_ultimo_movimiento > intervalo_bajada:
            if not juego.pieza_actual.mover_si_valido(0,1,juego.tablero):
                lineas_borradas, game_over = juego.tablero.fijar_pieza(juego.pieza_actual)
                juego.determinarPuntosJE(lineas_borradas)
                # print("Puntaje:", juego.puntaje) 
                juego.pieza_actual = juego.agregar_pieza_nueva()
                if game_over == True:
                    #print("Game over")
                    corriendo = False
                else:
                    juego.pieza_actual = juego.agregar_pieza_nueva()
                    juego.actualizar_pieza_fantasma()
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
                    juego.pieza_actual.mover_si_valido(-1,0,juego.tablero)
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
                if evento.key == pygame.K_RIGHT:
                    juego.pieza_actual.mover_si_valido(1,0,juego.tablero)
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
                # si quiero rotar la pieza toco espacio
                if evento.key == pygame.K_SPACE:
                    juego.pieza_actual.rotar_si_valido(juego.tablero)
            
        
        # Actualizá lógica del juego (bajar pieza, colisiones, etc)
        # juego.actualizar()  # Si tenés un método así
        
        
        """tiempo_actual = pygame.time.get_ticks()
        
        if tiempo_actual - tiempo_inicio > juego.tetris.vel_caida:
            pass"""

        interfaz.dibujar_gui() 
        
        pygame.display.update()
        reloj.tick(60)  # 60 FPS

        
    
    pygame.quit()
    


if __name__ == "__main__":
    main()



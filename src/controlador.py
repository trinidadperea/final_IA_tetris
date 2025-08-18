from busqueda_local import *
from pruebas import evaluar
from tetris import Tetris
from tetromino import Tetromino
from tablero import Tablero
from interfaz import *
from agente import *
from pruebas.evaluar import evaluar
import pygame
import time

def controlador(algoritmo, semilla, piezas_totales):
    # por aca se realiza el juego y las pruebas
    pygame.init()
    
    # Screen
    ancho = 300 + 200 # 10 columnas * 30px + 150 del panel
    alto = 660   # 20 filas * 30px
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(f"Tetris - {algoritmo}")
    
    # Estado incial del juego
    tablero = Tablero(22,10,30) 
    tablero.estado_actual = tablero.generar_matriz()
    juego = Tetris(tablero)
    # implemento semilla anes de agregar pieza nueva para que sea igual en los 3 algoritmos
    #juego.generar_semilla(semilla) 
    random.seed(semilla)
    contar_piezas = 0
    juego.agregar_pieza_nueva(contar_piezas,semilla)
    juego.nueva_pieza = True
    juego.set_nivel(1)
    
    # Interfaz
    interfaz = Interfaz(juego, screen)
    
    # Tiempos
    reloj = pygame.time.Clock()
    corriendo = True
    juego.tiempo_inicio = pygame.time.get_ticks()
    tiempo_ultimo_movimiento = pygame.time.get_ticks()
    #juego.set_vel_caida()
    #intervalo_bajada = juego.get_vel_caida()  # ms
    intervalo_bajada = 10
    # agente
    jugador = Agente()
    
    # para calcular el tiempo en la toma de decisiones
    tiempos = []
    while corriendo:
        
        ahora = pygame.time.get_ticks()
        if ahora - tiempo_ultimo_movimiento > intervalo_bajada:
        
            if juego.nueva_pieza:
                inicio = time.time()
                jugador.jugar(juego,algoritmo)
                fin = time.time()
                duracion = fin - inicio
                tiempos.append(duracion)
                juego.nueva_pieza = False

                # manejo de iteraciones para pruebas
                contar_piezas += 1
                if juego.game_over or contar_piezas >= piezas_totales:
                    corriendo = False 
                            
            nueva_fantasma = juego.actualizar_pieza_fantasma()
            interfaz.dibujar_pieza(nueva_fantasma, True)
            juego.actualizar_estado(contar_piezas, semilla)

            #if juego.vel_caida != intervalo_bajada:
                #intervalo_bajada = juego.vel_caida

            if juego.game_over:
                corriendo = False

            tiempo_ultimo_movimiento = ahora

        # tetris sin algoritmos            
        # aca va el codigo
        # ...

        interfaz.dibujar_gui() 
        pygame.display.update()
        reloj.tick(60)  # 60 FPS

    resultados = evaluar(juego, tiempos, contar_piezas)
    #print(resultados)
    pygame.quit()    

    #print(f"Piezas: {contar_piezas}, Algoritmo: {algoritmo}, tetrises: {juego.tetrises}")
    #print(f"Resultados: {resultados}")

    return resultados


# tetris sin algoritmos
"""    
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            # muevo la pieza con las teclas izq, der
            if evento.type == pygame.KEYDOWN:
                # si quieremos que acelere el tiempo podemos dejar que toque para abajo, sino lo sacamos
                if evento.key == pygame.K_DOWN:
                    juego.set_vel_caida("soft")
                    intervalo_bajada = juego.get_vel_caida()
                    juego.mover_si_valido(juego.pieza_actual,0,-1) 
                    
                if evento.key == pygame.K_LEFT:
                    juego.mover_si_valido(juego.pieza_actual,-1,0)
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
                if evento.key == pygame.K_RIGHT:
                    juego.mover_si_valido(juego.pieza_actual,1,0)
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)
                # si quiero rotar la pieza toco espacio
                if evento.key == pygame.K_SPACE:
                    juego.rotar_si_valido()
                    nueva_fantasma = juego.actualizar_pieza_fantasma()
                    interfaz.dibujar_pieza(nueva_fantasma, True)

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_DOWN:
                    juego.set_vel_caida()
                    intervalo_bajada = juego.get_vel_caida()
        """
from tetris import *
import pygame

class Interfaz:
    def __init__(self, tetris: Tetris, screen):
        self.tetris = tetris
        self.tamaño_bloque = self.tetris.tablero.bloque 
        self.screen = screen
        self.color = (0,0,0)


    def dibujar_gui(self):
        self.screen.fill(self.color)
        self.dibujar_tablero()
        self.dibujar_pieza(self.tetris.pieza_actual, False)
        self.dibujar_pieza(self.tetris.pieza_fantasma, True)
        self.dibujar_cuadricula()
        pygame.display.update()
        

    def dibujar_cuadricula(self):
        filas = self.tetris.tablero.filas
        columnas = self.tetris.tablero.columnas
        for fila in range(filas): # extremos de la linea horizontal
            pygame.draw.line(self.screen,(40,40,40), (0, fila * self.tamaño_bloque), (columnas * self.tamaño_bloque, filas * self.tamaño_bloque))
        for columna in range (columnas):
            pygame.draw.line(self.screen, (40,40,40), (columna * self.tamaño_bloque, 0), (columna * self.tamaño_bloque, filas * self.tamaño_bloque))

    def dibujar_tablero(self):
        for y, fila in enumerate(self.tetris.tablero.estado_actual):  # BIEN: dibuja el estado actual que tiene las piezas fijadas
            for x, color in enumerate(fila):
                rect = pygame.Rect(x * self.tamaño_bloque, y * self.tamaño_bloque, self.tamaño_bloque, self.tamaño_bloque)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (50, 50, 50), rect, width=1)

    '''def dibujar_tablero(self):
        for y, fila in enumerate(self.tetris.tablero.generarMatriz()):
            for x, color in enumerate(fila):
                rect = pygame.Rect(x * self.tamaño_bloque, y * self.tamaño_bloque, self.tamaño_bloque, self.tamaño_bloque)
                
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen,(50,50,50), rect, width=1)'''

    def dibujar_pieza(self, pieza: Tetromino, fantasma: bool):
        for x, y in pieza.obtenerFormaActual():
            px = x * self.tamaño_bloque  # coordenadas en píxeles
            py = y * self.tamaño_bloque

            if fantasma:
                pygame.draw.rect(self.screen, (200, 200, 255), (px, py, self.tamaño_bloque, self.tamaño_bloque), width=2)
            else:
                pygame.draw.rect(self.screen, pieza.color, (px, py, self.tamaño_bloque, self.tamaño_bloque))

    '''def dibujar_pieza(self, pieza: Tetromino, fantasma: bool):
        
        for x, y in pieza.forma:
            px = x * self.tamaño_bloque #pasamos las coordenadas a pixeles
            py = y * self.tamaño_bloque

            
            if fantasma:
                pygame.draw.rect(self.screen, (200, 200, 255), (px, py, self.tamaño_bloque, self.tamaño_bloque), width = 2)
            else:
                pygame.draw.rect(self.screen, pieza.color, (px, py, self.tamaño_bloque, self.tamaño_bloque))'''

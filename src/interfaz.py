from tetris import *
import pygame

class Interfaz:
    def __init__(self, tetris: Tetris, screen):
        self.tetris = tetris
        self.tamaño_bloque = self.tetris.tablero.bloque 
        self.screen = screen
        self.color = (68,68,68)


    def dibujar_gui(self):
        self.screen.fill(self.color)
        self.dibujar_tablero()
        self.dibujar_pieza(self.tetris.pieza_actual, False)
        self.dibujar_pieza(self.tetris.pieza_fantasma, True)
        self.dibujar_panel()
        #self.dibujar_cuadricula()
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
                pygame.draw.rect(self.screen, (68,68,68), rect, 1)

    def dibujar_pieza(self, pieza: Tetromino, fantasma: bool):
        for x, y in pieza.obtener_forma_actual():
            px = x * self.tamaño_bloque  # coordenadas en píxeles
            py = y * self.tamaño_bloque

            if fantasma:
                pygame.draw.rect(self.screen, (200, 200, 255), (px, py, self.tamaño_bloque, self.tamaño_bloque), width=2)
            else:
                self.diseño_pieza(px,py,pieza)
                
    def dibujar_panel(self):
        font = pygame.font.Font("Audiowide-Regular.ttf", 15)
        #font = pygame.font.SysFont("Arial", 20)
        panel_x = 300
        bloque_size = self.tamaño_bloque

        pygame.draw.line(self.screen, (80,80,80), (300, 0), (300, 800), 2)

        # ---------- TÍTULO PRÓXIMA PIEZA ----------
        texto = font.render("Próxima pieza", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 40, 24))

        pieza_siguiente = Tetromino(self.tetris.next_queue[0])
        pos_pieza = pieza_siguiente.obtener_forma_actual()

        # ---------- CENTRAR PIEZA ----------
        min_x = min(x for x, y in pos_pieza)
        max_x = max(x for x, y in pos_pieza)
        min_y = min(y for x, y in pos_pieza)
        max_y = max(y for x, y in pos_pieza)

        ancho = max_x - min_x 
        alto = max_y - min_y + 1

        cx = panel_x + (5 * bloque_size - ancho * bloque_size) // 2
        cy = 60 + (4 * bloque_size - alto * bloque_size) // 2

        # ---------- DIBUJAR PIEZA ----------
        for x, y in pos_pieza:
            px = cx + (x - min_x) * bloque_size
            py = cy + (y - min_y) * bloque_size
            
            self.diseño_pieza(px,py,pieza_siguiente)


        # ---------- LÍNEA DIVISORIA ----------
        pygame.draw.line(self.screen, (200, 200, 200), (panel_x, 190), (panel_x + 200, 190), 1)

        # ---------- TIEMPO ----------
        #pygame.draw.line(self.screen, (200, 200, 200), (panel_x, 310), (panel_x + 150, 310), 1)
        # Dibujar tiempo transcurrido
        tiempo_transcurrido = (pygame.time.get_ticks() - self.tetris.tiempo_inicio) // 1000
        texto_tiempo = font.render(f"Tiempo: {tiempo_transcurrido}s", True, (255, 255, 255))
        self.screen.blit(texto_tiempo, (panel_x + 10, 220)) 

        # ---------- PUNTUACIÓN ----------
        texto = font.render(f"Puntuación: {self.tetris.puntaje}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 260))

        # ---------- NIVEL ----------
        texto = font.render(f"Nivel: {self.tetris.nivel}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 300))

        # ---------- LÍNEAS ELIMINADAS ----------
        texto = font.render(f"Líneas: {self.tetris.lineas_eliminadas}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 340))

        # ---------- SINGLES ----------
        texto = font.render(f"Singles: {self.tetris.singles}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 380))

        # ---------- DOUBLES ----------
        texto = font.render(f"Doubles: {self.tetris.doubles}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 420))

        # ---------- TRIPLES ----------
        texto = font.render(f"Triples: {self.tetris.triples}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 460))

        # ---------- TETRIS ----------
        texto = font.render(f"Tetrises: {self.tetris.tetrises}", True, (255, 255, 255))
        self.screen.blit(texto, (panel_x + 10, 500))
    
    def diseño_pieza(self, px: int, py: int, pieza: Tetromino):
        sombra = (max(pieza.color[0] - 40, 0), max(pieza.color[1] - 40, 0), max(pieza.color[2] - 40, 0))
        brillo = (min(pieza.color[0] + 40, 255), min(pieza.color[1] + 40, 255), min(pieza.color[2] + 40, 255))

        pygame.draw.rect(self.screen, pieza.color, (px, py, self.tamaño_bloque, self.tamaño_bloque))
        pygame.draw.rect(self.screen, (200, 200, 200), (px, py, self.tamaño_bloque, self.tamaño_bloque), 1)  # Borde

        # Brillo arriba e izquierda
        pygame.draw.line(self.screen, brillo, (px, py), (px + self.tamaño_bloque, py), 2)
        pygame.draw.line(self.screen, brillo, (px, py), (px, py + self.tamaño_bloque), 2)

        # Sombra abajo y derecha
        pygame.draw.line(self.screen, sombra, (px, py + self.tamaño_bloque - 1), (px + self.tamaño_bloque, py + self.tamaño_bloque - 1), 2)
        pygame.draw.line(self.screen, sombra, (px + self.tamaño_bloque - 1, py), (px + self.tamaño_bloque - 1, py + self.tamaño_bloque), 2)


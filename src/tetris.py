from typing import List
from tablero import *
from tetromino import *
from piezas import *
import random


class Tetris:
    def __init__(self, tablero: Tablero, bag: List[Tetromino] = ["O", "I", "T", "L", "J", "S", "Z"]):
        self.tiempo_inicio = None
        self.tablero = tablero
        self.pieza_actual = None
        self.pieza_fantasma = None
        self.bag = bag
        self.next_queue = []
        self.vel_caida = None
        self.nivel = 1
        self.lineas_eliminadas = 0
        self.puntaje = 0
        #self.tetrises = 0
        #self.tspins = 0
        #self.b2b = 0
        self.game_over = False

    def actualizar_estado(self): #actualiza nivel, puntuacion, lineas eliminadas,...
        if not self.mover_si_valido(self.pieza_actual,0,1):
            self.tablero.fijar_pieza(self.pieza_actual)
            lineas = self.tablero.eliminar_lineas()
            if lineas != 0:
                self.lineas_eliminadas += lineas
                self.actualizar_puntos()
                self.actualizar_nivel()
            
            if not self.is_game_over():
                self.agregar_pieza_nueva()
            else:
                self.game_over = True

    # Operaciones con piezas ---------------------------------------------------
    def mover_si_valido(self, pieza: Tetromino, dx, dy):
        pieza.mover(dx, dy)
        if self.tablero.hay_colision(pieza):
            pieza.mover(-dx, -dy)
            return False
        return True
    
    def rotar_si_valido(self):
        self.pieza_actual.rotar()
        for x, y in self.pieza_actual.obtener_forma_actual():
            # Verificamos si está fuera de los límites del tablero
            if x < 0 or x >= self.tablero.columnas or y >= self.tablero.filas:
                self.pieza_actual.rotacion_inversa()
                return False
            # Verificamos si choca con otra pieza ya colocada
            if self.tablero.estado_actual[y][x] != 0:
                self.pieza_actual.rotacion_inversa()
                return False
        return True
    
    """def obtener_posiciones_pieza(self, pieza: Tetromino):
        posiciones = []
        forma = pieza.obtener_forma_actual()
        for i, fila in enumerate(forma):
            for j, celda in enumerate(fila):
                if celda == 'O':
                    posiciones.append((pieza.x + j, pieza.y + i))
        return posiciones"""
    
    # Generar piezas (actual y fantasma) ----------------------------------------
    def generar_cola(self): 
        nums = random.sample(range(0,7),7) 
        for i in range(7):
            self.next_queue.append(self.bag[nums[i]])
    
    def agregar_pieza_nueva(self):
        if len(self.next_queue) < 2:
            self.generar_cola()
        
        self.pieza_actual = Tetromino(self.next_queue.pop(0))
        self.actualizar_pieza_fantasma()
    
    def actualizar_pieza_fantasma(self):
        self.pieza_fantasma = self.pieza_actual.copy()

        while self.mover_si_valido(self.pieza_fantasma, 0, 1):
            continue
        return self.pieza_fantasma
    
    # Caida Pieza ---------------------------------------------------
    def get_vel_caida(self):
        return self.vel_caida
    
    def set_vel_caida(self, tipo: str = None):
        if tipo is None:
            self.vel_caida = ((0.8 - ((self.nivel - 1) * 0.007)) ** (self.nivel - 1)) * 1000
        
        if tipo == "soft":
            self.vel_caida = self.vel_caida / 20000

        if tipo == "hard":
            self.vel_caida = 0.0001

    # Niveles -------------------------------------------------------
    def get_nivel(self):
        return self.nivel
    
    def actualizar_nivel(self):
        if self.lineas_eliminadas == 10:
            self.nivel += 1
            self.lineas_eliminadas = 0

    # Puntaje -------------------------------------------------------
    def actualizar_puntos(self):
        if self.lineas_eliminadas == 1:
            self.puntaje += 100
        elif self.lineas_eliminadas == 2:
            self.puntaje += 200
        elif self.lineas_eliminadas == 3:
            self.puntaje += 400
        elif self.lineas_eliminadas == 4:
            self.puntaje += 800

    #Game Over --------------------------------------------------------
    def is_game_over(self):
        for _, y in self.pieza_actual.obtener_forma_actual():
            if y < 0:
                return True
        return False


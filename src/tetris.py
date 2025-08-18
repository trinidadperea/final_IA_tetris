from typing import List
from tablero import *
from tetromino import *
from piezas import *
import random
import numpy as np


class Tetris:
    def __init__(self, tablero: Tablero):
        self.tiempo_inicio = None
        self.tablero = tablero
        self.pieza_actual = None
        self.pieza_fantasma = None
        self.bag = ["O","I", "T", "L", "J", "S", "Z"]
        self.next_queue = []
        self.vel_caida = None
        self.nivel = None
        self.lineas_eliminadas = 0
        self.lineas_nivel = 0
        self.puntaje = 0
        self.singles = 0
        self.doubles = 0
        self.triples = 0
        self.tetrises = 0
        self.game_over = False
        self.nueva_pieza = True


    def actualizar_estado(self, num_iter, semilla): #actualiza nivel, puntuacion, lineas eliminadas,...

        if not self.mover_si_valido(self.pieza_actual,0,1, "vertical"):
            
            self.tablero.fijar_pieza(self.pieza_actual)
            lineas = self.tablero.eliminar_lineas()
            if lineas != 0:
                self.actualizar_lineas(lineas)
                self.actualizar_puntos(lineas)
                
            if not self.is_game_over():
                self.agregar_pieza_nueva(num_iter, semilla)
                self.nueva_pieza = True
            else:
                self.game_over = True
    
    def actualizar_estado_simulacion(self): #actualiza nivel, puntuacion, lineas eliminadas,...

        if not self.mover_si_valido(self.pieza_actual,0,1, "vertical"):
            
            self.tablero.fijar_pieza(self.pieza_actual)
            lineas = self.tablero.eliminar_lineas()
            if lineas != 0:
                self.actualizar_lineas(lineas)
                self.actualizar_puntos(lineas)
                
            
    
    # Operaciones con piezas ---------------------------------------------------
    def mover_si_valido(self, pieza: Tetromino, dx, dy, mov):
        pieza.mover(dx, dy)
        if self.tablero.hay_colision(pieza, mov):
            pieza.mover(-dx, -dy)
            return False
        return True
    
    def rotar_si_valido(self):
        self.pieza_actual.rotar()
        for x, y in self.pieza_actual.obtener_forma_actual():
            if x < 0 or x >= self.tablero.columnas or y >= self.tablero.filas:
                self.pieza_actual.rotacion_inversa()
                return False
            if y >= 0 and self.tablero.estado_actual[y][x] != 0:
                self.pieza_actual.rotacion_inversa()
                return False
        return True
        
    # Generar piezas (actual y fantasma) ----------------------------------------
    def generar_cola(self, num_iter, semilla): 
        #manejo la cola de manera random para utilizar la semilla
        random.seed(semilla + num_iter)
        nums = random.sample(range(0,7),7) 
        for i in range(7):
            self.next_queue.append(self.bag[nums[i]])
    
    # funcion para manejo de semillas 
    #def generar_semilla(self, seed):
        #random.seed(seed)

    def agregar_pieza_nueva(self, num_iter, semilla):
        if len(self.next_queue) < 2:
            self.generar_cola(num_iter, semilla)
        
        self.pieza_actual = Tetromino(self.next_queue.pop(0))
        self.actualizar_pieza_fantasma()
    
    def actualizar_pieza_fantasma(self):
        self.pieza_fantasma = self.pieza_actual.copy()

        while self.mover_si_valido(self.pieza_fantasma, 0, 1, "vertical"):
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
    
    def set_nivel(self, nivel: int):
        self.nivel = nivel

    def actualizar_lineas(self, lineas:int):
        total_lineas = self.lineas_nivel + lineas
        
        if total_lineas >= 10:
            self.actualizar_nivel()
            self.lineas_nivel = total_lineas - 10
        else:     
            self.lineas_nivel += lineas      
        
        self.lineas_eliminadas += lineas

    def actualizar_nivel(self):
        self.nivel += 1
        self.set_vel_caida()
    
    # Puntaje -------------------------------------------------------
    def actualizar_puntos(self, lineas):
            if lineas < 4:
                if lineas == 1:
                    self.puntaje += (100 * self.nivel)
                    self.singles += 1
                elif lineas == 2:
                    self.puntaje += (200 * self.nivel)
                    self.doubles += 1
                elif lineas == 3:
                    self.puntaje += (400 * self.nivel)
                    self.triples += 1
                return
            else: 
                self.puntaje += (800 * self.nivel)
                self.tetrises += 1
                self.actualizar_puntos(lineas - 4)
    
    #Game Over --------------------------------------------------------
    def is_game_over(self):
        for _, y in self.pieza_actual.obtener_forma_actual():
            if y < 0:
                return True
        return False
    
    # Copiar juego -----------------------------------------------
    def copy(self): #copiamos los objetos por separado, sino se duplican las piezas
        
        # copia del tablero --
        copia = Tetris(self.tablero.copy())

        # copia pieza actual ------
        copia.pieza_actual = self.pieza_actual.copy()
        
        # copia pieza fantasma -----
        copia.pieza_fantasma = self.pieza_fantasma.copy()
        
        # -------------
        copia.tiempo_inicio = self.tiempo_inicio
        copia.bag = self.bag[:]
        copia.next_queue = self.next_queue[:]

        copia.vel_caida = self.vel_caida
        copia.nivel = self.nivel
        copia.lineas_eliminadas = self.lineas_eliminadas
        copia.puntaje = self.puntaje
        copia.singles = self.singles
        copia.doubles = self.doubles 
        copia.triples = self.triples
        copia.tetrises = self.tetrises
        copia.game_over = self.game_over
        return copia
    
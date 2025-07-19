from typing import List
from tablero import *
from tetromino import *
from piezas import *
import random


class Tetris:
    def __init__(self, tablero: Tablero, bag: List[Tetromino] = ["O", "I", "T", "L", "J", "S", "Z"]):
        self.tablero = tablero
        self.puntaje = 0
        self.time = 0 #tiempo de juego
        self.lineasEliminadas = 0
        self.nivel = 1
        self.tetrises = 0
        self.tspins = 0
        self.b2b = 0
        self.vel_caida = 0.800
        self.temporizador = 0
        self.gameOver = False
        self.bag = bag
        #self.pieza_actual = self.generarPieza() #pieza actual
        self.pieza_actual = None
        self.pieza_fantasma = None
        self.next_queue = []

    def actualizar_estado(self): #actualiza nivel, puntuacion, lineas eliminadas,...
        self.generar_cola()
        self.pieza_actual = Tetromino(self.next_queue.pop(0))
        self.actualizar_pieza_fantasma()
            

    def actualizar_pieza_fantasma(self): #hay que llamarlo cada vez que se rote, mueva o cambie de pieza
        self.pieza_fantasma = self.pieza_actual.copy()

        while not self.tablero.hay_colision(self.pieza_fantasma):
            self.pieza_fantasma.y += 1
            
        return self.pieza_fantasma
    
    def moverPieza(self):
        # roto pieza temporalmente
        pieza_temp = self.pieza_actual.copy()
        pieza_temp.rotar()

        posiciones = self.obtener_posiciones_pieza(pieza_temp)

        if self.tablero.es_valida(posiciones):
            # solo si se puede la roto
            self.pieza_actual.rotar()
            self.actualizar_pieza_fantasma()
            return True
        else:
            return False
        
    def obtener_posiciones_pieza(self, pieza: Tetromino):
        posiciones = []
        forma = pieza.obtenerFormaActual()
        for i, fila in enumerate(forma):
            for j, celda in enumerate(fila):
                if celda == 'O':
                    posiciones.append((pieza.x + j, pieza.y + i))
        return posiciones
    
    """def bajar_pieza(self, pieza: Tetromino):
        pieza.y += 1
        pieza.forma()"""

    
    def generar_cola(self): #implementar control de generacion de queue
        for i in range(6):
            num = random.randint(0,6)
            self.next_queue.append(self.bag[num])

    def agregar_pieza_nueva(self):
        tipos = list(piezas.PIEZAS.keys())
        nuevo_tipo = random.choice(tipos)
        return Tetromino(nuevo_tipo)

    def get_vel_caida(self):
        return self.vel_caida
    
    def set_vel_caida(self):
        self.vel_caida = (0.8 - ((self.nivel - 1) * 0.007)) ^ (self.nivel - 1)

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        self.nivel = nivel


    def esJugadaEspecial(self) -> bool:
        pass

    def determinarPuntosJE(self,lineas_borradas) -> int:
        if lineas_borradas == 1:
            self.puntaje += 100
        elif lineas_borradas == 2:
            self.puntaje += 200
        elif lineas_borradas == 3:
            self.puntaje += 400
        elif lineas_borradas == 4:
            self.puntaje += 800



    def manejarEventos(self):
        pass


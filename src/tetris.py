from typing import List
from tablero import *
from tetromino import *
import random
import piezas

class Tetris:
    def __init__(self, tablero: Tablero, bag: List[Tetromino]):
        self.tablero = tablero
        self.puntuacion = 0
        self.time = 0 #tiempo de juego
        self.lineasEliminadas = 0
        self.nivel = 1
        self.tetrises = 0
        self.tspins = 0
        self.b2b = 0
        self.velCaida = 1 #establecer
        self.temporizador = 0
        self.gameOver = False
        self.bag = bag
        #self.pieza_actual = self.generarPieza() #pieza actual
        self.pieza_actual = None
        #self.next_queue = self.generarCola()

    def actualizarEstado(self): #actualiza nivel, puntuacion, lineas eliminadas,...
        pass

    def piezaFantasma(self): #mostrar pieza fantasma en el tablero
        pass

    def moverPieza(self):
        # roto pieza temporalmente
        pieza_temp = self.pieza_actual.copy()
        pieza_temp.rotar()

        posiciones = self.obtener_posiciones_pieza(pieza_temp)

        if self.tablero.es_valida(posiciones):
            # solo si se puede la roto
            self.pieza_actual.rotar()
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

    def esJugadaEspecial(self) -> bool:
        pass

    def determinarPuntosJE(self) -> int:
        pass

    def determinarNextQueue(self):
        pass

    def actualizarVelCaida(self):
        pass

    def manejarEventos(self):
        pass


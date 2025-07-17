from typing import List
from tablero import *
from tetromino import *



class Tetris:
    def __init__(self, tablero: Tablero, bag: List[Tetromino]):
        self.tablero = tablero
        self.puntuacion = 0
        self.time #tiempo de juego
        self.lineasEliminadas = 0
        self.nivel = 1
        self.tetrises = 0
        self.tspins = 0
        self.b2b = 0
        self.velCaida #establecer
        self.temporizador
        self.gameOver = False

    def actualizarEstado(self): #actualiza nivel, puntuacion, lineas eliminadas,...
        pass

    def piezaFantasma(self): #mostrar pieza fantasma en el tablero
        pass

    def rotarPieza(self, pieza: Tetromino):
        pass

    def moverPieza(self, pieza: Tetromino):
        pass 

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


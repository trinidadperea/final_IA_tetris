from typing import List
from tetromino import *

class Tablero:
    def __init__(self, filas: int, columnas:int, bloque: int):
        self.filas = filas
        self.columnas = columnas
        self.bloque = bloque #pixeles
        self.estado_actual = self.generarMatriz()
    
    def generarMatriz(self):
        # Creo matriz vacía
        return [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

    def es_valida(self, posiciones: list) -> bool:
        for x, y in posiciones:
            if x < 0 or x >= self.columnas or y < 0 or y >= self.filas:
                return False
            if self.estado_actual[y][x] != 0:
                return False
        return True
    
    def actualizar(self): #agrega piezas
        pass

    def mostrarNextQueue(self, listaPiezas: List[Tetromino]):
        pass

    def eliminarLineas(self):
        pass

    def hay_colision(self, pieza: Tetromino) -> bool:
        for fila in range(len(pieza.forma)):
            for col in range(len(pieza.forma[0])):
                if pieza.forma[fila][col] == 0:
                    continue

                x = pieza.x + col
                y = pieza.y + fila

                # Fuera de los límites del tablero
                if x < 0 or x >= self.columnas or y >= self.filas:
                    return True

                # Colisión con otro bloque en el tablero
                if y >= 0 and self.estado_actual[y][x] != 0:
                    return True

        return False


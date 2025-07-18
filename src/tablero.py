from typing import List
from tetromino import *

class Tablero:
    def __init__(self):
        self.filas = 20
        self.columnas = 10
        self.estadoActual = self.generarMatriz()
    
    def generarMatriz(self):
        # Creo matriz vacía
        return [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

    def es_valida(self, posiciones: list) -> bool:
        for x, y in posiciones:
            if x < 0 or x >= self.columnas or y < 0 or y >= self.filas:
                return False
            if self.estadoActual[y][x] != 0:
                return False
        return True
    
    def generar(self): 
        pass

    def actualizar(self): #agrega piezas
        pass

    def mostrarNextQueue(self, listaPiezas: List[Tetromino]):
        pass

    def eliminarLineas(self):
        pass

    def hayColisiones(self) -> bool:
        pass

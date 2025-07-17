from typing import List
from tetromino import *

class Tablero:
    def __init__(self):
        self.filas = 20
        self.columnas = 10
        self.estadoActual = self.generarMatriz()
    
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

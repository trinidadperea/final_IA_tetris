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
        nuevas_filas = []
        lineas_completas = 0
        
        for fila in self.estado_actual:
            if 0 not in fila:  # fila completa, sin ningún 0
                lineas_completas += 1
            else:
                nuevas_filas.append(fila)
        
        # Por cada línea completa, agrego una fila vacía arriba
        for _ in range(lineas_completas):
            nuevas_filas.insert(0, [0] * self.columnas)
        
        self.estado_actual = nuevas_filas
        
        return lineas_completas

    def hay_colision(self, pieza: Tetromino) -> bool:
        # dir = 0 -> vertical
        # dir = 1 -> derecha
        # dir = -1 -> izquierda
        for offset_x, offset_y in pieza.obtenerFormaActual():

            x = offset_x
            y = offset_y + 1

            if x < 0 or x >= self.columnas or y < 0 or y >= self.filas:
                return True
            
            # Colisión con otro bloque
            if self.estado_actual[y][x] != 0:
                return True
            
        return False

    def fijar_pieza(self, pieza: Tetromino):
        coilision_techo = False
        for x, y in pieza.obtenerFormaActual():
            if 0 <= y < self.filas and 0 <= x < self.columnas:
                self.estado_actual[y][x] = pieza.color
                colision_techo = False
            if y < 0:
                colision_techo = True
        return self.eliminarLineas(), colision_techo
    
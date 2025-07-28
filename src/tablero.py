from typing import List
from tetromino import *


class Tablero:
    def __init__(self, filas: int, columnas:int, bloque: int):
        self.filas = filas
        self.columnas = columnas
        self.bloque = bloque #pixeles
        self.cant_huecos = 0
        self.estado_actual = None
    
    def generar_matriz(self):
        return [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

    def eliminar_lineas(self):
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

    def hay_colision(self, pieza: Tetromino, mov: str) -> bool:
        for x, y in pieza.obtener_forma_actual():
                        
            if (x < 0 or x >= self.columnas) and mov == "horizontal": 
                print(f"colisión borde horizontal en x={x}, columna={pieza.x}, pieza={pieza.pieza}, rot={pieza.rotacion}")
                return True
            
            if (y < 0 or y >= self.filas) and mov == "vertical":
                #print(f"hay colision {mov}, x = {x}, y = {y}")
                return True
            
            # Colisión con otro bloque
            if self.estado_actual[y][x] != 0:
                return True
        return False
    
    def fijar_pieza(self, pieza: Tetromino):
        for x, y in pieza.obtener_forma_actual():
            if 0 <= y < self.filas and 0 <= x < self.columnas:
                self.estado_actual[y][x] = pieza.color
        
        self.set_huecos()
    
    def contar_huecos(self):
        huecos = 0
        for x in range(self.columnas):
            colision = False
            for y in range(self.filas):
                if self.estado_actual[y][x] != 0:
                    colision = True
                elif colision:
                    huecos += 1
        return huecos
    
    def get_huecos(self):
        return self.cant_huecos
    
    def set_huecos(self):
        self.cant_huecos = self.contar_huecos()

    # Copiar tablero -----------------------------------------------
    def copy(self):
        copia = Tablero(self.filas, self.columnas, self.bloque)
        copia.cant_huecos = self.get_huecos()
        copia.estado_actual = [fila[:] for fila in self.estado_actual]
        return copia
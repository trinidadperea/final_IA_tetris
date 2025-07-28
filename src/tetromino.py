from typing import List
import piezas

class Tetromino():
    def __init__ (self, pieza: str):
        self.pieza = pieza
        self.rotacion = 0
        (self.x, self.y) = piezas.OFFSET[self.pieza]
        self.formas = piezas.PIEZAS[self.pieza]
        self.color = piezas.COLORES[self.pieza]
    
    # prop pieza ------------------------------------------------------
    def obtener_forma_actual(self):
        forma_relativa = self.formas[self.rotacion]
        return [(x + self.x, y + self.y) for (x, y) in forma_relativa]
    
    def get_pieza(self):
        return self.pieza

    def get_rotacion(self):
        return self.rotacion
    
    """def set_posicion(self, x:int, y:int):
        self.x = x
        self.y = y"""
    
    # Op pieza--------------------------------------------------------
    def rotar(self):
        self.rotacion = (self.rotacion + 1) % len(self.formas)
        #print(f"rotacion= {self.rotacion}")
    
    def rotacion_inversa(self):
        self.rotacion = (self.rotacion - 1) % len(self.formas)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def copy(self):
        copia = Tetromino(self.pieza)
        copia.x = self.x
        copia.y = self.y
        copia.rotacion = self.rotacion
        copia.formas = self.formas
        copia.color = self.color
        return copia

    def imprimir_pieza(self):
        formaActual = self.forma[self.rotacion]
        for fila in formaActual:
            print(fila)

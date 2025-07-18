from typing import List
import piezas

class Tetromino():
    def __init__ (self,pieza: str, x: int = 5, y: int = 0):
        self.pieza = pieza.upper()
        self.rotacion = 0
        self.x = x
        self.y = y
        self.formas = piezas.PIEZAS[self.pieza]
    
    def obtenerFormaActual(self):
        return self.formas[self.rotacion]
    
    def rotar(self):
        self.rotacion = (self.rotacion + 1) % len(self.formas)
    
    def rotacionInversa(self):
        self.rotacion = (self.rotacion - 1) % len(self.formas)
    
    def getPieza(self):
        return self.pieza

    def getRotacion(self):
        return self.rotacion
    
    def setPosicion(self, x:int, y:int):
        self.x = x
        self.y = y

    def copy(self):
        copia = Tetromino(self.pieza, self.x, self.y)
        copia.rotacion = self.rotacion
        return copia

    def imprimir_pieza(self):
        formaActual = self.formas[self.rotacion]
        for fila in formaActual:
            print(fila)


    '''   
    #orientaciones = {"N", "S", "E", "W"}
    piezas = ["O", "I", "T", "L", "J", "S", "Z"]
    
    def __init__(self, pieza : chr):
        self.orientacion = "N" # por defecto la orientacion es north facing
        self.pieza = pieza

    def getPieza(self): #devuelve el tetrimino segun la letra 
        return self.pieza

    def generarPieza(self, pieza: chr): #devuelve la pieza 2d con la orientación correspondiente
        pass
    
    def getOrientación(self):
        return self.orientacion
    
    def setOrientacion(self, orientacion: chr):
        self.orientacion = orientacion
    '''
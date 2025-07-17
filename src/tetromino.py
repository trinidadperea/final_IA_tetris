from typing import List

class Tetromino():
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
from typing import List
import piezas

class Tetromino():
    def __init__ (self, pieza: str):
        self.pieza = pieza.upper()
        self.rotacion = 0
        (self.x, self.y) = piezas.OFFSET[self.pieza]
        self.formas = piezas.PIEZAS[self.pieza]
        #self.forma = [(x + self.x, y + self.y) for (x, y) in self.formas[self.rotacion]]
        self.color = piezas.COLORES[self.pieza]
    
    """def forma(self):
        formas = piezas.PIEZAS[self.pieza]
        return [(x + self.x, y + self.y) for (x, y) in formas[self.rotacion]] """

    def obtener_forma_actual(self):
        forma_relativa = self.formas[self.rotacion]
        return [(x + self.x, y + self.y) for (x, y) in forma_relativa]
    
    """
    def rotar_si_valido(self, tablero):
        self.rotar()
        for x, y in self.obtenerFormaActual():
            # Verificamos si está fuera de los límites del tablero
            if x < 0 or x >= tablero.columnas or y >= tablero.filas:
                self.rotacionInversa()
                return False
            # Verificamos si choca con otra pieza ya colocada
            if tablero.estadoActual[y][x] != 0:
                self.rotacionInversa()
                return False
        return True
    """
    
    
    def rotar(self):
        self.rotacion = (self.rotacion + 1) % len(self.formas)
    
    def rotacion_inversa(self):
        self.rotacion = (self.rotacion - 1) % len(self.formas)
    
    def getPieza(self):
        return self.pieza

    def getRotacion(self):
        return self.rotacion
    
    def setPosicion(self, x:int, y:int):
        self.x = x
        self.y = y

    def copy(self):
        copia = Tetromino(self.pieza)
        copia.x = self.x
        copia.y = self.y
        copia.rotacion = self.rotacion
        return copia

    def imprimir_pieza(self):
        formaActual = self.forma[self.rotacion]
        for fila in formaActual:
            print(fila)

    def mover(self, dx, dy):
        # Intentar mover la pieza
        self.x += dx
        self.y += dy


    """ def mover_si_valido(self, dx, dy, tablero):
        # Intentar mover la pieza
        self.x += dx
        self.y += dy

        # Verificar si hay colisión con el tablero
        for x, y in self.obtenerFormaActual():
            if x < 0 or x >= tablero.columnas or y >= tablero.filas or y < 0:
                # movimiento invalido
                self.x -= dx
                self.y -= dy
                return False
            if tablero.estado_actual[y][x] != 0:
                # Colisión con bloque ya fijo
                self.x -= dx
                self.y -= dy
                return False

        # Movimiento válido
        return True """
    

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
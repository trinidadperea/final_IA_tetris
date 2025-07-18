# main.py

from tetris import Tetris
from tetromino import Tetromino
from tablero import Tablero

def main():
    pass

if __name__ == "__main__":
    main()


# rotar pieza probando
''' 
def main():
    # Crear el tablero
    tablero = Tablero()
    tablero.estadoActual = tablero.generarMatriz()  # Matriz vacía (todo ceros)

    # Crear instancia de Tetris con el tablero y bag vacío (por ahora)
    juego = Tetris(tablero, [])

    # Crear y asignar una pieza 'I'
    juego.pieza_actual = Tetromino('I')

    print("Forma inicial:")
    juego.pieza_actual.imprimir_pieza()

    # Intentar rotar la pieza
    if juego.moverPieza():
        print("Forma luego de rotar:")
        juego.pieza_actual.imprimir_pieza()
    else:
        print("Rotación inválida, no se rotó la pieza.")

if __name__ == "__main__":
    main() '''


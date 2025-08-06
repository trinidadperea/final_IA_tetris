from busqueda_local import *
from tetris import *
from tablero import *


def evaluar(juego: Tetris, lista_tiempos):

    juego = juego.copy()

    tiempo_decision = sum(lista_tiempos) / len(lista_tiempos)
    puntaje = juego.puntaje
    lineas_eliminadas = juego.lineas_eliminadas
    altura_max = juego.tablero.calcular_altura()
    huecos = juego.tablero.contar_huecos()
    tetrises = juego.tetrises
    nival_alcanzado = juego.nivel

    return {
        "puntaje obtenido": puntaje,
        "lineas eliminadas": lineas_eliminadas,
        "altura maxima": altura_max,
        "cantidad de huecos": huecos,
        "cantidad de tetrises": tetrises,
        "nivel alcanzado": nival_alcanzado,
        "tiempo promedio toma decision": tiempo_decision
    }



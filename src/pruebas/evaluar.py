from busqueda_local import *
from tetris import *
from tablero import *

def evaluar(juego: Tetris, lista_tiempos, piezas):

    #juego = juego.copy()

    piezas_totales = piezas
    puntaje = juego.puntaje
    tiempo_decision = sum(lista_tiempos) / len(lista_tiempos)
    lineas_eliminadas = juego.lineas_eliminadas
    altura_max = juego.tablero.calcular_altura()
    huecos = juego.tablero.contar_huecos()
    singles = juego.singles
    doubles = juego.doubles
    triples = juego.triples
    tetrises = juego.tetrises
    nivel_alcanzado = juego.nivel

    return {
        "piezas totales": piezas_totales,
        "puntaje obtenido": puntaje,
        "tiempo promedio toma decision": tiempo_decision,
        "lineas eliminadas": lineas_eliminadas,
        "altura maxima": altura_max,
        "cantidad de huecos": huecos,
        "singles": singles,
        "doubles": doubles, 
        "triples": triples,
        "tetrises": tetrises,
        "nivel alcanzado": nivel_alcanzado
    }



from tetris import * 

def heuristica(juego: Tetris):
    # Que valores deben tener los pesos para que la funcion me devuelva la mejor posición posible?? 
    
    peso_lineas = 0.76
    peso_altura = 0.8
    peso_hueco = 1.2
    peso_desnivel = 0.7

    lineas_eliminadas = juego.lineas_eliminadas
    puntaje = peso_lineas * lineas_eliminadas
    #print(f"lineas_eliminadas: {lineas_eliminadas}")
    #print(f"puntaje (peso_lineas * lineas_eliminadas): {puntaje}")

    #print(" ")

    # huecos
    cant_huecos = juego.tablero.get_huecos()
    
    puntaje -= peso_hueco * cant_huecos
    #print(f"Cantidad de huecos: {cant_huecos}")
    #print(f"puntaje = {puntaje}")

    #print("")

    # altura
    
    alturas_por_columnas = calcular_altura_por_columna(juego)
    altura_maxima = max(alturas_por_columnas)
    altura_minima = min(alturas_por_columnas)
    
    
    puntaje -= peso_altura * altura_maxima
    #print(f"alturas por columna = {alturas_por_columnas}")
    #print(f"altura_maxima: {altura_maxima}")
    #print(f"puntaje = {puntaje}")

    #print("")
        
    # desnivel 
    desnivel = calcular_desnivel(alturas_por_columnas)
    puntaje -= peso_desnivel * desnivel
    #print(f"desnivel = {desnivel}")
    #print(f"puntaje = {puntaje}")

    altura_prom = sum(alturas_por_columnas) / len(alturas_por_columnas)
    puntaje -= 0.8 * (altura_maxima - altura_prom)

    diferencia_altura = abs(altura_maxima - altura_minima)

    puntaje -= 0.8 * diferencia_altura

    return puntaje


def calcular_altura_por_columna(juego: Tetris):
    alturas = []
    columnas = juego.tablero.columnas
    filas = juego.tablero.filas
    
    for x in range(columnas):
        altura = 0
        for y in range(filas):
            if juego.tablero.estado_actual[y][x] == 0:
                altura += 1
            else:
                break
        alturas.append(filas - altura)
        
    return alturas

def calcular_desnivel(alturas): 
    desnivel = 0
    for i in range(len(alturas)-1):
        desnivel += abs(alturas[i] - alturas[i+1])

    return desnivel


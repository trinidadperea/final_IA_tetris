from tetris import * 

def heuristic(juego: Tetris):
    peso_altura = 0.5
    peso_hueco = 0.2
    peso_desnivel = 0.5
    limite_altura_maxima = 6
    
    # estado actual
    juego_copia = juego.copy() 
    
    # posible estado -------------------------------------------
    juego_copia.actualizar_estado()

    #Puntaje por líneas eliminadas
    puntaje = juego_copia.puntaje - juego.puntaje 

    # huecos
    cant_huecos = abs(calcular_huecos(juego) - calcular_huecos(juego_copia))
    puntaje -= peso_hueco * cant_huecos

    # altura
    alturas_por_columnas = calcular_altura_por_columna(juego)
    altura_maxima = max(alturas_por_columnas)

    if altura_maxima > limite_altura_maxima:
        nro_lineas = altura_maxima - limite_altura_maxima
        puntaje -= peso_altura * nro_lineas
    
    
    # desnivel 
    desnivel = calcular_desnivel(alturas_por_columnas)
    puntaje -= peso_desnivel * desnivel

    return puntaje

def calcular_huecos(juego: Tetris):
    pass

def calcular_altura_por_columna(juego: Tetris):
    alturas = []
    columnas = juego.tablero.columnas
    filas = juego.tablero.filas

    for x in range(columnas):
        for y in range(filas):
            if juego.tablero[x][y] == 0:
                altura += 1
            else:
                break
        
        alturas.append(columnas - altura)
        altura = 0
    
    return alturas

def calcular_desnivel(alturas): 
    desnivel = 0
    for i in range(len(alturas)-1):
        desnivel += abs(alturas[i] - alturas[i+1])

    return desnivel


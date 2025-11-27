from tetris import * 

def heuristica(juego: Tetris, algo = None):
    # Que valores deben tener los pesos para que la funcion me devuelva la mejor posición posible?? 
    #print("")
    #print(" heuristica")
    #print("")
    if algo == "GA":
        peso_lineas = 0.8
        peso_hueco = 3.5
        peso_desnivel = 0.5
        peso_altura_prom = 0.3
        
    else:
        peso_lineas = 3.5
        peso_hueco = 5
        peso_desnivel = 0.5
        peso_altura_prom = 2

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
    
    #puntaje -= peso_altura * altura_maxima
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
    puntaje -= peso_altura_prom * altura_prom
    #puntaje -= peso_altura_prom * (altura_maxima - altura_prom)
    #print(f"altura promedio = {altura_prom}")
    #print(f"puntaje = {puntaje}")

    #diferencia_altura = abs(altura_maxima - altura_minima)
    #puntaje -= 0.8 * diferencia_altura

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

def combinaciones_validas(juego:Tetris, algo = None):
    combinaciones = []
    for columna in range(juego.tablero.columnas):

        for rotacion in range(len(juego.pieza_actual.formas)):
            simulacion = juego.copy()
            #pieza = juego.pieza_actual.pieza
            
            while simulacion.pieza_actual.y < 0:
                simulacion.pieza_actual.mover(0,1)

            for _ in range(rotacion):
                if not simulacion.rotar_si_valido():
                    break
            else:
                if mover_a_columna(simulacion, columna):
                    bajar_pieza(simulacion)
                    rot = simulacion.pieza_actual.rotacion
                    pos_x = simulacion.pieza_actual.x
                    
                    simulacion.actualizar_estado_simulacion()
                    if algo == "GA":
                        puntaje = heuristica(simulacion, "GA")
                    else:
                        puntaje = heuristica(simulacion)
                    
                    combinaciones.append((pos_x,rot,puntaje))
    return combinaciones

def mover_a_columna(juego: Tetris, destino):
    x_act = juego.pieza_actual.x
    desplazamiento = destino - x_act

    if desplazamiento > 0:
        dx = 1
    else:
        dx = -1

    for _ in range(abs(desplazamiento)):
        #juego.tablero.bajar(juego.pieza_actual)
        if not juego.mover_si_valido(juego.pieza_actual,dx,0, "horizontal"):
            #print(f"No se pudo mover a columna {destino} con rotación {juego.pieza_actual.rotacion}")
            #print(f"posiciones: destino = {destino}, desplazamiento = {desplazamiento}, x actual = {x_act}, x = {juego.pieza_actual.x}, y = {juego.pieza_actual.y}")
            
            return False
        
    return True

def bajar_pieza(juego:Tetris):
    while juego.mover_si_valido(juego.pieza_actual, 0, 1, "vertical"):
            continue

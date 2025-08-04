from tetris import *
from busqueda_local.heuristica import * 


def genetico(juego:Tetris, iteraciones: int):

    # [(pos,rot,fit), ...]
    combinaciones = combinaciones_validas(juego)

    tamaño_poblacion = min(len(combinaciones), 20)
    
    # poblacion = {(pos,rot,fit), ...}
    poblacion = random.sample(combinaciones, tamaño_poblacion)

    # (pos,rot)
    #mejor_estado = mejor_fitness(poblacion)

    elite_size = int(tamaño_poblacion * 0.1)
    h_variation = []

    i = 0
    print(f"Iteraciones: {iteraciones}")
    while iteraciones > 0:
        # Selecciono los individuos mas aptos 
        # Devuelve un dict con los individuos mas aptos de cada grupo
        # [(p1,r1,f1),...]
        seleccion = seleccionar_individuos(poblacion)
        print(f"Individuos seleccionados: {seleccion}")
        # Genero la poblacion nueva haciendo cruce entre los mas aptos
        # [(p1,r1,f1),...]

        #nueva_poblacion = cruce(seleccion, combinaciones)
        #print(f"Nueva poblacion, cruce: {nueva_poblacion}")

        # [(p1,r1,f1),...]
        nueva_poblacion = mutacion(seleccion, juego.pieza_actual, combinaciones)
        print(f"Mutacion: {nueva_poblacion}")

        descendencia = sorted(nueva_poblacion, key=lambda x: x[2], reverse=True)[:len(nueva_poblacion) - elite_size]
        print(f"Descendencia: {descendencia}")

        elites = sorted(poblacion, key=lambda x: x[2], reverse=True)[:elite_size]
        print(f"Elites: {elites}")
        
        nueva_poblacion = elites + descendencia
        print(f"Nueva poblacion(elites + descendencia): {nueva_poblacion}")

        mejor_combinacion = mejor_fitness(nueva_poblacion)
        print(f"Mejor fitness: {mejor_combinacion}")

        h_variation.append(mejor_combinacion[:2])
        if mejor_combinacion[2] == 0:
            # return best_state, i, h_variation
            return mejor_combinacion[:2]
            # (pos,rot,fit)
        
        poblacion = nueva_poblacion
        iteraciones -= 1
        i += 1
        print("")
        print(f"Iteraciones: {iteraciones}")


    #return best_state, i, h_variation
    return mejor_combinacion[:2]
    # (pos,rot,fit)

# combinaciones = {(pos,rot,fit)}
def mejor_fitness(combinaciones: dict): #si varias tienen el mejor fitness se queda con la primera

    #sum_fitness = 0
    mejor_fitness = float("-inf")
    mejor_combinacion = None
    
    for (pos,rot,fit) in combinaciones:
        #sum_fitness += mejor_fitness

        if fit > mejor_fitness:
            mejor_combinacion = (pos,rot,fit)
            mejor_fitness = fit

    return mejor_combinacion


# Seleccionamos por metodo de torneo sencillo
# poblacion = (pos,rot,fit)
def seleccionar_individuos(poblacion):
    individuos = []

    # Determino el tamaño de los grupos
    if len(poblacion) % 2 == 0:
        n = 2
    else:
        n = 3

    print("AQUI")

    grupos = agrupar_random(poblacion,n)
    # [[(pos1,rot1,fit1), (pos2,rot2,fit2)], [(), ()],...]
    print("")
    print(f"grupos: {grupos}")

    # Se toma de cada grupo el individuo con mejor fitness
    for grupo in grupos:
        mejor_fitness = max(individuo[2] for individuo in grupo)
        
        mejor_ind = [individuo for individuo in grupo if individuo[2] == mejor_fitness]
        # mejor_ind = [(pos1,rot1,fit1), ...]

        if (len(mejor_ind)) > 1:

            k = random.randint(0,len(mejor_ind)-1)
            individuos.append(mejor_ind[k])            
            
        else:
            individuos.append(mejor_ind[0])
                
    return individuos
    # Devuelvo una lista (pos,rot,fit) con los mejores individuos seleccionados de cada grupo 

def agrupar_random(poblacion, n):
    
    random.shuffle(poblacion)

    return [poblacion[i:i + n] for i in range(0,len(poblacion), n)]
    # [[(p,r,f), (p1,r1,f1), (p2,r2,f2)], [], ...]

# seleccion = [(pos,rot,fit), ...]
def cruce(seleccion: list, combinaciones_validas):

    nueva_poblacion = []
    # [(p1,r1,f1), (p2,r2,f2), (p3,r3,f3)]
    # (p1,r1,f1), (p2,r2,f2)
    # (p1,r1,f1), (p3,r3,f3)
    # (p2,r2,f2), (p3,r3,f3)
    for i in range(len(seleccion)):
        for j in range(len(seleccion)):
            if i != j:
                # hijo = (pos,rot,fit)
                hijo = cruzar_estados(seleccion[i],seleccion[j], combinaciones_validas)
                if hijo not in nueva_poblacion:
                    nueva_poblacion.append(hijo)
    
    return nueva_poblacion
    # [(pos,rot,fit), ...]
    

# padre1 = (pos1, rot1, fit1)
# padre2 = (pos2, rot2, fit2)
def cruzar_estados(padre1 ,padre2, combinaciones_validas):

    if random.random() < 0.5:
        rot = padre1[1]
        pos = padre2[0]
    else:
        rot = padre2[1]
        pos = padre1[0]
    
    hijo = (pos,rot)
        
    for combinacion in combinaciones_validas:
        if combinacion[:2] == hijo:
            return combinacion 
            # (pos,rot,fit)
    
    # si el hijo no es valido devolvemos uno de los dos padres para no perder diversidad
    hijo = random.choice([padre1,padre2])

    return hijo
    # (pos,rot,fit)"""
    

# 0.1 -> 50% de probabilidad por gen
# poblacion = [(p1,r1,f1),...]
def mutacion(poblacion, pieza_actual: Tetromino, combinaciones_validas, tasa_mutacion: int = 0.6):

    nuevos_individuos = []
    num_rotaciones = len(pieza_actual.formas)
    for (pos,_,_) in poblacion:
        # Solo alteramos de manera aleatoria la rotacion de cada hijo
        if random.random() < tasa_mutacion:
            rot_nueva = random.randint(0,num_rotaciones-1)
            #pos_nueva = random.randint(0,9)

            hijo = (pos,rot_nueva)
            #hijo = (pos_nueva,rot_nueva)
            #es_combinacion_valida = False

            for combinacion in combinaciones_validas:
                if combinacion[:2] == hijo:
                    #es_combinacion_valida = True
                    if hijo not in poblacion:
                        nuevos_individuos.append(combinacion) 
                        # (pos,rot,fit)
            
        """    if not es_combinacion_valida:
                nuevos_individuos.append((pos,rot,fit))
        else:
            nuevos_individuos.append((pos,rot,fit))"""

    return poblacion + nuevos_individuos
    # [(p1,r1,f1), (p2,r2,f2), ...]

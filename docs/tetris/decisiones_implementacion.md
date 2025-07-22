# Decisiones técnicas para la implementación del juego de Tetris

# Interfaz

La interfaz cuenta con un tablero donde se representan y ubican las piezas según el flujo del juego y un panel del lado derecho donde se muestra la siguiente pieza e informacion adicional como nivel, puntuación, tiempo de juego y líneas eliminadas por nivel

<img src="images/juegoInicio.png" alt="Interfaz" width="300">


# Tablero

El tablero implementado es una matriz de 22 filas por 10 columnas donde las 2 primeras filas se utilizan para posicionar las piezas cuando aparecen por primera vez en el tablero por encima de la línea skyline 

 # Tetrominos

Para las piezas implementamos los siete tipos del tetris clásico : I, O, T, L, J, S, Z. Cada uno con su forma y color correspondiente.
	- O : Amarillo
	- T : Purpura
	- I : Celeste
	- L : Naranja
	- J : Azul
	- S : Verde
	- Z : Rojo

<img src="images/colored_tetronimos.png" alt="Tablero" width="300">

## Ubicación y orientación incial 

Aparecen en dirección facing north y cada una en la ubicación correspondiente de manera centrada con respecto las columnas del tablero,  tal como lo establece el juego de tetris clásico 

## Tetrominos en juego 

- Cada pieza puede ser:
	-  Movida horizontalmente (una vez por celda)
	- Rotada (90° cada vez)
	- Hacer un soft drop (incrementa la velocidad de caida por 20)

- La velocidad de caída normal es calculada con la formula del tetris clásico

## Generación de Tetrominos

Se implemento del sistema de generación aleatoria de piezas del tetris clásico en el que las 7 piezas se generan de manera aleatoria cada vez que se vacía la bolsa 

## Pieza Fantasma

Se implementó la pieza fantasma, la cual indica donde caerá la pieza si se suelta en ese momento ya que puede ser útil para los algoritmos que implementaremos mas adelante

# Niveles y objetivos

- El nivel inicial del juego es el nivel 1 es decir no se puede comenzar desde un nivel más avanzado

- Se sube de nivel al cumplir el objetivo de lineas eliminas para cada nivel 

- El nivel afecta solo la velocidad de caída de las piezas 

# Sistemas de objetivos 

Se implemento el sistema de objetivos fijo cumpliendo con los siguientes parámetros:

-   Se deben limpiar 10 líneas en cada nivel, hasta el nivel 15.
    
-   Total de líneas a limpiar para llegar al nivel 15: 150 líneas (10 líneas × 15 niveles).

# Puntuación 

Los puntos de se actualizan de la siguiente manera: 

-   1 linea: 100 puntos
-   2 lineas: 200 puntos
-   3 lineas: 400 puntos
-   4 lineas o mas: 800 puntos

# Condiciones para la finalización de juego 

- El juego se termina cuando se llena el tablero y la pieza actual toca el techo 
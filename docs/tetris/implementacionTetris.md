**Tetris en Python**

Se implementó el juego "Tetris Clásico" en Python. El código se
encuentra estructurado en varias clases organizadas en módulos para
representar las distintas funcionalidades del juego, es decir, el
tablero, las piezas, la lógica y la interfaz.

Se implementó la versión básica de Tetris con:

- 7 tipos de piezas: I,O,T,S,Z,J,L

- Rotación de piezas

- Eliminación de líneas completas

- Detección de colisiones

- Game Over

- Pieza fantasma

- Cola con las próximas piezas

- Acumulación de puntos por líneas eliminadas

**Estructura**

- main.py: Punto de entrada

- tetris.py: Lógica general del juego

- tablero.py: Representación y manipulación del tablero

- tetronimo.py: Clase destinada a las piezas del juego

- piezas.py: Diccionario con las formas y colores de las piezas

- interfaz.py: Para mostrar por consola

**Clases**

- Tetronimo: Representa una pieza del juego

  - Atributos: pieza, x, y, rotación, formas

  - obtenerFormaActual(): devuelve la forma según su rotación

  - rotar() y rotacionInversa(): cambia la orientación de la pieza

  - copy(): Crea una copia exacta, es muy útil para verificar los
    movimientos antes de aplicarlos

  - imprimir_pieza(): imprime la forma actual de la pieza

  - Tetronimo utilizados: O (amarillo), I (celeste), T (purpura), L
    (naranja), J (azul), S (verde), Z (rojo).

 ![imagen tetronimos](images/colored_tetrominos.png)

- Pieza

  - Contiene el diccionario PIEZAS, que define las representaciones
    visuales de cada pieza con sus 4 rotaciones.

  - Contiene el diccionario COLORES, que define el color de la pieza

- Tablero: Contiene y gestiona el estado del juego

  - Tamaño fijo de 20 filas x 10 columnas

  - generar_matriz(): Se genera la matriz con esas dimensiones

  - eliminar_lineas(): función que cuando se completa una línea la
    elimina del tablero

  - hay_colision(): Se verifica si hay colision entre las piezas del
    juego

  - fijar_pieza(): Una ve verificado que se puede, coloca la pieza donde
    elige el usuario

  - Tablero al inicio del juego:

![Juego inicio](images/juegoInicio.png)

- Tablero luego de varias jugadas:

![Juego avanzado](images/juegoAvanzado.png)

- Tetris: Clase con el control principal

  - actualizar_estado(): Actualiza el nivel en el juego, la puntuación y
    las líneas eliminadas

  - mover_si_valido() y rotar_si_valido(): Verifica que los movimientos
    que se quieran hacer con la pieza dentro del juego se puedan hacer

  - Dentro de esta clase se generan las piezas, la actual y la fantasma

  - Se maneja la caída de las piezas y su velocidad, la cual hay 3
    tipos, caída normal, caída "soft" que se acelera al tocar la tecla
    para bajar, y caída "hard" que simula una caída casi instantánea.

  - actualizar_puntos(): método mediante el cual se actualizan los puntos
  del jugador, el cual va aumentando dependiendo cuantas elimina, si
  elimina 1 sola línea se le colocan 100 puntos, luego si elimina 2 se
  obtiene 200 puntos, si elimina 3 líneas se obtiene 400 puntos, y luego
  si elimina más de 3 se obtienen 800 puntos. En esta función vamos
  calculando y acumulando al puntaje que va obteniendo el jugador.

  - game_over(): Al tocar el "techo" se corta el juego, y pierde
    
  - Calculo velocidad de la caída:

![velocidad](images/velocidadCaida.png)

<!-- -->

- Interfaz: Clase encargada de mostrar el estado del juego utilizando la
  biblioteca pygame

  - Dibuja el tablero con la pieza actual, pieza fantasma y la pieza
    siguiente

  - Un panel lateral con la información del juego, puntaje, tiempo,
    nivel y líneas.

# Tetris clásico 

El Tetris es un juego que consta de siete Tetriminós de diferentes formas que caen en una Matriz rectangular. A medida que caen, el jugador puede rotarlos, moverlos o dejarlos caer en su lugar de descanso final. Si una o más filas están completamente llenas de bloques, la(s) línea(s) se eliminan de la Matriz y se obtienen puntos. Cuanto más eficientemente se eliminen filas en la Matriz (por ejemplo, en menos tiempo o con más despejes de línea simultáneos), mejor será la puntuación. Se otorgan bonificaciones por despejar líneas simultáneamente, acciones especiales llamadas "T-Spins" y por lograr acciones consecutivas de alta puntuación.

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tetris.png" style="width: 77%; height: auto;"/>
</p>

## Terminología 

#### Back-to-Back

Cuando se hacen dos jugadas de alto valor (como dos Tetrises o T-Spins) una tras otra, sin que entre medio ocurra una eliminación simple, doble o triple de líneas. Esto da más puntos y bonificaciones.

#### Block (Bloque)

Un solo cuadrado dentro del tablero, ya bloqueado (fijo) en una celda. Es la unidad más básica que forma las piezas y las líneas.

#### Block Out

Condición de _Game Over_ que ocurre cuando una nueva pieza no puede aparecer completamente en el tablero porque algo ya la está bloqueando (por ejemplo, la parte superior del tablero está ocupada).

#### Buffer Zone (Zona de búfer)

Área invisible encima del tablero (Matrix) de 10 columnas × 20 filas. Se usa para detectar condiciones de finalización de juego como _Block Out_, _Lock Out_ o _Top Out_. Las piezas comienzan a caer en esta zona.

#### Line Clear

Ocurre cuando una fila entera se llena con bloques y se elimina. Todas las piezas encima bajan una fila. Se pueden eliminar varias líneas a la vez, lo cual da más puntos.

#### Lock Down

Momento en que una pieza se fija y deja de poder moverse o rotarse. Suele ocurrir 0.5 segundos después de que toca el suelo o una pieza ya bloqueada.

#### Lock Down (Fijación de piezas)

-   Cuando se hace un Hard Drop (caída instantánea), la pieza se bloquea al instante al tocar una superficie.
    
-   Si la pieza cae naturalmente o por un Soft Drop, tiene un retraso de 0.5 segundos antes de bloquearse. Durante ese tiempo puede mover o rotar.
    
-   Existen tres reglas de comportamiento para el bloqueo:
    
    -   Infinite Placement: permite mover indefinidamente antes de que la pieza se bloquee.
        
    -   Extended: ofrece un número limitado de movimientos para reiniciar el temporizador. _(Por defecto)_.
        
    -   Classic: la pieza se bloquea sin posibilidad de extensión.

#### Lock Out

Condición de _Game Over_ que sucede cuando una pieza se bloquea completamente por encima de la línea superior visible del tablero (Skyline), sin siquiera poder entrar en el área de juego.

#### Matrix

Es el tablero de juego activo, normalmente de 10 columnas por 20 filas. Aquí es donde caen y se colocan las piezas. La parte superior del tablero está justo debajo de la zona de buffer

#### Mino

Un solo cuadrado que forma parte de una pieza Tetriminó. Cuatro Minos conectados entre sí crean un Tetriminó.

#### Skyline

Es la línea horizontal más alta del tablero visible. Las piezas aparecen justo encima de esta línea, en la zona de búfer.

#### Tetris

El nombre de la jugada cuando una pieza I (la larga) limpia 4 líneas de una sola vez, el máximo posible. Es una jugada de alto valor y puntaje.

#### Top Out

Otra condición de _Game Over_. Sucede cuando la acumulación de bloques llega hasta la parte superior de la zona de búfer, sobrepasando la línea límite (_Top Out Line_).

#### Top Out Line

Es la línea más alta posible del juego, 20 filas por encima del Skyline. Si los bloques la alcanzan, se termina el juego.

#### T-Slot

Una **formación específica de bloques** donde se puede encajar girando una pieza T. Es una configuración necesaria para ejecutar un _T-Spin_.

#### T-Spin

Técnica avanzada: consiste en rotar una pieza T dentro de un espacio ajustado (T-Slot) justo antes de que se bloquee. Da muchos puntos, especialmente si limpia líneas.

## Tetriminós

Son piezas de Tetris formadas por cuatro Minos conectados. Hay siete tipos: I, O, T, L, J, S, Z. Cada uno tiene una forma y color únicos.

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tetrominos.png" style="width: 77%; height: auto;"  />
</p>

-   **O-Tetrimino** (amarillo):  
    Forma de *cuadrado. Está compuesto por cuatro bloques en una estructura 2×2. No rota visualmente al girar.
    
-   **I-Tetrimino** (celeste):  
    Forma de una línea recta vertical. Cuatro bloques alineados. Es ideal para hacer un Tetris (limpiar 4 líneas).
    
-   **T-Tetrimino** (púrpura):  
    Forma de una T mayúscula. Tres bloques en fila con uno adicional en el centro, en la parte superior. Permite realizar T-Spins.
    
-   **L-Tetrimino** (naranja):  
    Forma de una L. Tres bloques en línea con uno añadido arriba del lado derecho.
    
-   **J-Tetrimino** (azul oscuro):  
    Forma de una J. Similar al L-Tetrimino, pero el bloque extra está a la izquierda.
    
-   **S-Tetrimino** (verde):  
    Forma de una S. Dos bloques horizontales encima de otros dos, desplazados hacia la derecha.
    
-   **Z-Tetrimino** (rojo):  
    Forma de una Z. Similar al S-Tetrimino, pero invertido hacia la izquierda.

## Nivel de Inicio

En Tetris, los niveles suelen ir del 1 al 15. Cada nivel representa una velocidad creciente en la caída de las piezas. Por lo general, el juego comienza en el nivel 1 por defecto, aunque en algunas versiones se puede elegir desde qué nivel iniciar. Esta elección permite ajustar la dificultad desde el principio.

## Tablero

El diseño del tablero debe incluir los siguientes elementos:
-   **Matriz** (tablero de juego)
    
-   **Hold Queue** (pieza guardada)
    
-   **Next Queue** (cola de próximas piezas)

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tablero.png" style="width: 77%; height: auto;"  />
</p>

## Componentes esenciales de la interfaz

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/interfaz.png" style="width: 77%; height: auto;"  />
</p>

#### 1. Matriz **

Es el tablero donde se juega. Tiene dimensiones estándar de 10 columnas de ancho × 20 filas de alto. Es el área donde caen y se colocan las piezas.

#### 2. Tetriminó en juego

Es la pieza actual que el jugador controla. Se puede:

- Mover lateralmente
    
- Rotar  (en sentido horario o antihorario)
    
-   Hacer un:
    
    -   **Soft Drop**: baja más rápido (20× la velocidad normal) mientras se mantiene presionado el botón.
        
    -   **Hard Drop**: baja instantáneamente y se bloquea al tocar superficie.
        

#### 3. Cola de próximas piezas (Next Queue)

Muestra las próximas piezas que aparecerán. Debe estar en la parte superior derecha de la matriz.

-   Lo ideal es mostrar las 6 siguientes piezas pero el número de piezas mostradas puede variar entre 1 y 6
    
-   El orden puede estar en columna o fila.
    
-   Las piezas deben mostrarse con orientación **"facing North"** (rotación estándar).
    

#### 4. Pieza Fantasma (Ghost Piece)

Es una sombra o contorno transparente de la pieza en juego que indica dónde caerá si se suelta en ese momento.  
Ayuda al jugador a planificar mejor sus movimientos.


#### 5. Gráfico de fondo (Background Graphic)

Fondo visual del juego. Puede dar estilo y estética, pero no debe interferir con la visibilidad de las piezas ni del tablero.


#### 6. Bloques iniciales (Starting Blocks)

Algunas variantes permiten que el juego comience con filas prellenadas en la parte inferior de la matriz, aumentando la dificultad desde el inicio.


#### 7. Información del juego (Game Info)

Datos que se muestran en pantalla, como:

-   Tipo de juego
    
-   Líneas eliminadas o restantes
    
-   Nivel actual
    
-   Tiempo transcurrido o restante
    
-   Puntuación actual y más alta
    
-   Nombre del jugador y su ranking
    

#### 8. Cola de retención (Hold Queue)

Permite guardar una pieza para usarla más adelante.

-   Si ya hay una pieza guardada, se intercambian.
    
-   Está ubicada en la parte superior izquierda de la matriz.
    
-   Las piezas deben mostrarse también con orientación "North Facing".

## Generación de Tetrominós

Cada Tetriminó en Tetris está compuesto por cuatro Minos, y cada Mino tiene exactamente el tamaño de una celda de la matriz (el tablero).

Según las guías oficiales de Tetris, se asigna un color específico a cada tipo de pieza para que sean fácilmente reconocibles. Los colores estándar son:

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetros/images/colored_tetrominos.png" style="width: 77%; height: auto;"  />
</p>

### Sistema de generación aleatoria

En Tetris, el sistema de generación aleatoria de piezas utiliza el llamado “sistema de bolsa” (7-bag). Esto garantiza una distribución justa: se colocan las 7 piezas distintas en una bolsa virtual, se mezclan al azar, y se van sacando una por una en ese orden. Cuando la bolsa se vacía, se vuelve a llenar y a mezclar.

Esto evita que aparezcan repeticiones excesivas de una misma pieza o que falten por mucho tiempo.

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/generacion_aleatoria.png" style="width: 77%; height: auto;"  />
</p>

### Ubicación y orientación inicial 

-   Todas las piezas aparecen con orientación "North Facing" (posición por defecto, sin rotación) en las filas 21 y 22,  justo por encima del tablero visible, sobre la línea llamada Skyline
    
-   El tablero tiene 10 columnas de ancho.

- Posiciones específicas al generarse:

	-   **T, L, J, S, Z**: comienzan en las columnas 4 a 6 (3 bloques de ancho), alineadas horizontalmente.
    
	-   **O (cuadrada)**: aparece centrada, ocupando columnas 5 y 6**.
    
	-   **I (barra)**: aparece más arriba (solo en la fila 21), ocupando columnas 4 a 7.

Esto asegura que todas las piezas se alineen visualmente al centro del tablero y tengan espacio para rotar.

#### Cuando un Tetrimino es generado, suceden tres cosas:

1.  Desciende una fila automáticamente si no hay bloques debajo.
    
2.  El jugador puede comenzar a moverlo o rotarlo inmediatamente.
    
3.  Si la opción está activada, aparece la Ghost Piece (pieza fantasma), en orientación estándar (_North Facing_), indicando dónde caerá la pieza.

Si hay un bloque en su camino desde el inicio, no baja una fila, pero se muestra parcialmente (si el hardware lo permite) para que el jugador pueda manipularla sobre el Skyline.

IMAGEN

## Comportamiento de tetriminós

### Solo una pieza a la vez

Solo un Tetriminó puede estar activo en el tablero a la vez. El jugador puede:

-   Moverla izquierda/derecha
    
-   Rotarla
    
-   Hacer Soft Drop (caída acelerada)
    
-   Hacer Hard Drop (caída instantánea)
    
-   Guardarla en el Hold


### Movimiento

-   Las piezas caen una celda a la vez, desde justo encima del Skyline.
    
-   El movimiento lateral también es de una celda por vez.
    
-   Visualmente el movimiento puede ser fluido, pero cada Mino se "acopla" a la cuadrícula.
    
-   No se permite mover dentro de celdas ya ocupadas, ni más allá de los bordes o suelo.


### Repetición automática

-   Si se mantiene presionada una tecla de dirección (izquierda o derecha), después de un retraso de 0.3 segundos, la pieza se moverá rápidamente hacia ese lado.
    
-   Esto permite mover la pieza de un extremo al otro en menos de 0.5 segundos, algo crucial en niveles rápidos.
    
-   Si se cambia de dirección mientras se mantiene Auto-Repeat, el movimiento se reinicia con el mismo retraso.
  
### Rotación

-   Las piezas pueden rotar 90 grados en sentido horario o antihorario.
    
-   Se usa el sistema llamado Super Rotation System (SRS), que permite rotar incluso cuando la pieza está contra una pared o bloque.
    
-   Se puede rotar la pieza mientras está en movimiento lateral con Auto-Repeat (movimiento rápido), pero no hay Auto-Repeat para la rotación (es decir, cada rotación requiere que se pulse la tecla).
  
### Hard drop
-   El comando Hard Drop hace que la pieza caiga instantáneamente hasta el primer lugar donde pueda bloquearse.
    
-   La caída es prácticamente inmediata (0.0001 segundos).
    
-   No hay Auto-Repeat para Hard Drop; cada uso debe ser una acción individual.


### Soft Drop (Caída suave)

-   Cuando se presiona el botón de Soft Drop, la pieza en juego cae a una velocidad 20 veces más rápida que la velocidad normal de caída.
    
-   Por ejemplo, si la velocidad normal es 0.5 segundos por línea, con Soft Drop será 0.025 segundos por línea.
    
-   La pieza vuelve a la velocidad normal cuando se suelta el botón.
    
-   **Importante:** Si se usa Soft Drop hasta que la pieza toca el suelo, el bloqueo (Lock Down) no ocurre inmediatamente, sino cuando termina el temporizador de Lock Down (usualmente 0.5 segundos).
    


### Hold (Guardar pieza)

-   Permite guardar la pieza en juego en la cola de retención (Hold Queue).
    
-   Si ya hay una pieza guardada, esta se intercambia y comienza a caer desde la posición inicial.
    
-   Sólo se puede tener una pieza guardada a la vez.
    
-   Debe ocurrir un Lock Down entre usos del Hold, es decir, no se puede guardar la misma pieza repetidamente sin que la pieza actual quede bloqueada primero.


### Extended Placement Lock Down (Bloqueo con colocación extendida)

-   Es el modo por defecto en las opciones del juego.
    
-   Cuando la pieza toca una superficie, empieza un temporizador de 0.5 segundos.
    
-   Si el jugador mueve o rota la pieza, el temporizador se reinicia a 0.5 segundos.
    
-   Además, la pieza puede moverse o rotar hasta 15 veces antes de bloquearse, independientemente del tiempo restante en el temporizador.
    
-   Si la pieza baja a una fila más baja que la que alcanzó antes, ese contador de 15 movimientos/rotaciones se reinicia.
    
-   Si la pieza vuelve a subir, sigue usando esos movimientos/rotaciones restantes.
    
-   Cuando se acaben esos movimientos/rotaciones, el temporizador ya no se reinicia y la pieza se bloquea al tocar una superficie.
    
-   Si la pieza no toca superficie, puede seguir moviéndose y rotándose hasta que baje más.


### Infinite Placement Lock Down (Bloqueo con colocación infinita)

-   También comienza el temporizador de 0.5 segundos cuando la pieza toca una superficie.
    
-   El temporizador se reinicia a 0.5 segundos cada vez que el jugador mueve o rota la pieza.
    
-   Esto permite que el jugador siga moviendo y rotando la pieza indefinidamente, siempre que continúe cambiando su posición u orientación antes de que expire el temporizador.
    
-   Solo cuando el temporizador llegue a cero sin movimiento o rotación, la pieza se bloquea.


### Classic Lock Down (Bloqueo Clásico)

-   Este modo se usa si no están activados ni el Infinite Placement ni el Extended Placement.
    
-   Al igual que en los otros modos, cuando la pieza toca una superficie, comienza un temporizador de 0.5 segundos.
    
-   El temporizador solo se reinicia si la pieza baja a una fila más baja (disminuye su coordenada y) dentro de la matriz.
    
-   No se reinicia el temporizador con movimientos laterales ni rotaciones.
    
-   Esto significa que una vez que la pieza toca superficie, tiene solo ese medio segundo para moverse o rotar antes de bloquearse, a menos que baje más.


##  Jugadas Especiales (T-Spins y Mini T-Spins)

Consisten en rotar un T-Tetriminó dentro de un espacio cerrado llamado T-Slot. Estas jugadas otorgan bonificaciones de puntos y pueden formar parte de secuencias Back-to-Back.

### ¿Qué es un T-Slot?
- Es una formación de bloques tal que cuando el T-Tetriminó se coloca dentro mediante rotación (no caída directa), tres de las cuatro casillas diagonales al centro del T-Tetriminó están ocupadas por bloques ya existentes.

### Requisitos para que cuente como T-Spin:

- El T-Tetriminó debe rotar al entrar al T-Slot.

- No basta con moverlo o dejarlo caer directamente en la posición.

- Si se cumplen las condiciones pero no se eliminan líneas, puede contarse como Mini T-Spin en lugar de un T-Spin completo.


### Reconocimiento

En los siguientes diagrama, cada letra corresponde al lado de un mino en el tetrominó:

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/spins.png" style="width: 77%; height: auto;"  />
</p>

#### T-Spin (válido)

Una rotación se considera T-Spin completo si:

- **A y B + (C o D)** están en contacto con la superficie al bloquearse el T.
- El T-Tetrimino llena completamente un T-Slot sin dejar huecos.
- Se utiliza el Punto de Rotación 5 del Super Rotation System para entrar al T-Slot.

> Una vez que se usa el Punto 5, cualquier rotación posterior será considerada un T-Spin (no Mini).

#### Mini T-Spin

Una rotación se considera Mini T-Spin si:

- **C y D + (A o B)** están tocando la superficie (al revés del caso anterior).
- El T-Tetrimino entra al T-Slot pero deja huecos.
-  Excepto si se usó el Punto de Rotación 5: en ese caso se eleva a T-Spin completo.

A continuación se presenta algunos ejemplos de T-Spins y Mini T-Spins en Tetris 

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tspin1.png" style="width: 77%; height: auto;"  />
</p>

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tspin2.png" style="width: 77%; height: auto;"  />
</p>

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tspin3.png" style="width: 77%; height: auto;"  />
</p>

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/tetris/images/tspin4.png" style="width: 77%; height: auto;"  />
</p>


---
## Niveles y objetivos en Tetris

-   Los juegos de Tetris típicos tienen 15 niveles, numerados del 1 al 15.
    
-   Se sube de nivel (Level Up) al cumplir el objetivo de líneas a eliminar para cada nivel.
    
-   El nivel actual afecta:
    
    -   La velocidad de caída de las piezas (a medida que sube el nivel, caen más rápido).
        
    -   La puntuación (se otorgan más puntos por limpiar líneas o hacer jugadas especiales como T-Spins).
        

### Sistemas de objetivos (Goals)

Hay dos sistemas principales para definir cuántas líneas hay que limpiar para avanzar de nivel:

1.  **Sistema de Objetivo Fijo (Fixed Goal System)**
    
    -   Se deben limpiar 10 líneas en cada nivel, hasta el nivel 15.
        
    -   Total de líneas a limpiar para llegar al nivel 15: 150 líneas (10 líneas × 15 niveles).
        
2.  **Sistema de Objetivo Variable (Variable Goal System)**
    
    -   El objetivo aumenta en 5 líneas por nivel:
        
        -   Nivel 1: 5 líneas
            
        -   Nivel 2: 10 líneas
            
        -   Nivel 3: 15 líneas
            
        -   … y así sucesivamente, sumando 5 líneas adicionales por nivel.
            
    -   Total de líneas para llegar al nivel 15: 600 líneas (suma acumulada).
        
    -   Este sistema puede incluir bonificaciones por limpiar múltiples líneas a la vez para acelerar el avance.
        

### Opciones para empezar en niveles superiores

-   El jugador debe poder empezar en cualquier nivel desde el menú principal.
    
-   Para el Sistema de Objetivo Fijo, si se empieza en un nivel superior a 1, el objetivo para avanzar incluye todas las líneas acumuladas desde los niveles anteriores más el objetivo del nivel actual.
    
Ejemplo:  
Si el jugador comienza en nivel 4, para subir a nivel 5 debe limpiar:

-   Las 30 líneas acumuladas hasta nivel 3 (3 niveles × 10 líneas cada uno)
    
-   -   Las 10 líneas del nivel 4  
        Total: 40 líneas para alcanzar el nivel 5.
        
-   Para niveles superiores a 1 en el Sistema Variable, el objetivo por nivel es simplemente:  
- 
    **Goal = Nivel × 5 líneas**

### Impacto en la puntuación

-   La puntuación total al final del juego es mayor si empezás en niveles más altos, ya que las piezas caen más rápido y las bonificaciones son mayores.

---

### Sistema de Objetivo Variable y Líneas Limpias (Line Clears)

Para acelerar el proceso de limpiar las 600 líneas necesarias en el Sistema de Objetivo Variable, la cantidad de líneas que se acreditan por cada acción depende directamente de la puntuación obtenida por esa acción.

-   Se calcula así:  

		Líneas Limpias otorgadas = (puntuación de la acción al nivel 1) ÷ 100
    
-   Esto significa que acciones que otorgan más puntos, como un T-Spin o un Tetris (limpiar 4 líneas a la vez), dan más líneas acreditadas para avanzar en el objetivo.
    
-   Además, este sistema incentiva a los jugadores a usar estas jugadas de alto puntaje para avanzar más rápido en el juego.

---

## Velocidad de caída

-   Al generarse una pieza, cae una fila automáticamente (si no hay bloque debajo).
    
-   Luego, comienza a descender según la velocidad normal de caída (_Fall Speed_), que depende del nivel actual.
    
-   Esta velocidad se mide como el tiempo que tarda una pieza en caer una línea.

- La velocidad (en segundos por línea) se calcula con la siguiente fórmula:

					(0.8 - ((nivel - 1) × 0.007)) ^ (nivel - 1)

-   A mayor nivel, menor será el tiempo, lo que significa que las piezas caen más rápido.
    
-   Por ejemplo:
    
    -   Nivel 1 ≈ 0.8 s por línea
        
    -   Nivel 10 ≈ 0.1 s por línea
        
    -   Nivel 15 ≈ 0.05 s por línea

A continuación se presenta una tabla con los valores aproximados en segundos por línea:

| Nivel | Velocidad de Caída (s/línea) |
|:-----:|:----------------------------:|
| 1     | 0.800                        |
| 2     | 0.717                        |
| 3     | 0.634                        |
| 4     | 0.551                        |
| 5     | 0.468                        |
| 6     | 0.385                        |
| 7     | 0.302                        |
| 8     | 0.219                        |
| 9     | 0.136                        |
| 10    | 0.100                        |
| 11    | 0.083                        |
| 12    | 0.067                        |
| 13    | 0.050                        |
| 14    | 0.033                        |
| 15    | 0.017                        |


## Velocidades de Descenso Manual (Drop Speeds)

Además de la caída automática (Fall Speed), el jugador puede controlar la velocidad de descenso mediante dos comandos:

###  Soft Drop
- Permite acelerar manualmente la caída del Tetriminó.
- Se recomienda que sea 20 veces más rápida que la velocidad de caída normal del nivel actual.
- Por ejemplo, si la Fall Speed en el nivel 1 es de 1.0 s/línea, la Soft Drop será de 0.05 s/línea.

### Hard Drop
- Hace que el Tetriminó caiga instantáneamente hasta la superficie y se bloquee.
- La velocidad recomendada es 0.0001 segundos por línea (prácticamente inmediata).

## Sistema de Puntuación (Scoring)

El jugador gana puntos al realizar diversas acciones durante el juego. Algunas dependen del nivel actual y otras tienen valores fijos.

####  Acciones que otorgan puntos

- **Line Clears:**
  - **Single** (1 línea)
  - **Double** (2 líneas)
  - **Triple** (3 líneas)
  - **Tetris** (4 líneas con un I-Tetrimino)

- **T-Spins:**
  - T-Spin Single
  - T-Spin Double
  - T-Spin Triple
  - **Mini T-Spin** (versiones reducidas del movimiento)

- **Drop:**
  - **Soft Drop:** puntos fijos por cada línea descendida manualmente
  - **Hard Drop:** puntos fijos por línea instantáneamente descendida

#### Bonificaciones especiales

- **Back-to-Back (B2B):**
  - Ocurre cuando se encadenan dos acciones importantes (como un Tetris seguido de un T-Spin Double) sin un Line Clear simple entre ellas.
  - Otorga una bonificación adicional.
  
  IMAGEN

#### T-Spins sin eliminación de líneas y el sistema Back-to-Back

- Los T-Spins y Mini T-Spins que no eliminan líneas:

  - No reciben bonificación Back-to-Back.
  - No pueden iniciar una secuencia Back-to-Back.
  - Tampoco rompen una secuencia existente. Es decir, si ocurren entre dos acciones Back-to-Back válidas, la cadena sigue activa.

* Ejemplo de Puntuación con Back-to-Back

	* Secuencia de acciones en Nivel 1:

		1. **Tetris**  
			   → 800 pts *(sin bonus B2B porque es el primero)*

		2. **T-Spin Double**  
		   → 1200 pts  
		   → +600 pts (bonus Back-to-Back)

		3. **T-Spin (sin Line Clear)**  
		   → 400 pts *(no rompe la secuencia B2B)*

		4. **Tetris**  
		   → 800 pts  
		   → +400 pts (bonus Back-to-Back)

		5. **T-Spin Single**  
		   → 800 pts  
		   → +400 pts (bonus Back-to-Back)

			Total: 800 + (1200 + 600) + 400 + (800 + 400) + (800 + 400) = 5400 puntos

- El primer movimiento válido en una secuencia Back-to-Back no recibe bonificación.

* Las acciones que no limpian líneas (como T-Spins vacíos o simplemente mover piezas) no rompen la cadena.

* Single, Double o Triple Line Clears sí rompen la secuencia Back-to-Back.

## Condiciones de finalización de juego

El juego termina (Game Over) cuando alguna de las siguientes situaciones ocurre:

1.  **Lock Out (Bloqueo de Tetrimino):**  
    Cuando un Tetrimino queda completamente bloqueado (fijo) _por encima_ de la "línea del cielo" (Skyline). Es decir, el jugador coloca una pieza en una posición tan alta que supera la línea que marca el límite visible del tablero.
    
2.  **Block Out (Bloqueo de Bloque):**  
    Cuando la pieza siguiente (Next Tetrimino) no puede aparecer porque una de sus casillas iniciales está ocupada por un bloque que ya está en el tablero.
    
3.  **Top Out (Superar el Buffer):**  
    Cuando bloques existentes son empujados _más allá_ de la zona llamada Buffer Zone (zona de reserva o amortiguamiento), que es un espacio de 20 filas por encima de la Skyline. Esto puede suceder, por ejemplo, si un ataque de línea del oponente empuja tus bloques hacia arriba más allá de esta zona.

* **Situaciones comunes respecto a la buffer zone**:

	-   **Lock Down - Normal (Juego no terminado):**  
    El Tetrimino queda bloqueado completamente _por debajo_ de la Skyline. Esto es lo usual y el juego continúa.
    
	-   **Lock Down - Peeking (Juego no terminado):**  
    El Tetrimino queda bloqueado parcialmente _por encima y por debajo_ de la Skyline, pero sigue dentro de límites aceptables, así que el juego continúa.

    
	-   **Jugar por encima de la Skyline (Juego no terminado):**  
    El jugador puede mover o rotar la pieza _por encima_ de la Skyline, en la zona de Buffer, sin que eso signifique un Game Over.
    
	-   **Bloques existentes forzados hacia arriba (Juego no terminado):**  
    Si bloques en el tablero son empujados _por encima_ de la Skyline, pero aún _dentro_ de la Buffer Zone, el juego sigue.

    
	-   **Top Out (Juego terminado):**  
    Cuando bloques son empujados _más allá_ de la Buffer Zone por un ataque del oponente, el juego termina.  
    Es muy raro que pase, porque normalmente el Lock Out o Block Out ocurren antes.
    
	-   **Lock Out (Juego terminado):**  
    Cuando un Tetrimino queda bloqueado completamente _por encima_ de la Skyline. Esto provoca el fin del juego.

	-   **Block Out (Juego terminado):**  
    Cuando la siguiente pieza no puede generarse porque su espacio inicial está ocupado, el juego termina.

## Bibliografía

Blue Planet Software, Inc. (2009). _Tetris® Design Guideline_. Marzo 2009. Blue Planet Software, Inc.

# Algoritmos de búsqueda local

La búsqueda local es un método de optimización que consiste en el desplazamiento iterativo de una solución a otra vecina. Para ello, se evalúan las soluciones basándose en una función heurística, que proporciona una medida de la calidad de la solución. Estos algoritmos buscan encontrar la mejor solución en las proximidades del estado actual, en lugar de explorar todo el espacio de soluciones. Esta estrategia de exploración local es lo que los hace especialmente valiosos.

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/busqueda_local/images/LS.png" style="width: 77%; height: auto;"  />
</p>

Los problemas de optimización implican encontrar la mejor solución entre un conjunto de soluciones factibles con base en una función objetivo definida. Estos problemas surgen en diversos campos, como la investigación de operaciones, la ingeniería, las finanzas y aprendizaje automático. Las características clave de los problemas de optimización incluyen:

**Función objetivo:** Función matemática que cuantifica la calidad de una solución.

**Restricciones:** Limitaciones o restricciones a las soluciones factibles.

**Espacio de búsqueda:** El conjunto de todas las soluciones posibles.

El aspecto "local" se refiere al alcance limitado de la búsqueda. Estos algoritmos están diseñados para optimizar dentro de un entorno restringido del estado actual, a diferencia de los métodos de optimización global que buscan encontrar el óptimo global en todo el espacio de la solución. Los algoritmos de búsqueda local adoptan un enfoque más específico. Evalúan y mejoran la solución actual de forma iterativa, avanzando paso a paso hacia una solución óptima o casi óptima.

## Características

- Mejora iterativamente una solución actual.

- Explora el vecindario de una solución.

- Se utiliza en problemas de optimización como programación, enrutamiento y aprendizaje automático.

## Importancia 
1. Eficiencia en amplios espacios de soluciones : Al abordar problemas con un número astronómico de posibles soluciones, la búsqueda exhaustiva se vuelve inviable. Los algoritmos de búsqueda local ofrecen un enfoque inteligente y específico al explorar soluciones cercanas al estado actual

2. Aplicaciones reales : Los algoritmos de búsqueda local encuentran aplicaciones en diversos dominios. Ya sea que esté planificando la ruta más eficiente, optimizando recursos o entrenando modelos de aprendizaje automático, estos algoritmos son sus herramientas de referencia.

3. Fundamentos para técnicas avanzadas : Los algoritmos de búsqueda local sirven como base para técnicas de optimización más sofisticadas en IA. Proporcionan los principios básicos sobre los que se construyen los algoritmos genéticos, el recocido simulado y otros métodos.

## Función heurística
En el corazón de los algoritmos de búsqueda local se encuentra el concepto de funciones de evaluación heurística. Estas funciones son esenciales para evaluar la calidad o conveniencia de una solución. La función heurística proporciona una puntuación numérica o una estimación de la proximidad de una solución a la óptima. Guía al algoritmo de búsqueda local en IA a la hora de decidir qué soluciones vecinas explorar a continuación.

El término "heurística" en este contexto significa que la evaluación se basa en reglas generales o conocimiento específico del dominio. En lugar de garantizar una solución óptima, la heurística proporciona una evaluación rápida e informada de la calidad de la solución. La elección de la función heurística desempeña un papel fundamental en el rendimiento de un algoritmo de búsqueda local, ya que influye en su capacidad para explorar eficazmente el espacio de la solución.

## Componentes de la búsqueda local

Los algoritmos de búsqueda local constan de varios componentes esenciales que trabajan en armonía para navegar eficientemente por los espacios de soluciones. Analicemos estos componentes en detalle:

1. Estado inicial : también conocido como punto de partida, es donde comienza la búsqueda local. Representa una posible solución al problema en cuestión. Los algoritmos de búsqueda local parten de este estado inicial y exploran iterativamente soluciones vecinas para mejorarlo.

2. Vecinos : Los vecinos son soluciones estrechamente relacionadas con el estado actual. Se obtienen realizando pequeñas modificaciones en el estado actual, como cambiar un elemento o moverse a un nodo adyacente en un espacio de búsqueda. Los vecinos son esenciales porque los algoritmos de búsqueda local se centran en refinar la solución actual examinando estas opciones cercanas.

3. Función Objetivo : La función objetivo, también conocida como función de evaluación o función heurística, desempeña un papel fundamental en los algoritmos de búsqueda local. Esta función cuantifica la calidad o conveniencia de una solución. Asigna un valor numérico a cada solución, lo que refleja su proximidad a la solución óptima. La función objetivo guía el proceso de búsqueda, ayudando al algoritmo a seleccionar los vecinos más prometedores para su exploración.

## Exploración versus Explotación

Los conceptos de exploración y explotación se consideran fundamentales en el contexto de algoritmos de optimización y metahurística ya que estos determinan las características de la búsqueda

En el libro Metaheuristics: From Design to Implementation (2009), El-Ghazali Talbi dice:

"La explotación busca intensivamente soluciones de alta calidad en el vecindario, mientras que la exploración diversifica la búsqueda para escapar de los óptimos locales y cubrir el espacio de búsqueda."

Si orientamos este concepto al juego de tetris, obtenemos:

| **Concepto** | **Descripción** | **Ejemplo en Tetris**|
| -----------------|--------------------|---------------|
|Explotación| Mejorar las mejores soluciones actuales, refinarlas.| Colocar las piezas de forma conservadora en posiciones similares a las que ya funcionaron.|
|Exploración | Probar nuevas soluciones en áreas del espacio no exploradas.| Probar colocar la pieza en una posición menos común o arriesgada para ver si rinde mejor.|


# Fundamentos de Hill Climbing y sus variantes

Hill Climbing es un algoritmo de búsqueda heurística utilizado principalmente para problemas de optimización matemática en inteligencia artificial (IA). Es una forma de búsqueda local, lo que significa que se centra en encontrar la solución óptima mediante cambios graduales en una solución existente y luego evaluar si la nueva solución es mejor que la actual. El proceso es similar a subir una colina, donde se busca continuamente mejorar la posición hasta alcanzar la cima, o máximo local, desde donde ya no se puede mejorar.

El Hill Climbing es un concepto fundamental en IA debido a su simplicidad, eficiencia y eficacia en determinados escenarios, especialmente cuando se trata de problemas de optimización o se encuentran soluciones en grandes espacios de búsqueda.

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/busqueda_local/images/LS1.png" style="width: 77%; height: auto;"  />
</p>

El proceso comienza con una solución inicial, que se mejora iterativamente mediante pequeños cambios incrementales. Estos cambios se evalúan mediante una función heurística para determinar la calidad de la solución. El algoritmo continúa realizando estos ajustes hasta alcanzar un máximo local , un punto en el que ya no se pueden realizar mejoras con el conjunto actual de movimientos.

El algoritmo Hill Climbing emplea un enfoque voraz, lo que significa que, en cada paso, se mueve en la dirección que optimiza la función objetivo. Esta estrategia busca encontrar la solución óptima de forma eficiente, tomando la mejor decisión inmediata sin considerar el contexto general del problema.

Este algoritmo, se utiliza a menudo para resolver problemas de optimización matemática en IA. Con una buena función heurística y un amplio conjunto de datos de entrada, el algoritm puede encontrar una solución suficientemente buena en un tiempo razonable, aunque no siempre alcanza el máximo óptimo global .

En optimización matemática, el método de Hill Climbing se aplica comúnmente a problemas que implican maximizar o minimizar una función real . Por ejemplo, en el problema del viajante , el objetivo es minimizar la distancia recorrida por el viajante al visitar varias ciudades.

## Pasos del Hill Climbing

**Estado inicial**: inicia con una solución arbitraria o aleatoria (estado inicial).

**Estados vecinos** : se identifican los estados vecinos de la solución actual realizando pequeños ajustes (mutaciones o ajustes).

**Mudarse a vecino**: si uno de los estados vecinos ofrece una mejor solución (según alguna función de evaluación), se avanza a este nuevo estado.

**Terminación**: se repite este proceso hasta que ningún estado vecino sea mejor que el actual. En este punto, habrá alcanzado un máximo o mínimo local (dependiendo de si está maximizando o minimizando).

## Variantes

<p align="center">
  <img src="https://github.com/trinidadperea/final_IA_tetris/raw/main/docs/busqueda_local/images/typesHC.png" style="width: 77%; height: auto;"  />
</p>

## Simple Hill Climbing

Simple Hill Climbing es una variante sencilla del Hill Climbing donde el algoritmo evalúa cada nodo vecino uno por uno y selecciona el primer nodo que ofrece una mejora sobre el actual.

#### Proceso:

1. Desde un estado actual, genera un sucesor.

2. Si el sucesor es mejor → lo adopta.

3. Si no hay mejora → se detiene.

#### Ventajas:

+ Rápido y fácil de implementar.
+ Consume menos memoria (solo necesita almacenar el estado actual y uno sucesor).

#### Desventajas:

* Puede quedar atrapado fácilmente en:
* Máximos locales
* Mesetas (áreas planas sin mejora)
* Crestas (cambios de mejora muy estrechos que se pueden pasar por alto)

## Steepest-Ascend Hill Climbing

El ascenso más pronunciado es una versión mejorada del ascenso simple. En lugar de moverse al primer nodo vecino que mejore el estado, evalúa todos los vecinos y se mueve al que ofrece la mayor mejora (ascenso más pronunciado).

#### Proceso:

1. Genera todos los vecinos (sucesores).

2. Evalúa la función objetivo para cada uno.

3. Se mueve al mejor sucesor si mejora.

4. Se detiene si no hay mejoras posibles.

#### Ventajas:

* Mayor probabilidad de encontrar una mejor solución que el simple hill climbing.
* Menos susceptible a tomar decisiones precipitadas.

#### Desventajas:
* Más costoso computacionalmente: necesita generar y evaluar todos los sucesores.
* Aún puede quedar atrapado en máximos locales o mesetas.

## Stochastic Hill Climbing

El ascenso estocástico introduce aleatoriedad en el proceso de búsqueda. En lugar de evaluar a todos los vecinos o seleccionar la primera mejora, selecciona un nodo vecino aleatorio y decide si se mueve en función de su mejora con respecto al estado actual.

#### Proceso:

1. Genera algunos sucesores del estado actual.

2. Filtra los que son mejores.

3. Selecciona uno al azar entre ellos para moverse.

4. Si no hay mejores → se detiene.

#### Ventajas:
* Ayuda a escapar de máximos locales suaves gracias al elemento aleatorio.

* Menos costoso que el steepest ascent (no necesita revisar todos los sucesores).

* Introduce exploración en la búsqueda.

#### Desventajas:

* Menos predecible: puede que no escoja la mejor mejora.
* Aún puede quedar atrapado si el espacio está mal diseñado o si hay pocos sucesores mejores.

## Algoritmo de Hill Climbing en Tetris

En Tetris, en cada turno el jugador debe colocar una pieza de entre varias formas (tetrominós) en una posición y rotación que minimice el espacio del tablero y maximice la puntuación. Esto puede verse como un problema de optimización, donde:

- El estado es la configuración actual del tablero.
- La acción es colocar la pieza actual en una posición válida.
- La función objetivo (o heurística) evalúa qué tan buena es una acción.

Teniendo en cuenta que hay un alto número de combinaciones posibles por pieza un enfoque determinista como Steepest-Ascent, puede dar buenos resultados si se tiene una buena función heurística. Pero si el juego comienza a repetir patrones o se estanca, agregar un poco de aleatoriedad (Stochastic) puede ayudar a evitar ciclos o zonas planas.

## Bibliografía 

Talbi, E.-G. (2009). _Metaheuristics: From design to implementation_. Wiley.

Russell, S., & Norvig, P. (2010). _Artificial intelligence: A modern approach_ (3rd ed.). Prentice Hall.

https://www.almabetter.com/bytes/tutorials/artificial-intelligence/local-search-algorithm-in-artificial-intelligence

https://www.geeksforgeeks.org/machine-learning/difference-between-hill-climbing-and-simulated-annealing-algorithm/

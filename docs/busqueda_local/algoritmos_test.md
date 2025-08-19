# Informe Comparativo Algoritmos de Tetris
___
## Análisis
El objetivo de éste analisis es demostrar y comparar el rendimiento de los distintos 
algoritmos aplicados en el tetris para así sacar conclusiones y evaluar cual es el más óptimo dependiendo las circunstancias. 
Los algoritmos evaluados son:
- Hill Climbing
- Simulated Annealing
- Algoritmo Genetico

Para garantizar condiciones justas, y que todos los algoritmos sean evaluados de manera pareja, se implanto una semilla aleatoria pareja. 
___
## Metodología
Se implementó un sistema de generacion de semillas para que todos los algoritmos recibieran en el mismo orden la misma secuencia de piezas. 
Esta semilla se implemento para asegurarnos de que las diferencias de rendimiento en cuanto a los algoritmos no se deba por las piezas al azar, 
sino de la toma de decisiones del algoritmo. Se realizaron las pruebas en base a la caida de 400 piezas para cada algoritmo 15 veces, es decir, se dejo correr cada algoritmo hasta alcanzar las 400 piezas ubicadas y de ahi se sacaron todas las comparaciones y conclusiones. Este proceso se repitio 15 veces seguidas. 
___
## Métricas evaluadas
Se eligieron las siguientes métricas para luego evaluar los comportamientos y decisiones de los algoritmos. 
- Singles: Cantidad de veces que se elimino 1 linea.
- Dobles: Cantidad de veces que se eliminaron 2 lineas.
- Triples: Cantidad de veces que se eliminaron 3 lineas.
- Nivel Alcanzado: Nivel al que se llegó.
- Puntaje Obtenido: Puntaje final obtenido.
- Tiempo promedio en la toma de decisiones: Promedio entre que aparece la pieza y se elige la posicion a colocarla.
- Consistencia por Algoritmo: Se evaluó el coeficiente de variación.
- Cantidad de piezas: Cantidad de líneas eliminadas por piezas colocadas.

___
## Toma de decisiones algoritmos
- Hill Climbing: Evalúa todos los movimientos posibles y elige el de mayor puntaje heurístico.
- Simulated Annealing: Permite al inicio no aceptar tan buenas posiciones para escapar de optimos locales.
- Genetico: Simula selección natural para encontrar estrategias.
___
## Gráficos Realizados
### Comparación de Singles, Dobles y Triples por Algoritmo
- Hill Climbing es el algoritmo mas efectivo en eliminar lineas constantemente, pero en su mayoria singles. El algoritmo Genético apuesta a jugadas de mayor riesgo, con menos singles pero mas tetrises puntuando alto algunas partidas. Y por último Simulated Annealing queda en el medio. 
- ![Comparacion singles, dobles y  triples](/docs/busqueda_local/images/cant_lineas_eliminadas.png)
___
### Nivel Alcanzado vs Puntaje Obtenido
- Este gráfico relaciona el nivel alcazado con el puntaje promedio. Se observa que Hill Climbing es el que mejor desempeño global obtiene, el genético logra un rendimiento aceptable, y Simulated Annealing queda con el peor resultado.
- ![Nivel vs Puntaje](/docs/busqueda_local/images/puntaje_vs_nivel.png)
___
### Puntaje Total por Algoritmo
- Gráfico de cajas que muestra la distribución de los puntajes obtenidos por los tres algoritmos. Hill Climbing resulta ser el más estable y confiable con resultados altos y consistentes, mientras que el Genético y el Simulated Annealing muestran mayor dispersión, si bien alcanzan puntajes elevados, la variabilidad es alta y los resultados no son predecibles. 
- ![Puntaje Obtenido](/docs/busqueda_local/images/total_puntaje.png)
___
### Puntaje Obtenido vs Tiempo de toma de Decisión
- Gráfico de comparación entre el puntaje promedio y el tiempo promedio de decisión para cada algoritmo. Hill Climbing es el más rápido con mejores resultados, luego le sigue el Genético que consume más tiempo y no obtiene los mejores resultados, y luego el Simulated Annealing que es el que peor rinde, ni con buenos resultados ni puntajes.
- ![Puntaje vs decision](/docs/busqueda_local/images/tiempo_vs_puntaje.png)
___
### Consistencia por Algoritmo
- El siguiente gráfico representa la consistencia de los algoritmos medida a través del coeficiente de variación tanto para el puntaje como para las líneas eliminadas. Mientras menor coeficiente de variación haya mayor consistencia, es decir los resultados de los algoritmos son mas estables entre ejecuciones. Se puede observar que el algoritmo Hill Climbing es el más consistente en puntaje, esto nos dice que aunque no siempre obtenga el mejor rendimiento absoluto, sus resultados tienden a ser mas previsibles. El algoritmo genético muestra mejor consistencia en líneas eliminadas pero es más variable en cuanto al puntaje. Por ultimo el algoritmo simulated annealing es el menos consistente de los tres con mucha variabilidad entre ejecuciones.
- ![Consistencia por algoritmo](/docs/busqueda_local/images/consistencia.png)
___
### Cantidad de líneas eliminadas por piezas colocadas
- Lo que nos devuelve ésta gráfica es que el algoritmo hill climbing logra un uso mas eficiente de cada pieza, sacando más provecho al juego, el algoritmo genético también se comporta bien pero un poco menos, y en cuanto al simulated annealing no optimiza tan bien la colocación de piezas en el entorno del tetris.
- ![Piezas colocadas](/docs/busqueda_local/images/piezas_lineas.png)

## Conclusión
Se realizó una matriz de metricas para evaluar y poder comparar todos los resultados, no solo a nivel de puntaje sino también en eficiencia y calidad de juego. En cuanto a conclusiones individuales se obtuvo: 
- Puntaje Total: Hill Climbing logra el puntaje más alto siendo el más eficaz, seguido por el algoritmo Genético y por ultimo el Simulated Annealing. 
- Tiempor promedio por decision: Todos los algoritmos tienen tiempos similares, con diferencias poco relevantes.
- Lineas eliminadas: El que más elimina es el algoritmo Hill Climbing
- Calidad del tablero: Hill Climbing mantiene una altura máxima más baja y con menores huecos, es decir, el que mejor control del tablero tiene. Los otros algoritmos tienden a dejar más huecos y acumular mayor altura.
- Distribución de eliminaciones: Hill Climbing tiene un equilibrio pero se destaca en eliminar singles, el algoritmo Genético logra mas triples y tetrises aunque sin tanta estabilidad, y por último el algoritmo Simulated Annealing queda en un punto intermedio entre los otros dos.
- Nivel Alcanzado: Hill Climbing es el que alcanza el nivel más alto, en este caso con estas pruebas alcanzando el nivel 15.
- ![Matriz metricas](/docs/busqueda_local/images/heatmap.png)

Por lo tanto, como conclusión final, en terminos globales, el algoritmo Hill Climbing fue el algoritmo más eficaz y consistente para resolver el tetris, alcanzando el mayor puntaje, más líneas eliminadas, menor altura y huecos en el tablero. El algoritmo Genético ofreció un rendimiento intermedio, destacandose en la obtención de tetrises, aunque con mayor variabilidad en los resultados. Por último, Simulated Annealing presento el desempeño más bajo en casi todas las métricas mostrando poca consistencia y eficiencia en comparación a los otros algoritmos. 


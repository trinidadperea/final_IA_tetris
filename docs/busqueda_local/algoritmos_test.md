# Informe Comparativo Algoritmos de Tetris
___
## Analisis
El objetivo de este analisis es demostrar y comparar el rendimiento de los distintos 
algoritmos aplicados en el tetris para asi sacar conclusiones y evaluar cual es el mas optimo dependiendo las circunstancias. 
Los algoritmos evaluados son:
- Hill Climbing
- Simulated Annealing
- Algoritmo Genetico

Para garantizar condiciones justas, y que todos los algoritmos sean evaluados de manera pareja, se implanto una semilla aleatoria pareja. 
___
## Metodologia
Se implemento un sistema de generacion de semillas para que todos los algoritmos recibieran en el mismo orden la misma secuencia de piezas. 
Esta semilla se implemento para asegurarnos de que las diferencias de rendimiento en cuanto a los algoritmos no se deba por las piezas al azar, 
sino de la toma de decisiones del algoritmo. Se realizaron las pruebas en base a la caida de 400 piezas para cada algoritmo 15 veces, es decir, se dejo correr cada algoritmo hasta alcanzar las 400 piezas ubicadas y de ahi se sacaron todas las comparaciones y conclusiones. Este proceso se repitio 15 veces seguidas. 
___
## Metricas evaluadas
Se eligieron las isguientes metricas para luego evaluar los comportamientos y decisiones de los algoritmos. 
- Singles: Cantidad de veces que se elimino 1 linea
- Dobles: Cantidad de veces que se eliminaron 2 lineas
- Triples: Cantidad de veces que se eliminaron 3 lineas
- Nivel Alcanzado: Nivel al que se llego luego de las 100 piezas
- Puntaje Obtenido: Puntaje final obtenido luega de las 100 piezas
- Tiempo promedio en la toma de decisiones: Promedio entre que aparece la pieza y se elige la posicion a colocarla
- Consistencia por Algoritmo: Se evaluo el coeficiente de variacion
- Cantidad de piezas: Piezas ubicadas por cada algoritmo

___
## Toma de decisiones algoritmos
- Hill Climbing: Evalua toos los movimientos posibles y elige el de mayor puntaje heuristico.
- Simulated Annealing: Permite al inicio no aceptar tan buenas posiciones para escapar de optimos locales.
- Genetico: Simula seleccion natural para encontrar estrategias.
___
## Graficos Realizados
### Comparacion de Singles, Dobles y Triples por Algoritmo
- Se obtiene y se puede observar que el algoritmo genetico es el que mas se enfoca en eliminar triples
- ![Comparacion singles, dobles y  triples](/docs/busqueda_local/images/lineas_eliminadas.png)
___
### Nivel Alcanzado vs Puntaje Obtenido
- Los tres algoritmos alcanzaron el mismo nivel, pero se puede observar como el Simulated Annealing es el que mejor puntaje obtiene al final
- ![Nivel vs Puntaje](/docs/busqueda_local/images/nivel_vs_puntaje.png)
___
### Puntaje Total por Algoritmo
- Se observa que por mas que en este ejemplo, luego de 100 piezas colocadas, el que mejor puntaje obtiene es el Simulated Annealing
- ![Puntaje Obtenido](/docs/busqueda_local/images/puntaje_total.png)
___
### Puntaje Obtenido vs Tiempo de toma de Decision
- El tiempo promedio de decision mas rapido es el Algoritmo Genetico pero comparandolo con los resultados, no obtiene los mejores. Luego el segundo algoritmo mas rapido a la
hora de la toma de decisiones es el Simulated Annealing, obteniendo el mayor puntaje entre los tres, y por ultimo el mas lento es el Hill Climbing, pero obtiene un puntaje final aceptable.
- ![Puntaje vs decision](/docs/busqueda_local/images/puntaje_vs_tiempo.png)
___
### Consistencia por Algoritmo
- El siguiente grafico representa la consistencia de los algoritmos medida a traves del coeficiente de variación tanto para el puntaje como para las lineas eliminadas. Mientras menor coeficiente de variación haya mayor consistencia, es decir los resultados de los algoritmos son mas estables entre ejecuciones. Se puede observar que el algoritmo Hill Climbing es el mas consistente en puntaje, esto nos dice que aunque no siempre obtenga el mejor rendimiento absoluto, sus resultados tienden a ser mas previsibles. El algoritmo genético muestra mejor consistencia en lineas eliminadas pero es mas variable en cuanto al puntaje. Por ultimo el algoritmo simulated annealing es el menos consistente de los tres con mucha variabilidad entre ejecuciones.
- ![Consistencia por algoritmo](/docs/busqueda_local/images/consistencia.png)
___
### Cantidad de lineas eliminadas por piezas colocadas
- Lo que nos devuelve esta grafica es que el algoritmo hill climbing logra un uso mas eficiiente de cada pieza, sacando mas provecho al juego, el algoritmo genetico tambien se comporta bien pero un poco menos, y en cuanto al simulated annealing no optimiza tqan bien la colocacion de piezas en el entorno del tetris.
- ![Piezas colocadas](/docs/busqueda_local/images/piezas_lineas.png)

## Conclusion
Se realizo una matriz de metricas para evaluar y poder comparar todos los resultados, no solo a nivel de puntaje sino tambien en eficiencia y calidad de juego. En cuanto a conclusiones individuales se obtuvo: 
- Puntaje Total: Hill Climbing logra el puntaje mas alto siendo el mas eficaz, seguido por el algoritmo Genético y por ultimo el Simulated Annealing. 
- Tiempor promedio por decision: Todos los algoritmos tienen tiempos similares, con diferencias poco relevantes.
- Lineas eliminadas: El que mas elimina es el algoritmo Hill Climbing
- Calidad del tablero: Hill Climbing mantiene una altura maxima mas baja y con menores huecos, es decir, el que mejor control del tablero tiene. Los otros algoritmos tienden a dejar mas huecos y acumular mayor altura.
- Distribucion de eliminaciones: Hill Climbing tiene un equilibrio pero se destaca en eliminar singles, el algoritmo Genético logra mas triples y tetrises aunque sin tanta estabilidad, y por ultimo el algoritmo Simulated Annealing queda en un punto intermedio entre los otros dos.
- Nivel Alcanzado: Hill Climbing es el que alcanza el nivel mas alto, en este caso con estas pruebas alcanzando el nivel 15.
- ![Matriz metricas](/docs/busqueda_local/images/heatmap.png)

Por lo tanto, como conclusion final, en terminos globales, el algoritmo Hill Climbing fue el algoritmo mas eficaz y consistente para resolver el tetris, alcanzando el mayor puntaje, mas lineas eliminadas, menor altura y huecos en el tablero. El algoritmo Genético ofrecio un rendimiento intermedio, destacandose en la obtencion de tetrises, aunque con mayor variabilidad en los resultados. Por último, Simulated Annealing presento el desempeño mas bajo en casi todas las métricas mostrando poca consistencia y eficiencia en comparación a los otros algoritmos. 


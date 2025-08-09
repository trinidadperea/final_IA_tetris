# Informe Comparativo Algoritmos de Tetris
___
## Analisis
El objetivo de este analisis es demostrar y comparar el rendimiento de los distintos 
algoritmos aplicados en el tetris para asi sacar conclusiones y evaluar cual es el mas optimo dependiendo las circunstancias. 
Los algoritmos evaluados son:
- Hill Climbing
- Simulated Annealing
- Algoritmo Genetico

Para garantizar condiciones justas, y que todos los algoritmos sean evaluados de manera pareja, fse implanto una semilla aleatoria pareja. 
___
## Metodologia
Se implemento un sistema de generacion de semillas para que todos los algoritmos recibieran en el mismo orden la misma secuencia de piezas. 
Esta semilla se implemento para asegurarnos de que las diferencias de rendimiento en cuanto a los algoritmos no se deba por las piezas al azar, 
sino de la toma de decisiones del algoritmo. Se realizaron las pruebas en base a la caida de 100 piezas, es decir, se dejo correr caa algoritmo hasta alcanzar 
las 100 piezas ubicadas y de ahi se sacaron todas las comparaciones y conclusiones.
___
## Metricas evaluadas
Se eligieron las isguientes metricas para luego evaluar los comportamientos y decisiones de los algoritmos. 
- Singles: Cantidad de veces que se elimino 1 linea
- Dobles: Cantidad de veces que se eliminaron 2 lineas
- Triples: Cantidad de veces que se eliminaron 3 lineas
- Nivel Alcanzado: Nivel al que se llego luego de las 100 piezas
- Puntaje Obtenido: Puntaje final obtenido luega de las 100 piezas
- Tiempo promedio en la toma de decisiones: Promedio entre que aparece la pieza y se elige la posicion a colocarla
___
## Toma de decisiones algoritmos
- Hill Climbing: Evalua toos los movimientos posibles y elige el de mayor puntaje heuristico.
- Simulated Annealing: Permite al inicio no aceptar tan buenas posiciones para escapar de optimos locales.
- Genetico: Simula seleccion natural para encontrar estrategias.
___
## Graficos Realizados
### Comparacion de Singles, Dobles y Triples por Algoritmo
- Se obtiene y se puede observar que el algoritmo genetico es el que mas se enfoca en eliminar triples
- ![Comparacion singles, dobles, triples](/docs/busqueda_local/images/lineas_eliminadas.png)
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

## Conclusion


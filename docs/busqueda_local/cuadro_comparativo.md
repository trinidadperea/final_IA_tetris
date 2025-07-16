# Cuadro comparativo entre los algoritmos de búsqueda local teniendo en cuenta parámetros relevantes para desarrollo del proyecto

| Parámetro | Hill Climbing | Simulated Annealing | Algoritmo Genético |
|-----------|:-------------:|:-------------------:|:------------------:|
| **Tipo de búsqueda** | Búsqueda local determinística: siempre elige la mejor opción inmediata. | Búsqueda local probabilística: permite aceptar soluciones peores al inicio, simulando el enfriamiento de metales. | Búsqueda poblacional inspirada en la evolución biológica: trabaja con una población de soluciones que evolucionan. |
| **Capacidad de escapar de óptimos locales** | Baja: se queda atrapado si no hay vecinos mejores. | Alta: puede aceptar soluciones peores para escapar de óptimos locales. | Alta: la diversidad genética permite explorar múltiples regiones del espacio de búsqueda. |
| **Exploración vs. explotación** | Explotación fuerte: enfocado solo en mejorar. | Equilibrio controlado por la temperatura: más exploración al principio, más explotación al final. | Alta exploración: combina cruce y mutación para generar variedad. |
| **Uso de aleatoriedad** | Mínimo: solo si se elige aleatoriamente entre vecinos iguales. | Moderado: usa aleatoriedad para seleccionar vecinos y aceptar soluciones peores. | Alto: la selección, cruce y mutación son procesos estocásticos. |
| **Dependencia de parámetros** | Baja: solo depende de la función heurística. | Media: necesita definir temperatura inicial, tasa de enfriamiento, criterio de parada. | Alta: muchos parámetros influyen (tamaño de población, tasas de mutación/cruce, elitismo, etc.). |
| **Costo computacional** | Bajo: rápido y simple, apto para decisiones en tiempo real. | Medio: más costoso por evaluar múltiples vecinos y usar funciones probabilísticas. | Alto: evalúa múltiples soluciones por generación y realiza operaciones genéticas. |
| **Aplicabilidad en tiempo real (como en un juego)** | Alta: ideal para entornos con decisiones rápidas como Tetris. | Media: puede adaptarse, pero necesita buen ajuste de parámetros para que sea ágil. | Baja-media: requiere optimización o simplificación para usarse en tiempo real. |
| **Complejidad de implementación** | Baja: se implementa fácilmente con pocos pasos. | Media: requiere lógica de temperatura, aceptación probabilística y enfriamiento. | Alta: implica manejar estructuras de población, operadores genéticos y ciclos evolutivos. |

## Bibliografía
Talbi, E.-G. (2009). _Metaheuristics: From design to implementation_. Wiley.

Russell, S., & Norvig, P. (2010). _Artificial intelligence: A modern approach_ (3rd ed.). Prentice Hall.
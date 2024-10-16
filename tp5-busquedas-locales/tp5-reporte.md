---
title: tp5-reporte

---

# Reporte Nahman Martina
## Introducción
Este informe es realizado con el fin de exponer de manera escrita la implementación al siguiente problema:
1. Implementar un algoritmo de Hill Climbing para resolver el problema de las N−reinas. 
2. Implementar el algoritmo Simulated Annealing para resolver el problema del ejercicio 1.
3. Implementar un algoritmo genético para resolver el problema del ejercicio 1. Además de la
implementación en código del mismo, se deberán incluir detalles respecto a:
a) Definición de los individuos de la población.
b) Estrategia de selección.
c) Estrategia de reemplazo.
d) Operadores.
## Marco Teórico
### Algoritmos de búsqueda local
Son útiles cuando al agente solo le importa el **estado objetivo** y NO la secuencia de estados para llegar al objetivo.Seguimos trabajando bajo un entorno, observable, deterministico y estático. Los mismos no realizan una exploración sistemática del espacio de estados. Evalúan y modifican un estado o un conjunto reducido de estados → se mueven entre estados “vecinos”
### Hill Climbing 
Es un algoritmo iterativo que comienza con una solución arbitraria a un problema, luego intenta encontrar una mejor solución variando incrementalmente un único elemento de la solución. Si el cambio produce una mejor solución, otro cambio incremental se le realiza a la nueva solución, repitiendo este proceso hasta que no se puedan encontrar mejoras.
### Simulated Annealing
Es un algoritmo de búsqueda metaheurística para problemas de optimización global; el objetivo general de este tipo de algoritmos es encontrar una buena aproximación al valor óptimo de una función en un espacio de búsqueda grande. Dicho "óptimo global" corresponde a la solución del problema de interés para el que no existe un mejor valor. En el caso de que tal problema sea de minimización, el óptimo global será aquél para el cual la función objetivo tenga el más pequeño posible de todos los de su (espacio de búsqueda) Por el contrario, para un problema de maxización, el óptimo global es aquél con el valor más alto posible.
### Algoritmos genéticos
Un algoritmo genético (GA) es un método de optimización inspirado en los procesos de selección natural y evolución biológica. Funciona simulando la evolución de soluciones potenciales a un problema, buscando la mejor solución posible a través de iteraciones o generaciones. Los pasos clave son:

1. Población inicial: Se genera un conjunto de posibles soluciones (individuos).
2. Evaluación (fitness): Se mide la calidad de cada solución con respecto al problema (función de evaluación o fitness).
3. Selección: Se eligen las mejores soluciones para reproducirse, emulando la supervivencia del más apto.
4. Cruce (crossover): Se combinan dos soluciones para generar una nueva (hijo) con características de ambos padres.
5. Mutación: Se hacen pequeños cambios aleatorios en algunos individuos para mantener diversidad genética.
6. Reemplazo: Las nuevas soluciones reemplazan algunas o todas las soluciones anteriores en la población.
7. Iteración: Se repiten los pasos hasta que se cumple un criterio de parada (como alcanzar una solución óptima o llegar a un número máximo de generaciones).

El objetivo de un GA es encontrar la solución más óptima de manera eficiente, simulando un proceso de evolución.

## Diseño experimental
### Descripción experimentos

En este trabajo, se implementaron y compararon tres algoritmos: Hill Climbing (HC), Simulated Annealing (SA) y un Algoritmo Genético (GA), con el objetivo de resolver el problema de las N-reinas. El objetivo es minimizar el número de conflictos entre las reinas en el tablero, representado por la función H, que cuenta el número de pares de reinas que se atacan entre sí.

Los experimentos se realizaron sobre valores de N {4, 8, 10, 12, 15}, con 30 ejecuciones por cada valor de N para obtener estadísticas confiables. Las evaluaciones máximas fueron 1000 por cada ejecución de HC y SA, mientras que en GA se ejecutaron 1000 generaciones con una población de tamaño 100.

Para Hill Climbing, se generaron vecinos cambiando la posición de una reina en el tablero y se seleccionó siempre el vecino con el menor H. Si no había mejoras, el algoritmo se detenía.

En Simulated Annealing, se utilizó una función exponencial para aceptar soluciones peores con cierta probabilidad controlada por una temperatura decreciente con cada iteración. La función de aceptación fue: 

**P**=e^(−ΔH/T) donde **ΔH** es el cambio en la función H y** 𝑇** es la temperatura.

El Algoritmo Genético utilizó una población de tableros (individuos) donde cada individuo representa una posible solución al problema. Se implementó un operador de cruce de un punto y mutación aleatoria. La selección se realizó mediante ruleta proporcional al fitness inverso de H, y la evaluación de generaciones continuaba hasta encontrar una solución óptima o alcanzar el número máximo de generaciones.

## Análisis de datos

Los resultados obtenidos se presentan en las tablas y gráficas adjuntas, comparando los tres algoritmos en términos de:

1. Porcentaje de éxito: porcentaje de ejecuciones que alcanzaron una solución óptima (H=0).
2. Tiempo de ejecución: tiempo promedio en segundos hasta encontrar la solución o agotar las evaluaciones.
3. Estados evaluados: cantidad de estados generados durante la búsqueda.

**Hill Climbing** mostró un desempeño aceptable para valores pequeños de N (N=4, N=8), pero su porcentaje de éxito disminuye drásticamente a medida que N aumenta, debido a que frecuentemente se estanca en óptimos locales. Esto se refleja en que el número de estados evaluados es bajo en comparación con los otros algoritmos.

**Simulated Annealing** fue más robusto, logrando soluciones óptimas en un mayor porcentaje de ejecuciones, especialmente para valores intermedios de N (N=8, N=10). La función de temperatura permitió escapar de óptimos locales en algunas ejecuciones, pero su eficiencia decrece conforme aumenta N.

El **Algoritmo Genético** fue el más efectivo en términos de porcentaje de éxito, alcanzando soluciones óptimas en la mayoría de las ejecuciones para todos los valores de N. El proceso de selección y cruce mantuvo una diversidad en la población, lo que permitió explorar más el espacio de soluciones, a costa de un mayor número de evaluaciones.

Se observaron distribuciones diferentes en los tiempos de ejecución: Hill Climbing fue el *más rápido* pero el menos efectivo, mientras que el Algoritmo Genético fue *más lento* debido a las múltiples generaciones evaluadas.

Se incluyen boxplots para visualizar la distribución de tiempos de ejecución y estados evaluados para cada algoritmo y valor de N. Además, gráficas con respecto a la funcion H.

## Conclusión
Los experimentos realizados demostraron que, si bien Hill Climbing es un algoritmo rápido, no es adecuado para valores grandes de N debido a su tendencia a estancarse en óptimos locales. Simulated Annealing mejora este comportamiento gracias a su capacidad de aceptar soluciones peores bajo ciertas condiciones, pero su efectividad decrece para problemas más complejos.

El Algoritmo Genético mostró ser el método más robusto para resolver el problema de las N-reinas, logrando soluciones óptimas en la mayoría de las ejecuciones, aunque su tiempo de ejecución fue mayor debido al proceso de selección, cruce y mutación.

En resumen, la elección del algoritmo depende del tamaño del problema y de los recursos computacionales disponibles. Para problemas grandes donde se prioriza la exactitud, el Algoritmo Genético es el más adecuado, mientras que para problemas pequeños y tiempo limitado, Hill Climbing puede ser suficiente.


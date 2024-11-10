---
title: tp6-reporte

---

# Reporte Nahman Martina - TP6 CSP

### 1. Describir en detalle una formulación CSP para el Sudoku.

* Variables:
En el Sudoku, las variables representan las celdas del tablero. Un tablero de Sudoku estándar es de 9x9, por lo que se definen 81 variables (con valores entre 1 y 9), una para cada celda. Las variables se pueden denotar como VijVij, donde ii y jj son los índices de la fila y la columna de la celda correspondiente, respectivamente.
* Dominio:
El dominio de cada variable VijVij es el conjunto de posibles valores que la celda puede tomar. En el Sudoku, los valores permitidos son los números del 1 al 9, por lo que el dominio de cada variable es Dij={1,2,3,4,5,6,7,8,9}Dij={1,2,3,4,5,6,7,8,9}.
Si alguna celda del Sudoku ya está llena (es decir, el número ya está determinado), el dominio de esa variable se reduce a un solo valor (el valor dado en la celda).
 Restricciones:

* Restricción de filas:
Cada fila debe contener números del 1 al 9 sin repetir.

* Restricción de columnas: 
Similar a las filas, cada columna debe contener números del 1 al 9 sin repetir.

* Restricción de subcuadrículas (bloques 3x3):
El tablero de Sudoku se divide en 9 bloques de 3x3, y cada bloque debe contener los números del 1 al 9 sin repetir. 

### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignaci´on parcial WA=red, V=blue para el problema de colorear el mapa de Australia


En este ejercicio, se utiliza el algoritmo AC-3 para detectar la inconsistencia de la asignación parcial WA = Red y V = Blue en el problema de colorear el mapa de Australia. El objetivo es comprobar si esta asignación cumple las restricciones del problema o si resulta en una situación sin solución.
Paso 1: Dominio inicial

    D(WA) = {R}
    D(V) = {B}
    D(NT), D(SA), D(Q), D(NSW) = {R, B, G}

Paso 2: Verificación de arcos

El algoritmo AC-3 revisa pares de regiones adyacentes y elimina valores inconsistentes de sus dominios. Los pasos clave son:

    SA -> WA: Se elimina RR de SASA, dejando D(SA) = {B, G}.
    SA -> V: Se elimina BB de SASA, dejando D(SA) = {G}.
    NT -> SA: Se elimina GG de NTNT, dejando D(NT) = {R, B}.
    NSW -> V: Se elimina BB de NSWNSW, dejando D(NSW) = {R, G}.
    NSW -> SA: Se elimina GG de NSWNSW, dejando D(NSW) = {R}.
    Q -> NSW: Se elimina RR de QQ, dejando D(Q) = {B, G}.
    Q -> SA: Se elimina GG de QQ, dejando D(Q) = {B}.
    NT -> Q: Se elimina BB de NTNT, dejando D(NT) = {R}.
    NT -> WA: Se elimina RR de NTNT, dejando D(NT) = { }.

Conclusión

Al llegar al paso final, el dominio de NT queda vacío, lo que indica que la asignación parcial es inconsistente y no es posible encontrar una solución para este problema bajo esas condiciones.

### 3. ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un ´arbol estructurado CSP?

La complejidad en el peor caso del algoritmo AC-3 es O(E⋅D²), donde:

    E es el número de aristas (o arcos).
    D es el tamaño máximo de los dominios de las variables.
    
### 4. AC-3 coloca de nuevo en la cola todo arco (Xk,Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk,Xi) se puede llevar la cuenta del n´umero de valores restantes de Xi que sean consistentes con cada valor de Xk. Explicar cómo actualizar ese n´ umero de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(N² * D²).
Para cada valor de Xi, mantenemos un registro de las variables Xk para las que un arco de Xk a Xi se satisface con ese valor concreto de Xi. Esto puede calcularse en un tiempo proporcional al tamaño de la representación del problema. Entonces, cuando se elimina un valor de Xi, reducimos en 1 el conteo de valores permitidos para cada arco (Xk, Xi) registrado bajo ese valor.
### 5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (secci´on 6.5, AIMA 3ra edición). Para ello, demostrar: 
* **a) Para un CSP cuyo grafo de restricciones es un árbol, la 2-consistencia (consistencia de arco) implica n−consistencia, siendo n el número total de variables.**
Un CSP tiene n-consistencia cuando, para cada subconjunto de variables de tamaño menor o igual a n, cualquier asignación a esas variables puede extenderse a una asignación consistente para una variable adicional. La 2-consistencia implica que cada variable es consistente con las variables conectadas a ella (vecinos). Además, la estructura de árbol permite que cualquier subconjunto de k variables (con k < n) que sea consistente puede extenderse a la siguiente variable en el orden del árbol.
Dado que los árboles no contienen ciclos, no hay conflictos que puedan requerir la reconsideración de las asignaciones previas. Por lo tanto, la 2-consistencia es suficiente para garantizar la n-consistencia.
* **b) Argumentar por qué lo demostrado en 5a es suficiente.**
Ya que cada subconjunto de variables puede extenderse a una asignación consistente para la siguiente variable en el árbol (por su estructura), y dado que el árbol se puede recorrer sin necesidad de retroceder, la 2-consistencia es suficiente para asegurar que se pueden satisfacer todas las restricciones sin necesidad de verificar subconjuntos más grandes.
### 6.  Implementar una solución al problema de las N−reinas utilizando una formulación CSP
A continuación se presentan dos gráficos para poder representar en términos de estados y tiempo las distintas ejecuciones. 
#### Gráfico 1: 
![STATES]([https:// "title"](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp6-csp/images/states/boxplot_estados_N15.png))
En el gráfico 1 se puede visualizar la cantidad de estados explorados para un N=15. Vemos que la cantidad para ambos algoritmos es de 105 aprox. 

#### Gráfico 2: 
![TIME]([https:// "title"](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp6-csp/images/time/boxplot_tiempo_N15.png))
    
En el gráfico 2 se puede visualizar el tiempo empleado por los algoritmos en la ejecución del problema para un N=15 también.

Vemos que Forward Cheking es notablemente más veloz respecto al Backtracking para este N. 

### 7. Comparativa tp5

Las comparaciones se hicieron respecto a un N=15 para todos los algoritmos: Simulated Annealing,  Hill Climbing, algoritmo genético, backtracking CSP y forward checking.

Backtracking y forward checking,  al ser algoritmos de búsqueda exhaustiva, son mucho más eficientes en la exploración del espacio de búsqueda que los algoritmos heurísticos. Los algoritmos heurísticos exploran un espacio mucho más amplio, buscando una solución "buena" en lugar de óptima, lo que puede resultar en la evaluación de muchos estados no prometedores.

 Las gráficas revelan que backtracking y forward checking tienen tiempos de ejecución significativamente menores que los algoritmos heurísticos. Al igual que con los estados evaluados, la diferencia en la escala de las gráficas es enorme, lo que indica un mejor desempeño para backtracking y forward checking

---
title: tp3y4-reporte

---

# Reporte Nahman Martina
## Introducción 
Este informe es realizado con el fin de exponer de manera escrita la implementación al siguiente problema:
1. Dado el entorno FrozenLake y los entornos deterministas aleatorios de 100x100, implementar un agente que resuelva el problema planteado mediante un algoritmo de búsqueda **NO INFORMADA:** BFS, DFS, DLS y UCS. Además, resuelva también para el algoritmo de búsqueda **INFORMADA:** A* 
2. Ejecutar un total de 30 veces cada algoritmo en escenarios aleatorios con las características descriptas en el ejercicio 1. Evaluar cada uno de los algoritmos sobre los mismos entornos generados.
a) Calcular la media y la desviación estándar de:
* Cantidad de estados explorados para llegar al objetivo (si es que fue posible).
* Costo total de las acciones tomadas para las soluciones obtenidas.
* Tiempo empleado (segundos).
b) Presentar los resultados en gráficos de cajas y bigotes.
3. Repetir el procedimiento descrito en el ejercicio anterior, para el caso de un agente con comportamiento aleatorio. Esto es, el agente elige cada una de sus acciones al azar.
## Marco teórico
### Agentes inteligentes
Dentro de los agentes inteligentes, en este caso nos centraremos específicamente en uno.
### Tipo de agente: Agente basado en objetivos
Un objetivo puede verse como un **conjunto de estados** del mundo (exactamente aquellos estados que satisfacen el objetivo). 

La tarea del agente es encontrar/buscar qué **secuencia de acciones** permite obtener un estado objetivo.

El primer paso para solucionar un problema es la **formulación del objetivo**, basado en la situación actual y la **medida de rendimiento** del agente. El segundo paso consiste en **buscar** la secuencia de acciones que nos permitan llegar al objetivo (solucion). Y el tercer paso es **ejecutar** la secuencia de acciones.

Los agentes resuelve problemas ***solo*** funcionan bajo ambientes:
* Estáticos
* Observables
* Deterministas
* Discretos
### Formulación del problema
1. Estado inicial
2. Función sucesor
3. Espacio de estados
4. Función de evalución del objetivo
5. Función de costo
### Búsqueda de la solución
1. Se utiliza un árbol (o grafo) de búsqueda explícito generado por el estado inicial y la función sucesor, definiendo así el espacio de estados.
2. Por cada nodo, se genera mediante la función sucesor los estados posibles del espacio de estado
3. Cada nodo contiene información sobre el estado, sumado a posiblemente otra información como podría ser Padre, Acción que se aplicará al Padre, costo, Profundidad, etc.

En este caso, se utilizaron los siguientes grafos de búsqueda para resolver el problema: 
* Búsqueda en Anchura
* Búsqueda de costo uniforme 
* Búsqueda en Profundidad
* Búsqueda en profundidad Limitada
## Diseño experimental
### Medida de rendimiento
La medida de rendimiento en este experimento es la cantidad de estados explorados para llegar al objetivo. Esta métrica refleja qué tan eficaz es el agente en cumplir su objetivo en un entorno específico.
### Configuraciones del entorno
Para evaluar el rendimiento de los agentes, se utilizaron distintas configuraciones del entorno **Frozen Lake**, modificando parámetros como el tamaño del mapa, la proporción de huecos (posiciones peligrosas) y la posición inicial del agente.

### Programación del entorno
Se creó una clase llamada *"Environment"* para gestionar la generación de diferentes configuraciones de entornos aleatorios y controlados, con el objetivo de facilitar la experimentación.

En particular, se desarrolló la función *generate_random_map_custom*, la cual permite generar un mapa aleatorio de tamaño variable, con una proporción ajustable de casilleros peligrosos ("H" - huecos) y casilleros seguros ("F" - congelados). Esta función también asegura que el agente y el objetivo no se ubiquen en huecos, manteniendo la viabilidad de la exploración.

Para controlar la posición inicial del agente, se implementó la clase *CustomFrozenLakeEnv*, que extiende la funcionalidad de la clase base de Gym y permite definir una posición inicial específica para el agente. Además, se integró un **wrapper** de TimeLimit para limitar el número máximo de pasos que puede realizar el agente, evitando bucles infinitos y asegurando la consistencia en las pruebas.

Este diseño permite la personalización y control de los entornos experimentales de manera reproducible mediante el uso de semillas, lo cual es crucial para la evaluación y comparación del rendimiento de diferentes algoritmos de búsqueda.

### Configuración de nodos
La clase Nodo es la estructura básica utilizada para representar los estados dentro del entorno de búsqueda. Cada nodo contiene la información necesaria para rastrear el estado actual del agente, la acción que llevó al agente a este nodo, el nodo padre (el nodo anterior en el recorrido), y el costo del camino acumulado (path cost).
### Programación del Nodo
La clase Nodo se diseñó con los siguientes atributos clave:

* estado: Representa la posición actual del agente en el entorno.
* parent: Nodo padre desde el cual se llegó al nodo actual, lo que permite rastrear el camino recorrido.
* action_number: La acción realizada en el nodo padre para llegar al nodo hijo.
* path_cost: Costo acumulado para llegar a este nodo desde el nodo inicial. 
El método *goal_test* permite verificar si el nodo actual corresponde al estado objetivo, mientras que *_ lt _* facilita la comparación entre nodos según el costo del camino, permitiendo su uso en estructuras como **colas de prioridad**.

### Generación de acciones posibles
Uno de los aspectos más importantes de la clase Nodo es el método *possible_actions*, que genera una lista de acciones posibles desde el estado actual. Este método revisa las posiciones adyacentes (derecha, izquierda, arriba, abajo) y verifica si estas posiciones son seguras (es decir, que no sean huecos representados por 'H') dentro del entorno. De esta manera, se devuelve una lista de acciones viables y los números asociados a cada acción para indicar las direcciones correspondientes (por ejemplo, derecha = 2, izquierda = 0, etc.).

Se incluye también una versión alternativa del método, *possible_actions_p*, que devuelve las acciones posibles junto con el número total de acciones viables desde la posición actual. Este método es útil para algoritmos que requieren conocer la cantidad de posibles movimientos antes de evaluar las acciones individuales.

Ambos métodos garantizan que el agente no se mueva a posiciones peligrosas y puedan ser fácilmente integrados con algoritmos de búsqueda.

### Integración con algoritmos de búsqueda
La estructura de la clase Nodo es **esencial** para implementar algoritmos como Búsqueda en Profundidad, Búsqueda de Costo Uniforme, A*, etc. La capacidad de rastrear el estado, registrar las acciones y calcular el costo acumulado permite a los algoritmos operar de manera eficiente y orientada a los objetivos dentro del entorno Frozen Lake.
### Implementación A*
Para la implementación del algoritmo A*, se seleccionó la heurística de Manhattan, la cual calcula la suma de las distancias horizontales y verticales desde la posición actual de cada ficha hasta su posición objetivo. Esta elección se basó en su adecuación al problema, ya que proporciona un equilibrio eficiente entre el tiempo de ejecución y la simplicidad de cálculo, haciendo que sea una de las heurísticas más apropiadas para este tipo de entornos.P
### Cantidad de repeticiones
Para garantizar que los resultados sean estadísticamente significativos y no dependan de una configuración inicial específica, cada experimento se repite 30 veces en 30 entornos distintos. Esto se realiza tanto para el agente inteligente en cada uno de los algoritmos de búsqueda como para el agente aleatorio. Al repetir los experimentos varias veces con diferentes posiciones iniciales del agente y entornos, se obtiene un promedio del rendimiento de cada agente en esas condiciones.

## Análisis de datos
Los datos recopilados de las repeticiones de cada experimento fueron analizados calculando los promedios de rendimiento para cada configuración del entorno y su desviación estándar. Este enfoque estadístico permite obtener una visión general de cómo las variables del entorno afectan el comportamiento y la efectividad de los agentes.

### Gráfico 1: BFS
![DATOS BFS](https://hackmd.io/_uploads/S1NzrPypC.png)
Resultados de 30 iteraciones del algoritmo BFS. Se puede observar la cantidad de estados explorados, el costo del primer escenario, el costo del segundo escenario y el tiempo empleado.
### Gráfico 2: DFS
![DATOS DFS](https://hackmd.io/_uploads/B1mNHDJTA.png)
Resultados de 30 iteraciones del algoritmo DFS. Se puede observar la cantidad de estados explorados, el costo del primer escenario, el costo del segundo escenario y el tiempo empleado.
### Gráfico 3: DLS
![DATOS DLS](https://hackmd.io/_uploads/BywSBwyaA.png)
Resultados de 30 iteraciones del algoritmo DLS. Se puede observar la cantidad de estados explorados, el costo del primer escenario, el costo del segundo escenario y el tiempo empleado.
### Gráfico 4: UCS
![DATOS UCS](https://hackmd.io/_uploads/ryVFSPk6R.png)
Resultados de 30 iteraciones del algoritmo UCS. Se puede observar la cantidad de estados explorados, el costo del primer escenario, el costo del segundo escenario y el tiempo empleado.
### Gráfico 5: A*
![DATOS A_STAR](https://hackmd.io/_uploads/B1c9Bvy6C.png)
Resultados de 30 iteraciones del algoritmo A*. Se puede observar la cantidad de estados explorados, el costo total y el tiempo empleado.
### Gráfico 6: Agente aleatorio
![DATOS AGENTE ALEATORIO](https://hackmd.io/_uploads/r1TtUP1TA.png)
Resultados de 30 iteraciones del agente aleatorio. Se puede observar la cantidad de estados explorados, el costo del primer escenario, el costo del segundo escenario y el tiempo empleado.

A simple vista, podemos determinar que el A* es el que más se destaca respecto a los demás. Además, en algunos casos como es en DLS no se encontró solución alguna. 
## Conclusión
El algoritmo A* se destaca frente a BFS, DFS, DLS y UCS debido a su capacidad de combinar tanto el costo del camino recorrido como una estimación de la distancia restante hacia el objetivo, utilizando una heurística. Esto lo hace más eficiente en problemas donde se busca no solo alcanzar el objetivo, sino hacerlo de la manera más óptima en términos de costo.

A* se distingue por su capacidad de enfocarse hacia la solución más prometedora gracias a la heurística, lo que le permite explorar menos estados y llegar más rápidamente al objetivo con un menor costo total, optimizando tanto el tiempo de ejecución como los recursos de procesamiento. Esto lo convierte en una opción superior cuando se requiere eficiencia y optimalidad en la resolución de problemas de búsqueda.





---
title: tp2-reporte

---

# Reporte Nahman Martina
## Introducción 
Este informe es realizado con el fin de exponer de manera escrita la implementación al siguiente problema:
1. Evaluar los desempeños de un agente reflexivo y un agente aleatorio bajo distintos entornos y porcentajes de suciedad en el ambiente. 
* Entornos de: 2 × 2, 4 × 4, 8 × 8, 16 × 16, 32 × 32, 64 × 64, 128 × 128.
* Porcentaje de suciedad en el ambiente: 0.1, 0.2, 0.4, 0.8

## Marco teórico
### Agentes y entornos
Un **agente** es cualquier cosa que puede percibir su entorno a través de sensores y actuar sobre él mediante actuadores. Un agente puede ser un humano, un robot, o un software que simula comportamientos inteligentes. El rendimiento de un agente se mide en función de cómo sus acciones logran un objetivo en un entorno dado.

En esta simulación, el entorno es un espacio bidimensional dividido en una cuadrícula de celdas, algunas de las cuales están sucias. El agente, representando una aspiradora automática, se mueve por la cuadrícula y limpia las celdas sucias.
### Tipos de agentes
Existen diferentes tipos de agentes en inteligencia artificial:

**Agente Reflexivo Simple:** Este tipo de agente toma decisiones basadas únicamente en la percepción actual del entorno, sin tener en cuenta el historial o el estado futuro. En este caso, el agente aspiradora simplemente revisa si la celda actual está sucia y, si lo está, la limpia.

**Agente Aleatorio:** Este agente selecciona sus acciones al azar, sin ninguna lógica específica, lo que generalmente lleva a un rendimiento bajo en entornos donde se espera que haya una optimización de las acciones.
### Elementos del entorno
**Dimensión de la cuadrícula:** Se trata del tamaño del entorno, definido en términos de filas y columnas. En esta simulación, la dimensión se establece al inicio y permanece constante.

**Distribución de la suciedad:** La suciedad se distribuye aleatoriamente en las celdas del entorno al inicio de la simulación. Cada celda tiene una probabilidad de estar sucia dependiendo de la tasa de suciedad (dirt_rate) definida por el usuario.

**Posición inicial del agente:** La posición inicial del agente también se determina aleatoriamente en la cuadrícula al comienzo de la simulación.
### Medida de rendimiento
La medida de rendimiento evalúa qué tan bien el agente cumple su objetivo en el entorno. En esta simulación, el rendimiento se mide por la cantidad de celdas sucias que el agente logra limpiar durante su "vida" de 1000 acciones. Cada celda limpiada incrementa el rendimiento del agente en un punto.
### Acciones y percepciones
Las acciones disponibles para el agente son Arriba, Abajo, Izquierda, Derecha, Limpiar, y NoHacerNada. Estas acciones permiten al agente moverse dentro de la cuadrícula y realizar la tarea de limpieza. El agente percibe su entorno a través de la información sobre la suciedad de la celda en la que se encuentra y la posibilidad de moverse dentro de los límites de la cuadrícula
## Diseño experimental
### Medida de rendimiento
La medida de rendimiento en este experimento es la cantidad de celdas que el agente logra limpiar durante su "vida" de 1000 acciones. Cada celda limpia añade un punto al rendimiento total del agente. Esta métrica refleja qué tan eficaz es el agente en cumplir su objetivo en un entorno específico.
### Configuraciones del entorno
Para evaluar el desempeño de los agentes, se experimentó con diferentes configuraciones del entorno. Las configuraciones incluyen:

**Tamaño de la cuadrícula:** Se permite al usuario definir el tamaño de la cuadrícula en cada simulación. Esto puede variar, por ejemplo, desde una cuadrícula pequeña de 2x2 hasta una cuadrícula grande de 128x128 o más. El tamaño afecta la cantidad de espacio disponible para la suciedad y, por lo tanto, puede influir en el rendimiento del agente.

**Porcentaje de suciedad:** El porcentaje de suciedad en la cuadrícula también se define por el usuario antes de iniciar la simulación. Se permite un valor entre 0 (cuadrícula completamente limpia) y 1 (cuadrícula completamente sucia). Este porcentaje afecta la distribución de las celdas sucias en la cuadrícula y, en consecuencia, la cantidad de trabajo que el agente tendrá que realizar para limpiar.
### Cantidad de repeticiones
Para garantizar que los resultados sean estadísticamente significativos y no dependan de una configuración inicial específica, cada experimento se repite 10 veces. Esto se realiza tanto para el agente reflexivo como para el agente aleatorio. Al repetir los experimentos varias veces con diferentes distribuciones de suciedad y posiciones iniciales del agente, se obtiene un promedio del rendimiento de cada agente en esas condiciones.
## Análisis de datos
Los datos recopilados de las repeticiones de cada experimento fueron analizados calculando los promedios de rendimiento para cada configuración del entorno. Este enfoque estadístico permite obtener una visión general de cómo las variables del entorno afectan el comportamiento y la efectividad de los agentes. Además, se compararon los resultados entre el agente reflexivo y el agente aleatorio (con una suciedad del 80%) para determinar cuál es más eficiente en diferentes condiciones.

### Gráfico 1
![agente_reflex](https://hackmd.io/_uploads/rJh3xl2oC.png)
La gráfica presenta el rendimiento promedio del agente reflexivo en entornos de diferentes tamaños (desde 2x2 hasta 128x128) y con distintos niveles de suciedad (0.1, 0.2, 0.4, y 0.8).

**Tamaño del Entorno:** A medida que el tamaño del entorno aumenta, el rendimiento promedio del agente reflexivo también incrementa. Esto se debe a que un entorno más grande ofrece más oportunidades para limpiar celdas, lo que resulta en una mayor acumulación de puntos de rendimiento.

**Porcentaje de Suciedad:** El porcentaje de suciedad influye significativamente en el rendimiento del agente reflexivo. En general, a mayor porcentaje de suciedad, mejor es el rendimiento, dado que el agente tiene más celdas sucias que limpiar. Esto es particularmente notable en los entornos más grandes, como el de 128x128, donde el rendimiento del agente con un 80% de suciedad es significativamente superior al rendimiento en entornos con menor suciedad.
### Gráfico 2
![agente_aleatorio](https://hackmd.io/_uploads/HyMu-xnoC.png)
La gráfica presenta el rendimiento promedio del agente aleatorio en entornos de diferentes tamaños (desde 2x2 hasta 128x128) y con distintos niveles de suciedad (0.1, 0.2, 0.4, y 0.8).

**Tamaño del Entorno:** A medida que el tamaño del entorno aumenta, el rendimiento del agente aleatorio también muestra un incremento, aunque menos pronunciado en comparación con el agente reflexivo. En entornos más pequeños, el rendimiento es bajo debido a la naturaleza no determinística del agente, lo que significa que a menudo pierde oportunidades de limpiar celdas de manera eficiente. En entornos más grandes, especialmente en el tamaño 64x64 y 128x128, el rendimiento mejora notablemente, lo que sugiere que el agente tiene más oportunidades para moverse al azar y eventualmente encontrar celdas sucias.

**Porcentaje de Suciedad:** El porcentaje de suciedad tiene un impacto considerable en el rendimiento del agente aleatorio. En general, con un 80% de suciedad, el agente logra su mejor rendimiento en la mayoría de los tamaños de entorno, ya que casi cualquier movimiento probablemente lo lleve a una celda sucia. Sin embargo, para porcentajes de suciedad más bajos (0.1 y 0.2), el agente aleatorio tiene dificultades para encontrar y limpiar las celdas sucias, resultando en un bajo rendimiento.
### Gráfico 3
![compare_08](https://hackmd.io/_uploads/H1JYXx2jA.png)
La gráfica compara el rendimiento promedio del agente reflexivo y del agente aleatorio en entornos con un 80% de suciedad, variando el tamaño del entorno. 

**Diferencia de Rendimiento:** El agente reflexivo muestra un rendimiento consistentemente superior al agente aleatorio en todos los tamaños de entorno. Esto indica que el agente reflexivo es más eficiente en su toma de decisiones, ya que se basa en la percepción del entorno para actuar de manera más informada, mientras que el agente aleatorio selecciona sus acciones sin considerar la situación actual.

**Evolución del Rendimiento:** En entornos más pequeños (2x2 y 4x4), la diferencia en rendimiento entre ambos agentes es mínima, ya que el espacio reducido limita las opciones de movimiento y la diferencia en decisiones tiene menos impacto. Sin embargo, a medida que el tamaño del entorno aumenta, la brecha de rendimiento entre el agente reflexivo y el aleatorio se amplía considerablemente. En el entorno de 128x128, el agente reflexivo alcanza un rendimiento promedio cercano a 250, mientras que el agente aleatorio apenas supera los 50 puntos.

## Conclusión 
Respecto a lo evaluado y visto en los gráficos, se puede concluir que el agente reflexivo demuestra ser mucho más efectivo en limpiar celdas en comparación con el agente aleatorio, especialmente en entornos más grandes y con mayor suciedad. Esto se debe a su capacidad para tomar decisiones basadas en la percepción del entorno, lo que le permite actuar de manera más estratégica.

El tamaño del entorno y el porcentaje de suciedad tienen un impacto directo en el rendimiento de los agentes. Un mayor tamaño y más suciedad ofrecen más oportunidades para limpiar y, por lo tanto, un mayor rendimiento, especialmente para el agente reflexivo.

El agente aleatorio tiene un rendimiento limitado, independientemente del tamaño del entorno o la cantidad de suciedad. Esto resalta la importancia de dotar a los agentes con mecanismos de toma de decisiones más inteligentes para mejorar su efectividad en tareas como la limpieza en un entorno simulado.










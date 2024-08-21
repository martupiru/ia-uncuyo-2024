---
title: tp2-aima-questions

---

#### Ejercicio 6
##### 2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.
######  A) Can a simple reflex agent be perfectly rational for this environment? Explain.
Esto no es posible, ya que el agente no tiene conocimiento sobre el estado del entorno en el que se encuentra. Además, no tiene memoria respecto a los casilleros que ya visitó. Por esto, no es perfectamente racional
###### B) What about a reflex agent with state? Design such an agent.
Por más que el agente pueda tener memoria respecto a los casilleros que ya visitó, al no conocer previamente su entorno, el agente no es perfectamente racional
###### C)  How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?
En este caso, el agente al tener memoria respecto a los casilleros que visitó y un conocimiento absoluto del entorno, se puede construir un agente perfectamente racional. El mismo, puede buscar caminos más cortos y la manera más eficiente de limpiar la basura
##### 2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)
###### A) Can a simple reflex agent be perfectly rational for this environment? Explain.
Si el agente no tiene conocimiento de su entorno y memoria respecto a los casilleros que visitó no es perfectamente racional. Al no saber las dimensiones de su entorno, le llevaría más tiempo explorarlo. (movimientos limitados)
###### B) Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.
A partir de los ejercicios realizados, se puede observar que los rendimientos de los agentes tanto reflexivo como aleatorio son bastantes parecidos. Si agrandamos nuestro entorno, el agente reflexivo tiene una mejor performance respecto al aleatorio
###### C) Can you design an environment in which your randomized agent will perform poorly? Show your results.
El agente aleatorio tiene un bajo rendimiento en entornos de gran tamaño. Puede verse afectado tambien en la cantidad de basura que haya distribuida por el entorno. El desempeño disminuye cuando tenemos gran cantidad de basura en un entorno grande
###### D)  Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?
Esto si es probable ya que al tener memoria respecto a los casilleros que visitó, puede tener mejor performance. Sin embargo, al no tener un conocimiento absoluto respecto al entorno, deberá realizar muchos movimientos para encontrar las posiciones de basura.


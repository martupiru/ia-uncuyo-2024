---
title: tp7-id3

---

# ID3 - TP7 - PARTE C
## Laricchia Aida y Nahman Martina

### Resultados sobre la evaluación sobre el dataset tennis.csv


|Atributo  | Ganancia de informacion | 
| -------- | --------                | 
| outlook  | 0.24674982              |
| temp     | 0.02922257              |
| humidity | 0.15183550              |
| windy    | 0.04812703              |

#### Selección del atributo raiz
El atributo **outlook** tiene la ganancia de información más alta (0.24674982), lo que indica que es el atributo más relevante para dividir los datos. Por lo tanto, se selecciona como el nodo raíz del árbol.

#### Proceso de división en el árbol
El árbol comienza dividiendo los datos con base en el atributo **outlook**:

1. Si el valor de outlook es "sunny":

    * El árbol evalúa el atributo humidity:
        * Si la humedad es "high", la decisión es no jugar.
        * Si la humedad es "normal", la decisión es jugar.

2. Si el valor de outlook es "overcast":

    * No se evalúan más atributos, ya que la decisión es directamente jugar.
    
3. Si el valor de outlook es "rainy":

    * El árbol evalúa el atributo windy:
        * Si no hay viento (windy = false), la decisión es jugar.
        * Si hay viento (windy = true), la decisión es no jugar.
        
#### Predicciones
1. Para el día con outlook = sunny, humidity = high, windy = false, el árbol predice no jugar.
2. Para el día con outlook = rainy, windy = true, humidity = normal, el árbol predice no jugar.
3. Para el día con outlook = overcast, independientemente de los demás atributos, el árbol predice jugar.
4. Para el día con outlook = sunny, humidity = normal, el árbol predice jugar.


#### Estrategia para tipo de dato real
En el árbol de decisión que implementamos, se utilizaron únicamente atributos discretos, ya que el algoritmo ID3 está diseñado para trabajar con variables categóricas. En el conjunto de datos utilizado (tennis.csv), las características como la temperatura (temp), la humedad (humidity) y el viento (windy) ya están representadas de manera discreta, lo que permitió su uso directamente sin requerir ningún tipo de transformación.

Por otro lado, si los datos fueran continuos, como la temperatura expresada en grados Celsius, una estrategia común sería discretizar esos valores, es decir, convertirlos en intervalos. Por ejemplo, la temperatura podría clasificarse en categorías como "baja", "media" o "alta". Esta conversión es esencial para que el algoritmo ID3 pueda manejar adecuadamente variables continuas y realizar la clasificación correctamente.

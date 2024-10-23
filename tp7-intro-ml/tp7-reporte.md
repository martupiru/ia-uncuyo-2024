---
title: tp7-reporte

---

# Reporte Nahman Martina
## Lectura: Introduction to Statistical Learning
### Proveer las respuestas a los puntos 1,2,5,6,7 de la sección 2.4 (página 52 del ISLRv2)
1. **For each of parts (a) through (d), indicate whether we would generally expect the performance of a fexible statistical learning method to be better or worse than an infexible method. Justify your answer.**

**a) The sample size n is extremely large, and the number of predictors p is small.**

Se esperaría que un método inflexible tenga mejor rendimiento. Con una gran cantidad de datos y pocos predictores, un modelo simple, como la regresión lineal, puede capturar la relación entre los predictores y la respuesta sin sobreajustar. Además, el flexible requiere una gran cantidad de parámetros para ajustarse mejor.

**b) The number of predictors p is extremely large, and the number of observations n is small.**

Aquí se esperaría que un método flexible funcione mejor. Con muchos predictores y pocos datos, un modelo inflexible podría no ser suficiente para captar la complejidad del problema, y un modelo flexible podría ajustarse mejor.

**c) The relationship between the predictors and response is highly non-linear.**

Un método flexible funcionaría mejor. Los métodos flexibles, como los árboles de decisión o las redes neuronales, pueden capturar relaciones complejas no lineales que un modelo inflexible, como la regresión lineal, no podría.

**d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.**

En este caso, un método inflexible podría ser preferible. Los métodos flexibles tienden a ajustarse más a la variabilidad aleatoria del error, lo que puede aumentar el sobreajuste y empeorar el rendimiento en nuevos datos.

**2. Explain whether each scenario is a classifcation or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.**

**a) We collect a set of data on the top 500 frms in the US. For each frm we record proft, number of employees, industry and the CEO salary. We are interested in understanding which factors afect CEO salary.**
* Tipo de problema: Regresión.
* Objetivo principal: Inferencia (entender qué factores afectan al salario del CEO).
* n: 500, p: 3 (beneficio, número de empleados, industria).

**b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.**
* Tipo de problema: Clasificación.
* Objetivo principal: Predicción (determinar el éxito o fracaso).
* n: 20, p: 13 (precio, presupuesto de marketing, etc.).

**c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.** 
* Tipo de problema: Regresión.
* Objetivo principal: Predicción (predecir el cambio porcentual).
* n: 52 (semanas de 2012), p: 3 (cambios en los mercados bursátiles).

**5. What are the advantages and disadvantages of a very fexible (versus a less fexible) approach for regression or classifcation? Under what circumstances might a more fexible approach be preferred to a less fexible approach? When might a less fexible approach be preferred?**
#### Ventajas de un enfoque flexible:
* Puede capturar relaciones complejas y no lineales entre predictores y respuesta.
* Generalmente produce predicciones más precisas cuando la relación es compleja.

#### Desventajas:
* Mayor riesgo de sobreajuste, ajustándose a ruido en los datos.
* Menor interpretabilidad.
* Requiere más datos para evitar sobreajuste.

#### Cuándo preferir un enfoque flexible:
* Cuando la relación entre las variables es altamente no lineal o compleja, y se tiene suficiente cantidad de datos.

#### Cuándo preferir un enfoque inflexible:
* Cuando se busca interpretabilidad o la relación entre las variables es simple y lineal.

**6. Describe the diferences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classifcation (as opposed to a nonparametric approach)? What are its disadvantages?**
* **Enfoque paramétrico:** Asume una forma funcional específica para f(X), por ejemplo, lineal. La ventaja es que requiere estimar menos parámetros y es más simple e interpretable.
* **Ventajas:** Simplicidad, facilidad para interpretar y requiere menos datos.
* **Desventajas:** Puede llevar a un sesgo alto si el modelo asumido no refleja bien la realidad.
* **Enfoque no paramétrico:** No hace supuestos específicos sobre la forma de f(X). Es más flexible y puede ajustarse mejor a relaciones complejas.
* **Ventajas:** Flexibilidad y ajuste
* **Desventajas:** Requiere muchos datos y puede ser menos interpretable.
7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.


    | Obs | X1   | X2   | X3  | Y   |
    | --- | ---- | ---- | --- | --- |
    | 1   | 0    |  3   | 0   | Red
    | 2   | 2    |  0   | 0   | Red
    | 3   | 0    |  1   | 3   | Red
    | 4   | 0    |  1   | 2   | Green
    | 5   | -1   |  0   | 1   | Green
    | 6   | 1    |  1   | 1   | Red


**Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.
a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.**
#### Distancias: 

**Observación 1:** = 3
**Observación 2:** = 2
**Observación 3:** = √10
**Observación 4:** = √5
**Observación 5:** = √2
**Observación 6:** = √3

**b) What is our prediction with K = 1? Why?**
El punto más cercano es la observación 5 (distancia 1.41, clase Verde). Predicción: Verde.
**c) What is our prediction with K = 3? Why?**
Las tres observaciones más cercanas son 5 (Verde), 6 (Rojo), y 2 (Rojo). Predicción: Rojo (2 votos contra 1).
**d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?**
Un valor pequeño de K es preferible. Un K pequeño permite captar la complejidad de la frontera no lineal, mientras que un K grande suavizaría demasiado la frontera.

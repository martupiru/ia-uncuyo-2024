---
title: tp7-reporte-arbolado

---

# DESAFIO - TP7 - PARTE B
## Laricchia Aida y Nahman Martina

### Descripción del proceso de procesamiento de deatos

**1. Carga de datos:**

* Los datos fueron cargados usando readr::read_csv, lo cual ofrece una carga más rápida y eficiente de los archivos CSV. Los conjuntos de datos utilizados son:
    * Entrenamiento: arbolado-mza-dataset.csv
    * Prueba: arbolado-mza-dataset-test.csv

**2. Filtrado de Datos:**

* Se seleccionaron los árboles con inclinación peligrosa (inclinacion_peligrosa == 1), lo que representó un subconjunto de la base de datos.
* Luego, se filtró un número igual de árboles con inclinación no peligrosa (inclinacion_peligrosa == 0) para equilibrar las clases en el conjunto de datos.

**3. Manejo del Desequilibrio de Clases:**

* Para asegurarnos de que las clases "peligrosas" y "no peligrosas" estén balanceadas, se extrajeron 3,500 muestras aleatorias de árboles con inclinación no peligrosa, cantidad que coincide con la de árboles peligrosos.

**4. Selección de Variables:** 

* Se eliminaron las siguientes columnas del conjunto de datos para evitar que afecten al modelo de clasificación:
    * inclinacion_peligrosa, id, nombre_seccion, area_seccion, seccion, ultima_modificacion, circ_tronco_cm.
* Estas columnas no aportan información relevante para la predicción, y su eliminación ayuda a mejorar el rendimiento del modelo.

**5. Transformación de Variables:**

* Se asegura que la variable de respuesta inclinacion_peligrosa sea un factor (variable categórica), ya que Random Forest requiere que la variable dependiente sea categórica para clasificación.

**6. Unión de Conjuntos de Datos:**

Los conjuntos de datos de árboles con inclinación peligrosa y no peligrosa fueron unidos en un solo conjunto de datos (data_filtrado) para crear un conjunto de entrenamiento balanceado.

### Resultados obtenidos sobre el conjunto de validacion

El modelo de Random Forest fue entrenado utilizando 3,900 árboles (ntree = 3900) y un valor de mtry = 3, lo que significa que se consideran 3 variables al dividir cada nodo en el árbol. El rendimiento del modelo sobre el conjunto de validación (en este caso, el conjunto de prueba) se evaluó utilizando las predicciones realizadas:

* Primeras 30 predicciones: Se visualizó que las predicciones varían entre los valores 0 y 1, donde el 0 indica que el árbol no presenta inclinación peligrosa y el 1 indica que el árbol es peligroso.
* Resumen de las predicciones: El modelo proporciona una distribución de clases, permitiendo observar cuántas predicciones fueron para cada clase. El modelo muestra un balance adecuado entre las clases predichas. 

### Resultados obtenidos en kaggel 

![RESULTADOS](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp7-ml/images/results_PartB.png)
    
### Descripción Detallada del algoritmo propuesto

El algoritmo propuesto para la predicción de la inclinación peligrosa de los árboles es Random Forest, un algoritmo basado en la construcción de múltiples árboles de decisión. El proceso de clasificación funciona de la siguiente manera:

**1. Construcción de Árboles:**

* El modelo crea 3,900 árboles (ntree = 3900) utilizando diferentes subconjuntos aleatorios de los datos. Cada árbol es entrenado sobre una muestra aleatoria de los datos de entrenamiento, lo que mejora la robustez del modelo y reduce el riesgo de sobreajuste (overfitting).

**2. Selección de Variables:**

* Para cada división en los árboles, se seleccionan aleatoriamente 3 variables (por mtry = 3). Este parámetro controla el número de variables que se consideran en cada punto de decisión del árbol. Un valor pequeño de mtry generalmente lleva a modelos más robustos.

**3. Clasificación:**

* Cada árbol realiza una predicción de clase (0 o 1) para el árbol. La predicción final del modelo Random Forest se obtiene a partir de una votación de las predicciones de todos los árboles. El modelo predice que un árbol es "peligroso" si la mayoría de los árboles lo clasifican como tal.

**4. Evaluación del Modelo:**

* Después de entrenar el modelo, se realiza una predicción sobre el conjunto de prueba (data_test). La salida de la predicción es convertida en una variable binaria (0 o 1) para indicar si el árbol es o no peligroso.
* Además, el modelo se puede evaluar mediante el cálculo de la curva ROC y el AUC (Área bajo la curva), lo que proporciona una métrica adicional para la calidad del modelo.

**5. Resultados y Predicciones:**

* Finalmente, las predicciones se exportan a un archivo CSV para su envío a Kaggle, donde se espera evaluar el rendimiento del modelo en función de diversas métricas de clasificación.

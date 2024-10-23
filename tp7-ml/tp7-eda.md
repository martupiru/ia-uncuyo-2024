---
title: tp7-eda

---

# Respuestas Nahman Martina
## A partir del archivo arbolado-mendoza-dataset-train.csv responder las siguientes preguntas:
**A) Cual es la distribución de las clase inclinacion_peligrosa?** 
La distribución de las clases inclinacion_peligrosa es sesgada a derecha con respecto a la grafica.Por lo que hay menos árboles con inclinación peligrosa.
![Distribución inclinación peligrosa](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp7-intro-ml/images/inclinacion_peligrosa.png)
**B) ¿Se puede considerar alguna sección más peligrosa que otra?**
Si. La seccion 4 es más peligrosa que el resto

### Datos de árboles peligrosos por sección:

| Seccion | Cantidad |
| --------| -------- | 
|1        | 290      |
|2        | 450      |
|3        | 322      |
|4        | 840      |
|5        | 550      |
|6        | 309      |
|7        | 88       |
|8        | 27       |

![Inclinación peligrosa por seccion](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp7-intro-ml/images/inclinacion_peligrosa_seccion.png)

**C) ¿Se puede considerar alguna especie más peligrosa que otra?**
Si, podemos considerar que la especie morera es más peligrosa que las demás.
### Datos de árboles peligrosos por especie:

| Especie | Cantidad |
| --------| -------- | 
|Morera        | 1971      |
|Platano        | 224      |
|Paraiso        | 200      |
|Fresno europeo        | 183      |
|Acacia SP        | 79      |
|Fresno americnao        | 55      |
|Jacaranda        | 27       |
|Aguaribay        | 26       |
|Caducifolio        | 22      |
|Paraiso sombrilla       | 12      |
|Prunas        | 12      |
|Perenne        | 9      |
|Acer        | 9      |
|Olmo comun        | 8      |
|Ailanthus         | 7       |
|Tipa        | 6       |
|Álamo blanco        | 6      |
|Olmo bola        | 5      |
|Catalpa        | 4      |
|Acacia visco        | 3      |
|Conifera        | 3       |
|Alagrrobo        | 2       |
|Ligustro        | 2       |
|Eucalyptus         | 1       |

![Inclinación peligrosa por especie](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp7-intro-ml/images/inclinacion_peligrosa_especie.png)

**3)B) Generar un histograma de frecuencia para la variable circ_tronco_cm. Probar con diferentes  números de bins.**

Los bins utilizados fueron 10 y 20.
![Histograma del diámetro del tronco](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp7-intro-ml/images/histograma_ctronco.png)


**C) Repetir el punto b) pero separando por la clase de la variable inclinación_peligrosa** 

![Histograma del diámetro del tronco separado por inclinación peligrosa](https://github.com/martupiru/ia-uncuyo-2024/blob/main/tp7-intro-ml/images/histograma_ctronco_inclinacion_peligrosa.png)

**D)Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo  4 posibles valores [ muy alto, alto, medio, bajo ]. Utilizar la información del punto b. para seleccionar los puntos de corte para cada categoría. Guardar el nuevo dataframe bajo el nombre de arbolado-mendoza-dataset-circ_tronco_cm-train.csv**

Los puntos de corte se basarán en los valores que identificamos en los histogramas anteriores. 

* Bajo: Circunferencia del tronco menor que 50 cm
* Medio: Entre 50 cm y 100 cm
* Alto: Entre 100 cm y 150 cm
* Muy alto: Mayor a 150 cm

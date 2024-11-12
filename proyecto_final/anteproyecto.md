# Anteproyecto IA I

## Algoritmo evolutivo para la asignación de horarios y escuelas
### Código: CLASSMATCH 
### Integrantes: Laricchia Aida(13251) y Nahman Martina(13685)
![robots](https://github.com/martupiru/ia-uncuyo-2024/blob/main/proyecto_final/images/robots.jpg)
![legos](https://github.com/martupiru/ia-uncuyo-2024/blob/main/proyecto_final/images/legos.jpg)

### Descripción: 

Este proyecto propone el desarrollo de un algoritmo evolutivo para la asignación de horarios y ubicaciones de trabajo de profesores en una red de escuelas o talleres. El **objetivo principal** es optimizar el proceso de asignación de manera que se minimicen las distancias de traslado y se ajusten los horarios a la disponibilidad de los docentes, tomando en cuenta su nivel de experiencia. En particular, se define que los profesores “junior” no pueden impartir clases solos, por lo que deben ser asignados en conjunto con un profesor “senior”, mientras que los “senior” pueden trabajar de manera independiente. Además, el algoritmo debe cumplir con una distribución justa y eficiente en función de la experiencia, horarios disponibles y ubicación de residencia de los profesores.

Para la implementación, se investigará el uso de la librería DEAP (Distributed Evolutionary Algorithms in Python), una herramienta flexible y de código abierto que facilita el diseño y prueba de algoritmos evolutivos. DEAP permitirá estructurar y personalizar la solución, así como aplicar operadores genéticos que optimicen los resultados en este contexto. (1)(2)

![curso](https://github.com/martupiru/ia-uncuyo-2024/blob/main/proyecto_final/images/curso.jpeg)
#### Objetivos
* Optimización de horarios asignados a cada profesor para minimizar conflictos de disponibilidad respecto a sus horarios y a los diversos horarios de las escuelas/talleres.
* Reducción de las distancias entre la ubicación de los docentes y las escuelas asignadas para reducir los tiempos de traslado.
* Asegurar que los profesores “junior” estén siempre acompañados de un profesor “senior”.

#### Alcance

El algoritmo asignará profesores a las escuelas que mejor cumplan con los requisitos de cercanía, disponibilidad horaria, y adecuación de nivel (junior o senior).
Se utilizará el framework DEAP para implementar un algoritmo evolutivo, aprovechando sus capacidades para resolver problemas de optimización multiobjetivo. (3) (4)


#### Limitaciones

* No se considerarán otros factores, como preferencias personales de los profesores o la variabilidad en el tráfico.
* El proyecto se centrará en un número limitado de escuelas y profesores, para hacer factible la simulación dentro de los recursos de cómputo disponibles.
* El algoritmo no garantiza soluciones óptimas globales debido a la naturaleza aproximada de los algoritmos evolutivos, pero se buscarán soluciones cercanas al óptimo.
* Existen restricciones en la disponibilidad de horarios y en las combinaciones de profesores “junior” y “senior”, lo que puede limitar la flexibilidad de la asignación.

#### Métricas de evaluación

La evaluación del algoritmo se llevará a cabo mediante la comparación entre el estado actual de las asignaciones y el resultado después de aplicar el algoritmo, analizando tanto la eficiencia de asignación como el cumplimiento de restricciones. Las métricas específicas incluyen:
* *Nivel de Adecuación Horaria:* Medirá el porcentaje de coincidencia entre la disponibilidad horaria de los profesores y los horarios requeridos por las escuelas, garantizando que los horarios asignados sean los más adecuados para cada profesor.
* *Balance de Experiencia:* Evaluará la proporción de profesores "junior" y "senior" asignados en cada escuela, verificando que los profesores "junior" siempre estén acompañados por un "senior" y que se cumplan los requisitos de experiencia en cada asignación.
* *Número de Asignaciones Exitosas:* Este indicador medirá la cantidad de asignaciones satisfactorias que cumplen con las restricciones de distancia, disponibilidad horaria y experiencia.
* *Comparación con el Sistema Actual:* La solución obtenida por el algoritmo se comparará con el sistema actual de asignación de la empresa, evaluando si se mejora la optimización de horarios y distancias en relación con el método tradicional.
* *Porcentaje de Restricciones Cumplidas:* Se calculará el porcentaje de cumplimiento de las restricciones establecidas (por ejemplo, la co-asignación de juniors y seniors), garantizando que el algoritmo respete los requerimientos de experiencia y disponibilidad.


#### Bibliografía
* DEAP. (n.d.). DEAP Documentation. Retrieved from https://deap.readthedocs.io/en/master/ (1)

* DEAP. (n.d.). DEAP - Distributed Evolutionary Algorithms in Python [GitHub repository]. GitHub. Retrieved from https://github.com/DEAP/deap (2)

* Forcén, M. (2018). Selección y evaluación de estrategias en inteligencia artificial para la asignación de recursos docentes en instituciones educativas [Tesis de maestría, Universidad Nacional de La Plata]. CONICET Digital. https://ri.conicet.gov.ar/handle/11336/134016 (3)

* Forcén, M., & Forcén, M. (2017). Análisis de técnicas de optimización para la asignación de horarios en entornos educativos [Artículo]. CONICET Digital. https://ri.conicet.gov.ar/handle/11336/67471 (4)


### Justificación

La naturaleza multiobjetivo del problema (minimizar distancias y maximizar adecuación horaria y de habilidades) hace que un enfoque de optimización evolutivo sea una opción adecuada. Los algoritmos evolutivos, como los implementados en el framework DEAP, permiten la exploración simultánea de múltiples soluciones, lo cual es ideal para encontrar asignaciones óptimas en problemas de gran complejidad y con varios objetivos. Además, la capacidad de estos algoritmos para generar poblaciones de soluciones permite obtener asignaciones balanceadas y personalizadas para cada profesor y escuela, algo difícil de lograr mediante enfoques de optimización simples o métodos heurísticos convencionales.

### Listado de actividades a realizar

1. Recopilación de bibliografía y ejemplos similares de problemas de asignación y optimización multiobjetivo.
 *Descripción:* Investigar artículos y libros sobre asignación de recursos, optimización multiobjetivo y algoritmos evolutivos. (1)(2)(3)(4)

*Duración:* 3 días

3. Recopilación de datos respecto a los profesores y escuelas.

*Descripción:* Con la información recopilada mediante encuestas a los profesores, realizar un dataset con el que se trabajará luego.

*Duración:* 2 días

4. Diseño conceptual del algoritmo y selección de parámetros iniciales.

*Descripción:* Determinar los operadores genéticos, criterios de selección y otros parámetros importantes del algoritmo evolutivo.

*Duración:* 3 días

5. Puesta a punto del entorno de desarrollo e instalación de DEAP.

*Descripción:* Configurar el entorno de desarrollo y realizar pruebas iniciales con DEAP para familiarizarse con el framework.

*Duración:* 2 días

6. Implementación de la estructura básica del algoritmo evolutivo en DEAP.

*Descripción:* Crear la estructura base del algoritmo, incluyendo la generación de población inicial y el ciclo de generaciones.

*Duración:* 4 días

7. Codificación de las funciones de evaluación (fitness) para medir distancia, adecuación horaria y balance de experiencia.

*Descripción:* Implementar y probar las funciones de evaluación que usarán el algoritmo evolutivo para optimizar los objetivos definidos.

*Duración:* 4 días

8. Implementación de operadores genéticos específicos (cruce, mutación y selección).

*Descripción:* Programar y ajustar los operadores evolutivos según las necesidades del problema de asignación.

*Duración:* 4 días

9. Ejecución de experimentos con distintas configuraciones y parámetros.

*Descripción:* Ejecutar varias simulaciones del algoritmo variando parámetros (p. ej., tamaño de población, número de generaciones) y registrar los resultados.

*Duración:* 3 días

10. Análisis de los resultados obtenidos.

*Descripción:* Evaluar la eficacia de las asignaciones generadas en términos de las métricas establecidas y realizar ajustes si es necesario.

*Duración:* 4 días

11. Escritura del informe final y presentación de resultados.

*Descripción:* Redactar el informe final detallando el desarrollo del proyecto, los resultados obtenidos y el análisis de estos.

*Duración:* 3 días

### Cronograma estimado de actividades
![CRONOGRAMA](https://github.com/martupiru/ia-uncuyo-2024/blob/main/proyecto_final/images/CRONOGRAMA.png)










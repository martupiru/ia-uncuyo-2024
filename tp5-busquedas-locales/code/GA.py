#GA
import random
from environment import *

# Generación de un individuo (tablero)
def generar_individuo(n):
    return [random.randint(0, n-1) for _ in range(n)]

# Generación inicial de la población
def generar_poblacion(tam_poblacion, n):
    return [generar_individuo(n) for _ in range(tam_poblacion)]

# Selección proporcional
def seleccion_ruleta(poblacion, fitnesses):
    total_fitness = sum(fitnesses)
    probabilidades = [f/total_fitness for f in fitnesses] #probabilidad proporcional a su fitness.
    return poblacion[random.choices(range(len(poblacion)), probabilidades)[0]]

# Operador de cruce (de un punto)
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2 #generamos 2 hijos

# Operador de mutación
def mutacion(tablero, tasa_mutacion=0.1):
    n = len(tablero)
    if random.random() < tasa_mutacion:
        col = random.randint(0, n-1)
        fila = random.randint(0, n-1)
        tablero[col] = fila
    return tablero

# Algoritmo Genético
def algoritmo_genetico(n, tam_poblacion, generaciones, tasa_mutacion=0.1):
    poblacion = generar_poblacion(tam_poblacion, n)
    historial_h = []  # Lista para guardar la evolución de H
    evaluaciones = 0  # Contador de evaluaciones de la función H

    for generacion in range(generaciones):
        # Evaluación de la función fitness (el inverso de H, porque estamos minimizando)
        fitnesses = [1 / (H(individuo) + 1) for individuo in poblacion]
        evaluaciones += len(poblacion)  # Actualizar el número de evaluaciones
        
        nueva_poblacion = []
        for _ in range(tam_poblacion // 2):
            # Selección de padres
            padre1 = seleccion_ruleta(poblacion, fitnesses)
            padre2 = seleccion_ruleta(poblacion, fitnesses)

            # Cruce
            hijo1, hijo2 = cruce(padre1, padre2)

            # Mutación
            hijo1 = mutacion(hijo1, tasa_mutacion)
            hijo2 = mutacion(hijo2, tasa_mutacion)

            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)

        poblacion = nueva_poblacion

        # Registrar el mejor H en esta generación
        mejor_individuo_h = min(H(individuo) for individuo in poblacion)
        historial_h.append(mejor_individuo_h)

        # Si encontramos una solución (fitness perfecto), detener
        for individuo in poblacion:
            if H(individuo) == 0:
                return individuo, 0, evaluaciones, historial_h

    # Si no se encuentra una solución perfecta
    mejor_individuo = min(poblacion, key=H)
    h_mejor = H(mejor_individuo)
    return mejor_individuo, h_mejor, evaluaciones, historial_h


# Ejemplo de uso
"""n = 15  # Tamaño del tablero N-Reinas
solucion, generaciones, evaluciones, historial_h = algoritmo_genetico(n, tam_poblacion=100, generaciones=1000, tasa_mutacion=0.1)
print(f"Solución: {solucion} encontrada en {generaciones} generaciones con H(solución)={H(solucion)}")
"""""
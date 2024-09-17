#Simulated Annealing
import random
import math
from HillC import *

def generar_vecino_aleatorio(tablero):
    n = len(tablero)
    vecino = tablero.copy()
    col = random.randint(0, n-1)
    fila = random.randint(0, n-1)
    while vecino[col] == fila:
        fila = random.randint(0, n-1)
    vecino[col] = fila
    return vecino

def simulated_annealing(n, max_evaluations, temp_inicial=100, alpha=0.99):
    estado_actual = generar_tablero_inicial(n)
    mejor_estado = estado_actual.copy()
    h_actual = H(estado_actual)
    h_mejor = h_actual
    temperatura = temp_inicial
    evaluaciones = 0
    
    while evaluaciones < max_evaluations and h_mejor > 0 and temperatura > 0.1:
        vecino = generar_vecino_aleatorio(estado_actual)
        h_vecino = H(vecino)
        delta_H = h_vecino - h_actual
        
        if delta_H < 0 or random.uniform(0, 1) < math.exp(-delta_H / temperatura):
            estado_actual = vecino
            h_actual = h_vecino
            if h_actual < h_mejor:
                mejor_estado = estado_actual.copy()
                h_mejor = h_actual
        
        temperatura *= alpha
        evaluaciones += 1
    
    return mejor_estado, h_mejor, evaluaciones
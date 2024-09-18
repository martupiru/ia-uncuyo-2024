#Hill Climbing 

from environment import *

def generar_vecinos(tablero):
    vecinos = []
    n = len(tablero)
    for col in range(n):
        for fila in range(n):
            if tablero[col] != fila:
                vecino = tablero.copy()
                vecino[col] = fila
                vecinos.append(vecino)
    return vecinos

def hill_climbing(n, max_evaluations):
    estado_actual = generar_tablero_inicial(n)
    evaluaciones = 0
    h_actual = H(estado_actual)
    
    # Lista para guardar los valores de H en cada iteración -funcion H()
    historial_h = [h_actual] 
    
    while evaluaciones < max_evaluations and h_actual > 0:
        vecinos = generar_vecinos(estado_actual)
        vecinos_h = [(vecino, H(vecino)) for vecino in vecinos]
        vecinos_h.sort(key=lambda x: x[1])
        mejor_vecino, mejor_h = vecinos_h[0]
        
        if mejor_h >= h_actual:
            break  # No hay mejora
        
        estado_actual = mejor_vecino
        h_actual = mejor_h
        evaluaciones += 1
        
        # Guardar el valor de H en cada iteración -funcion H()
        historial_h.append(h_actual)
    
    return estado_actual, h_actual, evaluaciones, historial_h
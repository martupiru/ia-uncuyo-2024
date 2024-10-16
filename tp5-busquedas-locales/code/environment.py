#Tablero
import random

def generar_tablero_inicial(n):
    return [random.randint(0, n-1) for _ in range(n)]
#cuenta el número de pares de reinas que están amenazadas entre sí 
#(en la misma fila o en la misma diagonal). Si H(tablero) = 0, el tablero es una solución válida.
def H(tablero):
    conflictos = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j]:
                conflictos += 1
            elif abs(i - j) == abs(tablero[i] - tablero[j]):
                conflictos += 1
    return conflictos
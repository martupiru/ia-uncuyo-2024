#Tablero
import random

def generar_tablero_inicial(n):
    return [random.randint(0, n-1) for _ in range(n)]

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
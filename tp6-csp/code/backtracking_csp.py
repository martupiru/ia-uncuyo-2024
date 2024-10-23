#backtracking csp
from environment import *

#funcion para verificar si se puede colocar una reina en la posición (fila, col)
def es_valido(tablero, fila, col):
    for c in range(col):
        if tablero[c] == fila or abs(tablero[c] - fila) == abs(c - col):
            return False
    return True

#funcion recursiva de backtracking
def resolver_n_reinas(tablero, col):
    n = len(tablero)
    if col >= n:
        return True

    for fila in range(n):
        if es_valido(tablero, fila, col):
            tablero[col] = fila  #coloco reina
            if resolver_n_reinas(tablero, col + 1):
                return True
            tablero[col] = -1  #retroceder (backtracking)

    return False

#funcion principal que llama al backtracking
def solucionar_n_reinas(n):
    tablero = [-1] * n  #creo tablero vacio
    if resolver_n_reinas(tablero, 0):
        return tablero
    else:
        return None
    
# Ejemplo de uso
n = 15
solucion = solucionar_n_reinas(n)
if solucion:
    print(f"Solución para {n} reinas: {solucion}")
    print(f"Conflictos: {H(solucion)}")  #usamos H para verificar que no haya conflictos
else:
    print("No se encontró solución")
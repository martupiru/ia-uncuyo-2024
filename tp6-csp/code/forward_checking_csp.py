#forward checking 
from environment import *

def es_valido(tablero, fila, col, dominios):
    # Verificar si alguna reina anterior está en conflicto
    for c in range(col):
        if tablero[c] == fila or abs(tablero[c] - fila) == abs(c - col):
            return False
    return True

#funcion para actualizar dominios al colocar una reina
def actualizar_dominios(dominios, fila, col, n):
    nuevo_dominios = [dominio[:] for dominio in dominios]
    for c in range(col + 1, n):
        if fila in nuevo_dominios[c]:
            nuevo_dominios[c].remove(fila) #eliminar fila
        dist = c - col
        if fila + dist in nuevo_dominios[c]:
            nuevo_dominios[c].remove(fila + dist) #eliminar diagonal abajo
        if fila - dist in nuevo_dominios[c]:
            nuevo_dominios[c].remove(fila - dist) #eliminar diagonal arriba
    return nuevo_dominios

#funcion recursiva con forward checking
def resolver_n_reinas_fc(tablero, col, dominios):
    n = len(tablero)
    if col >= n:
        return True

    for fila in dominios[col]:
        if es_valido(tablero, fila, col, dominios):
            tablero[col] = fila
            nuevo_dominios = actualizar_dominios(dominios, fila, col, n)
            if all(nuevo_dominios[c] for c in range(col + 1, n)): #verificar si quedan valores en los dominios
                if resolver_n_reinas_fc(tablero, col + 1, nuevo_dominios):
                    return True
            tablero[col] = -1  #retroceder (backtracking)

    return False

#funcion principal que llama al forward checking
def solucionar_n_reinas_fc(n):
    tablero = [-1] * n  # Creo tablero vacío
    dominios = [list(range(n)) for _ in range(n)] #dominios iniciales: todas las filas posibles
    if resolver_n_reinas_fc(tablero, 0, dominios):
        return tablero
    else:
        return None

# Ejemplo de uso
n = 15
solucion = solucionar_n_reinas_fc(n)
if solucion:
    print(f"Solución para {n} reinas con forward checking: {solucion}")
    print(f"Conflictos: {H(solucion)}")  #usamos H para verificar que no haya conflictos
else:
    print("No se encontró solución")
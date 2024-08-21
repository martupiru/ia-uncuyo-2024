import random
from environment import *
class Agent:
    def __init__(self, environment):
        self.environment = environment

    def choose_action(self, action):
        # Recibe la accion y la ejecuta
        return action
    
def obtener_accion_usuario():
    while True:
        action = input('Introduce la acción: Arriba, Abajo, Izquierda, Derecha, Limpiar, NoHacerNada: ')
        if action in ['Arriba', 'Abajo', 'Izquierda', 'Derecha', 'Limpiar', 'NoHacerNada']:
            return action
        else:
            print("Acción no válida. Por favor, elige una acción de la lista.")
    

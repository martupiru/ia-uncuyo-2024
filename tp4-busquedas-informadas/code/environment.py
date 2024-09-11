import numpy as np
import gymnasium as gym

class Environment:
    def __init__(self, size, holes_rate, seed):
        self.environment, self.initial_state, self.final_state, self.map_list = generate_random_map_custom(size, holes_rate, seed)
        self.size = size

# Clase personalizada para modificar la posición inicial del agente
class CustomFrozenLakeEnv(gym.Wrapper):
    def __init__(self, env, start_pos=(0, 0)):
        super().__init__(env)
        self.start_pos = start_pos
    
    def reset(self, **kwargs):
        # Restablecer el entorno a su estado inicial.
        self.env.reset(**kwargs)
        # Convertir la posición del agente en el entorno utilizando las coordenadas de start_pos
        self.env.unwrapped.s = self.start_pos[0] * self.env.unwrapped.ncol + self.start_pos[1]
        return int(self.env.unwrapped.s)

def generate_random_map_custom(size, holes_rate, seed):
    if seed is not None:
        np.random.seed(seed)  # Establecer la semilla para la reproducibilidad
    
    # Crear una matriz vacía con 'F' y 'H'
    map_matrix = create_matrix(size, size, holes_rate, seed)
    
    # Asignar posición aleatoria para el agente 'A'
    start_pos = (np.random.randint(0, size), np.random.randint(0, size))
    while map_matrix[start_pos] == 'H':
        start_pos = (np.random.randint(0, size), np.random.randint(0, size))
    map_matrix[start_pos] = 'A'
        
    # Asegurarse de que la posición del objetivo 'G' sea distinta de la posición de 'A'
    while True:
        goal_pos = (np.random.randint(0, size), np.random.randint(0, size))
        if goal_pos != start_pos and map_matrix[goal_pos] != 'H':
            map_matrix[goal_pos] = 'G'
            break
    
    # Convertir la matriz a lista de strings para pasarla a gym
    map_list = [''.join(row) for row in map_matrix]
    
    # Crear el entorno base con gym.make
    env = gym.make('FrozenLake-v1', desc=map_list, render_mode='human', is_slippery=False)
    
    # Aplicar el wrapper personalizado para modificar la posición inicial
    env = CustomFrozenLakeEnv(env, start_pos=start_pos)
    
    # Modificar la vida del agente a 1000 acciones utilizando el wrapper TimeLimit
    env = gym.wrappers.TimeLimit(env, max_episode_steps=1000)
        
    return env, start_pos, goal_pos, map_list

def create_matrix(filas, columnas, proporcion, seed):
    if seed is not None:
        np.random.seed(seed)  # Establecer la semilla para la reproducibilidad
    
    # Calcular la cantidad de 'H' (huecos) y 'F' (congelado)
    total_casilleros = filas * columnas
    hole_amount = int(total_casilleros * proporcion)
    frozen_amount = total_casilleros - hole_amount

    # Crear la matriz con la cantidad adecuada de 'H' y 'F'
    matriz = np.array(['H'] * hole_amount + ['F'] * frozen_amount)

    # Mezclar la matriz para distribuir aleatoriamente los 'H' y 'F'
    np.random.shuffle(matriz)

    # Redimensionar la matriz a la forma deseada
    matriz = matriz.reshape(filas, columnas)

    return matriz

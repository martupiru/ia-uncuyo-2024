#AGENTE ALEATORIO
from environment import *
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from node import Nodo

print("AGENTE CON COMPORTAMIENTO ALEATORIO")

def random_agent(env):
    nombre = "Agente Aleatorio"
    start_time = time.time()

    # Inicializar el estado del entorno
    current_state = env.initial_state
    nodo_actual = Nodo(current_state)  # Crear un nodo para el estado inicial
    
    explored = set()
    first_cost = 0  # Número de acciones consideradas
    second_cost = 0  # Costo acumulado
    moves = []
    
    # Agregar el estado inicial a los explorados
    explored.add(current_state)
    move_count=0 
    
    while (current_state != env.final_state) and (move_count < 1000):
        # Obtener las posibles acciones usando el método de Nodo
        actions, action_number = nodo_actual.possible_actions(env)
        
        if not actions:
            break  # No hay más acciones posibles, terminamos el ciclo

        valid_action = False
        while not valid_action:
            # Elegir una acción aleatoria
            random_index = random.randint(0, len(actions) - 1)
            chosen_action = actions[random_index]
            action_cost = action_number[random_index]
            
            # Verificar si la acción lleva a un agujero
            if env.map_list[chosen_action[0]][chosen_action[1]] != 'H':  # 'H' representa un agujero
                valid_action = True  # Si no es un agujero, la acción es válida
        
        # Actualizar estado y costos
        moves.append(action_cost)
        current_state = chosen_action
        nodo_actual = Nodo(current_state)  # Actualizar el nodo actual
        explored.add(current_state)
        
        first_cost +=1
        second_cost += action_cost + 1
        move_count +=1
    
    end_time = time.time()
    final_time = end_time - start_time
    
    explored_amount = len(explored)
    found = current_state == env.final_state
    
    # Devuelve las métricas del agente aleatorio
    return moves, explored_amount, first_cost, second_cost, final_time, found, nombre

# Inicializar listas para almacenar los resultados
states_explored_list = []
first_cost_list = []
second_cost_list = []
time_list = []
cont_found =0
for i in range(30):
    env = Environment(100, 0.08, i * 9)  # tamaño, porcentaje de hielo, semilla
    result = random_agent(env)

    moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
    
    # Almacenar los resultados en las listas
    if found:
        cont_found +=1
        states_explored_list.append(explored_amount)
        first_cost_list.append(first_cost)  
        second_cost_list.append(second_cost)  
        time_list.append(final_time)

# Calcular la media y la desviación estándar
prom_states = np.mean(states_explored_list)
std_states = np.std(states_explored_list)

prom_first_cost = np.mean(first_cost_list)
std_first_cost = np.std(first_cost_list)

prom_second_cost = np.mean(second_cost_list)
std_second_cost = np.std(second_cost_list)

prom_time = np.mean(time_list)
std_time = np.std(time_list)

print("RESULTADOS:")
print("FOUND: ", cont_found)
print(f"Promedio de estados explorados: {prom_states:.2f} (±{std_states:.2f})")
print(f"Promedio de first_cost: {prom_first_cost:.2f} (±{std_first_cost:.2f})")
print(f"Promedio de second_cost: {prom_second_cost:.2f} (±{std_second_cost:.2f})")
print(f"Promedio de tiempo empleado: {prom_time:.5f} s (±{std_time:.5f} s)")

# Graficar los resultados en boxplots
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.boxplot(states_explored_list)
plt.title('Estados Explorados')

plt.subplot(1, 4, 2)
plt.boxplot(first_cost_list)
plt.title('First Cost')

plt.subplot(1, 4, 3)
plt.boxplot(second_cost_list)
plt.title('Second Cost')

plt.subplot(1, 4, 4)
plt.boxplot(time_list)
plt.title('Tiempo Empleado (s)')

plt.suptitle("Resultados del Agente Aleatorio en 30 ejecuciones")
plt.show()

#MAIN DLS
from node import * 
from environment import * 
from dls import * 
import matplotlib.pyplot as plt
import numpy as np

print("AGENTE BÚSQUEDA DLS")

# Inicializar listas para almacenar los resultados
states_explored_list = []
first_cost_list = []
second_cost_list = []
time_list = []
cont_found=0

for i in range(30):
    env = Environment(100, 0.08, i * 9)  # tamaño, porcentaje de hielo, semilla
    result = dls(env,10)  

    path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
    
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
print(f"Promedio de estados explorados: {prom_states:.2f} s (±{std_states:.2f})") #media, desviacion estandar
print(f"Promedio de first_cost: {prom_first_cost:.2f} s (±{std_first_cost:.2f})")
print(f"Promedio de second_cost: {prom_second_cost:.2f} s (±{std_second_cost:.2f})")
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

plt.suptitle("Resultados de DLS en 30 ejecuciones")
plt.show()
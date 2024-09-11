#MAIN A STAR
import numpy as np
import matplotlib.pyplot as plt
import environment as e
from a_Star import a_star

# Listas para almacenar resultados
explored_states = []
total_costs = []
times_taken = []
cont_found = 0
# Ejecutar el algoritmo 30 veces
for i in range(30):
    env = e.Environment(100, 0.08, i*9)  # tamaño, porcentaje de hielo, semilla
    result = a_star(env)
    
    path, moves, explored_amount, total_cost, final_time, found, nombre = result
    if found:
        cont_found +=1
        explored_states.append(explored_amount)
        total_costs.append(total_cost)
        times_taken.append(final_time)


# Calcular media y desviación estándar
mean_states = np.mean(explored_states)
std_states = np.std(explored_states)
mean_cost = np.mean(total_costs)
std_cost = np.std(total_costs)
mean_time = np.mean(times_taken)
std_time = np.std(times_taken)

print("RESULTADOS:")
print("FOUND: ", cont_found)
print(f"Media de estados explorados: {mean_states}, Desviación estándar: {std_states}")
print(f"Media de costo total: {mean_cost}, Desviación estándar: {std_cost}")
print(f"Media de tiempo empleado: {mean_time}, Desviación estándar: {std_time}")

# Graficar boxplots
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.boxplot(explored_states)
plt.title('Estados Explorados')

plt.subplot(1, 3, 2)
plt.boxplot(total_costs)
plt.title('Costo Total')

plt.subplot(1, 3, 3)
plt.boxplot(times_taken)
plt.title('Tiempo Empleado (s)')

plt.suptitle('Resultados de A* en 30 ejecuciones')
plt.show()


        

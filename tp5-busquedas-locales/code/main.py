#MAIN
#Ejecucion algoritmos y csv
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from HillC import *
from SimulatedA import *
from estadistic import *
from GA import * 

#30 ejecuciones para la estadística 
def ejecutar_algoritmos(n_values, num_runs=30, max_evaluations=1000, graficar=False):
    resultados = []
    tam_poblacion = 100  # Definir el tamaño de la población para el algoritmo genético
    generaciones = 1000  # Definir el número de generaciones

    for n in n_values:
        print(f"Ejecutando para N={n}")
        
        # Para guardar los historiales de H para cada algoritmo
        historial_h_hc_runs = []
        historial_h_sa_runs = []
        historial_h_ga_runs = []
        
        for run in range(num_runs):
            # Hill Climbing
            start_time = time.time()
            solucion_hc, h_hc, eval_hc, historial_h_hc = hill_climbing(n, max_evaluations)
            tiempo_hc = time.time() - start_time
            resultado_hc = {
                'Algoritmo': 'Hill Climbing',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_hc,
                'H': h_hc,
                'Optimo': h_hc == 0,
                'Tiempo': tiempo_hc,
                'Estados_Evaluados': eval_hc
            }
            resultados.append(resultado_hc)
            historial_h_hc_runs.append(historial_h_hc)
            
            # Simulated Annealing
            start_time = time.time()
            solucion_sa, h_sa, eval_sa, historial_h_sa = simulated_annealing(n, max_evaluations)
            tiempo_sa = time.time() - start_time
            resultado_sa = {
                'Algoritmo': 'Simulated Annealing',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_sa,
                'H': h_sa,
                'Optimo': h_sa == 0,
                'Tiempo': tiempo_sa,
                'Estados_Evaluados': eval_sa
            }
            resultados.append(resultado_sa)
            historial_h_sa_runs.append(historial_h_sa)
            
            # Algoritmo Genético
            start_time = time.time()
            solucion_ga, h_ga, evaluaciones_ga, historial_h_ga = algoritmo_genetico(n, tam_poblacion, generaciones)
            tiempo_ga = time.time() - start_time
            resultado_ga = {
                'Algoritmo': 'Genético',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_ga,
                'H': h_ga,
                'Optimo': h_ga == 0,
                'Tiempo': tiempo_ga,
                'Estados_Evaluados': evaluaciones_ga  # Contamos las generaciones como estados evaluados
            }
            resultados.append(resultado_ga)
            historial_h_ga_runs.append(historial_h_ga)
        
        # Graficar si se ha pasado el argumento graficar=True
        if graficar:
            # Graficar Hill Climbing
            graficar_historial_h(historial_h_hc_runs[-1], "Hill Climbing", n)
            # Graficar Simulated Annealing
            graficar_historial_h(historial_h_sa_runs[-1], "Simulated Annealing", n)
            # Graficar Algoritmo Genético
            graficar_historial_h(historial_h_ga_runs[-1], "Genético", n)

    return pd.DataFrame(resultados)


#csv 
def guardar_csv(df, filename='resultados_nreinas.csv'):
    df.to_csv(filename, index=False)
    print(f"Resultados guardados en {filename}")


#EJECUCION PRUEBAAAAA
n_values = [4, 8, 10,12,15]
    
# Ejecutar los algoritmos
df_resultados = ejecutar_algoritmos(n_values, num_runs=30, max_evaluations=1000, graficar=True)
    
# Guardar resultados en CSV de todos los algoritmos
guardar_csv(df_resultados, 'resultados_nreinas.csv')

# Calcular estadísticas
df_estadisticas = calcular_estadisticas(df_resultados)
print("\nEstadísticas por Algoritmo y N:")
print(df_estadisticas)
    
# Guardar estadísticas en CSV de lo pedido
guardar_csv(df_estadisticas, 'estadisticas_nreinas.csv')
    
# Generar boxplots 
generar_boxplots(df_resultados, n_values)


# Graficar historial h
"""for n in n_values:
    estado_final, h_final, evaluaciones, historial_h_hc = hill_climbing(n, max_evaluations=1000)
    graficar_historial_h(historial_h_hc, "Hill Climbing", n)

    estado_final_sa, h_final_sa, evaluaciones_sa, historial_h_sa = simulated_annealing(n, max_evaluations=1000)
    graficar_historial_h(historial_h_sa, "Simulated Annealing", n)

    estado_final_ga, h_final_ga, evaluaciones_ga, historial_h_ga = algoritmo_genetico(n, tam_poblacion=100, generaciones=1000, tasa_mutacion=0.1)
    graficar_historial_h(historial_h_ga, "Genético", n)"""  
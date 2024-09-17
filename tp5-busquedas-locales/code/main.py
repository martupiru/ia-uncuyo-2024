#Ejecucion algoritmos y csv
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from HillC import *
from SimulatedA import *
from estadistic import *

def ejecutar_algoritmos(n_values, num_runs=30, max_evaluations=1000):
    resultados = []
    for n in n_values:
        print(f"Ejecutando para N={n}")
        for run in range(num_runs):
            # Hill Climbing
            start_time = time.time()
            solucion_hc, h_hc, eval_hc = hill_climbing(n, max_evaluations)
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
            
            # Simulated Annealing
            start_time = time.time()
            solucion_sa, h_sa, eval_sa = simulated_annealing(n, max_evaluations)
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
    
    return pd.DataFrame(resultados)


def guardar_csv(df, filename='resultados_nreinas.csv'):
    df.to_csv(filename, index=False)
    print(f"Resultados guardados en {filename}")


#EJECUCION PRUEBAAAAA

n_values = [4, 8, 10,12,15]
    
# Ejecutar los algoritmos
df_resultados = ejecutar_algoritmos(n_values, num_runs=30, max_evaluations=1000)
    
# Guardar resultados en CSV
guardar_csv(df_resultados, 'resultados_nreinas.csv')

# Calcular estadísticas
df_estadisticas = calcular_estadisticas(df_resultados)
print("\nEstadísticas por Algoritmo y N:")
print(df_estadisticas)
    
# Guardar estadísticas en CSV
guardar_csv(df_estadisticas, 'estadisticas_nreinas.csv')
    
# Generar boxplots
generar_boxplots(df_resultados, n_values)
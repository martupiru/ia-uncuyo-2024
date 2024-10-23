#MAIN
import csv 
import time
import pandas as pd
from estadistic import *
from backtracking_csp import *
from forward_checking_csp import *

#30 ejecuciones para la estadística 
def ejecutar_algoritmos(n_values, num_runs=30):
    resultados = []
    
    for n in n_values:
        print(f"Ejecutando para N={n}")
        
        for run in range(num_runs):
            #backtracking
            start_time = time.time()
            solucion_bt = solucionar_n_reinas(n)
            tiempo_bt = time.time() - start_time
            h_bt = H(solucion_bt) if solucion_bt else -1
            eval_bt = n * (n - 1) // 2  
            resultado_bt = {
                'Algoritmo': 'Backtracking',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_bt,
                'H': h_bt,
                'Optimo': h_bt == 0,
                'Tiempo': tiempo_bt,
                'Estados_Evaluados': eval_bt
            }
            resultados.append(resultado_bt)
            
            # Forward Checking
            start_time = time.time()
            solucion_fc = solucionar_n_reinas_fc(n)
            tiempo_fc = time.time() - start_time
            h_fc = H(solucion_fc) if solucion_fc else -1
            eval_fc = n * (n - 1) // 2  
            resultado_fc = {
                'Algoritmo': 'Forward Checking',
                'N': n,
                'Run': run + 1,
                'Solucion': solucion_fc,
                'H': h_fc,
                'Optimo': h_fc == 0,
                'Tiempo': tiempo_fc,
                'Estados_Evaluados': eval_fc
            }
            resultados.append(resultado_fc)

    return pd.DataFrame(resultados)


#csv 
def guardar_csv(df, filename='resultados_nreinas.csv'):
    df.to_csv(filename, index=False)
    print(f"Resultados guardados en {filename}")


#EJECUCION
n_values = [4, 8, 10, 12, 15]

#ejecutar los algoritmos
df_resultados = ejecutar_algoritmos(n_values, num_runs=30)

#guardar resultados en CSV
guardar_csv(df_resultados, 'resultados_nreinas.csv')

#calcular estadisticas
df_estadisticas = calcular_estadisticas(df_resultados)
print("\nEstadísticas por Algoritmo y N:")
print(df_estadisticas)

# Guardar estadísticas en CSV
guardar_csv(df_estadisticas, 'estadisticas_nreinas.csv')

# Generar boxplots
generar_boxplots(df_resultados, n_values)

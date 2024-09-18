# Calculo de estadisticas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def calcular_estadisticas(df):
    estadisticas = []
    grouped = df.groupby(['Algoritmo', 'N'])
    for (alg, n), group in grouped:
        total = len(group)
        exitos = group[group['Optimo'] == True]
        num_exitos = len(exitos)
        porcentaje_exitos = (num_exitos / total) * 100
        
        if num_exitos > 0:
            tiempo_promedio = exitos['Tiempo'].mean()
            tiempo_std = exitos['Tiempo'].std()
            estados_promedio = exitos['Estados_Evaluados'].mean()
            estados_std = exitos['Estados_Evaluados'].std()
        else:
            tiempo_promedio = None
            tiempo_std = None
            estados_promedio = None
            estados_std = None
        
        estadistica = {
            'Algoritmo': alg,
            'N': n,
            'Porcentaje_Exitos': porcentaje_exitos,
            'Tiempo_Promedio': tiempo_promedio,
            'Tiempo_Desviacion': tiempo_std,
            'Estados_Promedio': estados_promedio,
            'Estados_Desviacion': estados_std
        }
        estadisticas.append(estadistica)
    
    return pd.DataFrame(estadisticas)


def generar_boxplots(df, n_values):
    # Aplicar un tema de Seaborn
    sns.set_theme(style="whitegrid")
    
    # Definir paleta de colores
    colores = sns.color_palette("Set2")
    
    for n in n_values:
        subset = df[df['N'] == n]
        
        # Boxplot de Tiempos de Ejecución
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Algoritmo', y='Tiempo', hue='Algoritmo', data=subset, palette=colores, dodge=False)
        plt.title(f'Distribución de Tiempos de Ejecución para N={n}', fontsize=16, fontweight='bold')
        plt.ylabel('Tiempo (segundos)', fontsize=12)
        plt.xlabel('Algoritmo', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.savefig(f'boxplot_tiempo_N{n}.png', dpi=300, bbox_inches='tight')  # Mayor resolución
        plt.close()
        
        # Boxplot de Estados Evaluados
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Algoritmo', y='Estados_Evaluados', hue='Algoritmo', data=subset, palette=colores, dodge=False)
        plt.title(f'Distribución de Estados Evaluados para N={n}', fontsize=16, fontweight='bold')
        plt.ylabel('Estados Evaluados', fontsize=12)
        plt.xlabel('Algoritmo', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.savefig(f'boxplot_estados_N{n}.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    print("Boxplots generados y guardados como imágenes.")

def graficar_historial_h(historial_h, algoritmo, n):
    plt.figure(figsize=(10, 6))
    plt.plot(historial_h, marker='o')
    plt.title(f'Variación de H() en {algoritmo} para N={n}', fontsize=16)
    plt.xlabel('Iteraciones', fontsize=12)
    plt.ylabel('H (Número de conflictos)', fontsize=12)
    plt.grid(True)
    plt.show()


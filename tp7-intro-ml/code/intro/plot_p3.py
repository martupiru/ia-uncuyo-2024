#Punto 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Cargar el archivo CSV de entrenamiento
file_path = 'C:/Users/Usuario/Documents/MARTI/Github/ia-uncuyo-2024/tp7-intro-ml/data/arbolado-mendoza-dataset-train.csv'
data = pd.read_csv(file_path)

# Generar un histograma de circ_tronco_cm con diferentes números de bins
plt.figure(figsize=(10, 6))

# Primer histograma con 10 bins
plt.subplot(1, 2, 1)
data['circ_tronco_cm'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de circ_tronco_cm (10 bins)')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

# Segundo histograma con 20 bins
plt.subplot(1, 2, 2)
data['circ_tronco_cm'].plot(kind='hist', bins=20, color='lightgreen', edgecolor='black')
plt.title('Histograma de circ_tronco_cm (20 bins)')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Separar los datos por la clase inclinacion_peligrosa
plt.figure(figsize=(12, 6))

# Histograma para árboles sin inclinación peligrosa
plt.subplot(1, 2, 1)
data[data['inclinacion_peligrosa'] == 0]['circ_tronco_cm'].plot(kind='hist', bins=15, color='lightcoral', edgecolor='black')
plt.title('Histograma de circ_tronco_cm (Sin inclinación peligrosa)')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

# Histograma para árboles con inclinación peligrosa
plt.subplot(1, 2, 2)
data[data['inclinacion_peligrosa'] == 1]['circ_tronco_cm'].plot(kind='hist', bins=15, color='lightskyblue', edgecolor='black')
plt.title('Histograma de circ_tronco_cm (Con inclinación peligrosa)')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Definir los puntos de corte
bins = [0, 50, 100, 150, data['circ_tronco_cm'].max()]
labels = ['Bajo', 'Medio', 'Alto', 'Muy alto']

# Crear la nueva variable categórica circ_tronco_cm_cat
data['circ_tronco_cm_cat'] = pd.cut(data['circ_tronco_cm'], bins=bins, labels=labels, include_lowest=True)

# Verificar los primeros registros con la nueva variable categórica
print(data[['circ_tronco_cm', 'circ_tronco_cm_cat']].head())

# Guardar el nuevo archivo con la nueva columna categórica
new_file_path = 'C:/Users/Usuario/Documents/MARTI/Github/ia-uncuyo-2024/tp7-intro-ml/data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv'
data.to_csv(new_file_path, index=False)

#Punto 2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV de entrenamiento
file_path = 'C:/Users/Usuario/Documents/MARTI/Github/ia-uncuyo-2024/tp7-intro-ml/data/arbolado-mendoza-dataset-train.csv'
data = pd.read_csv(file_path)

# Verificar que los datos se cargaron correctamente
print("Primeras 5 filas del dataset:")
print(data.head())

# Contar la cantidad de valores para la columna inclinacion_peligrosa
distribution = data['inclinacion_peligrosa'].value_counts()

# Graficar la distribución de la inclinación peligrosa (0 = No peligrosa, 1 = Peligrosa)
plt.figure(figsize=(8, 6))
sns.barplot(x=distribution.index, y=distribution.values, palette="Blues_d")
plt.title('Distribución de inclinación peligrosa')
plt.xlabel('Inclinación peligrosa (0 = No, 1 = Sí)')
plt.ylabel('Cantidad de árboles')
plt.show()

# Agrupar por sección y contar la cantidad de árboles con inclinación peligrosa
seccion_peligrosa = data[data['inclinacion_peligrosa'] == 1].groupby('seccion').size()

# Verificar si hay datos antes de graficar
if not seccion_peligrosa.empty:
    print("Datos de árboles peligrosos por sección:")
    print(seccion_peligrosa)
    
    # Graficar la cantidad de árboles peligrosos por sección
    plt.figure(figsize=(12, 8))
    seccion_peligrosa.plot(kind='bar', color='coral')
    plt.title('Árboles con inclinación peligrosa por sección')
    plt.xlabel('Sección')
    plt.ylabel('Cantidad de árboles peligrosos')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("No hay árboles con inclinación peligrosa por sección para graficar.")

# Agrupar por especie y contar la cantidad de árboles con inclinación peligrosa
especie_peligrosa = data[data['inclinacion_peligrosa'] == 1].groupby('especie').size().sort_values(ascending=False)

# Verificar si hay datos antes de graficar
if not especie_peligrosa.empty:
    print("Datos de árboles peligrosos por especie:")
    print(especie_peligrosa)
    
    # Graficar la cantidad de árboles peligrosos por especie
    plt.figure(figsize=(12, 8))
    especie_peligrosa.plot(kind='bar', color='lightgreen')
    plt.title('Árboles con inclinación peligrosa por especie')
    plt.xlabel('Especie')
    plt.ylabel('Cantidad de árboles peligrosos')
    plt.xticks(rotation=90)
    plt.show()
else:
    print("No hay árboles con inclinación peligrosa por especie para graficar.")


import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar el archivo CSV
file_path = 'C:/Users/Usuario/Documents/MARTI/Github/ia-uncuyo-2024/tp7-intro-ml/data/arbolado-mza-dataset.csv'
data = pd.read_csv(file_path)
"""se utiliza para dividir un conjunto de datos en dos (o más) subconjuntos,
comúnmente un conjunto de entrenamiento y uno de prueba o validación.
Es muy útil para tareas de aprendizaje automático, donde se necesita evaluar el
rendimiento de un modelo en datos que no ha visto antes."""

# Dividir el 80% para entrenamiento y 20% para validación de manera uniforme
train_data, validation_data = train_test_split(data, test_size=0.2, random_state=28)

# Guardar los archivos resultantes
train_file_path = 'C:/Users/Usuario/Documents/MARTI/Github/ia-uncuyo-2024/tp7-intro-ml/data/arbolado-mendoza-dataset-train.csv'
validation_file_path = 'C:/Users/Usuario/Documents/MARTI/Github/ia-uncuyo-2024/tp7-intro-ml/data/arbolado-mendoza-dataset-validation.csv'

train_data.to_csv(train_file_path, index=False)
validation_data.to_csv(validation_file_path, index=False)

(train_file_path, validation_file_path)

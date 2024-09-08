import pickle

# Ruta del archivo pickle
pickle_file_path = 'pruebas/dataframe.pkl'

# Cargar el archivo pickle
with open(pickle_file_path, 'rb') as f:
    data = pickle.load(f)

# Ver el contenido del archivo
print(data)
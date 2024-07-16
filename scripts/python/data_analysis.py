# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:57:02 2024

@author: HARMONI

Ejemplo para leer los datos generados en el BOM de Autodesk Inventor
"""
# scripts/python/data_analysis.py

""" IMPORTAMOS MODULOS"""
import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from config.config import DATA_FILE_PATH  # Importa la ruta desde config/config.py


"""IMPORTAMOS LOS FICHEROS"""
ficheroBOM = os.path.join(DATA_FILE_PATH, 'EjemploBoM.csv')
ficheroElectric = os.path.join(DATA_FILE_PATH, 'Electric.csv')
ficheroPBS = os.path.join(DATA_FILE_PATH, 'PBS.csv')
try:
    data_BOM = pd.read_csv(ficheroBOM, encoding='latin1', delimiter=';')
    data_Electric = pd.read_csv(ficheroElectric, encoding='latin1', delimiter=';')
    data_PBS = pd.read_csv(ficheroPBS, encoding='latin1', delimiter=';')
except Exception as e:
    print(f'Error al leer el archivo CSV: {e}')
    raise
    
# Crear una matriz booleana de valores nulos
null_matrix = data_Electric.isnull()

# Configurar la visualización de la matriz de valores nulos con colores
plt.figure(figsize=(10, 6))
sns.heatmap(null_matrix, cbar=False, cmap='viridis', yticklabels=True, xticklabels=True)
plt.title("Matriz de Valores Nulos en el DataFrame")
plt.show()

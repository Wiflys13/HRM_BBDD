# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:57:02 2024

@author: HARMONI

Ejemplo para leer los datos generados en el BOM de Autodesk Inventor
"""
# scripts/python/data_analysis.py
import os
import pandas as pd
from config.config import DATA_FILE_PATH  # Importa la ruta desde config/config.py

ficheroBOM = os.path.join(DATA_FILE_PATH, 'EjemploBoM.csv')

try:
    data = pd.read_csv(ficheroBOM, encoding='latin1', delimiter=';')
except Exception as e:
    print(f'Error al leer el archivo CSV: {e}')
    raise
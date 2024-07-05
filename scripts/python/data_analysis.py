# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:57:02 2024

@author: HARMONI

Ejemplo para leer los datos generados en el BOM de Autodesk Inventor
"""
# scripts/python/data_analysis.py
import pandas as pd
from config.config import DATA_FILE_PATH  # Importa la ruta desde config/config.py

# Leer el archivo CSV usando una codificación específica
data = pd.read_csv(DATA_FILE_PATH, encoding='latin1', delimiter=';') #la codificacion uft-8 no me la reconoce

# Imprimir las primeras filas del DataFrame
print(data.head())

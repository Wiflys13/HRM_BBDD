# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:06:58 2024

@author: HARMONI

#Cada vez que se ejecuta salta: Reloaded modules
"""
## Modificar passwords 
# config/config.py
import os

# Definir la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Definir la ruta al archivo CSV
DATA_FILE_PATH = os.path.join(BASE_DIR, 'data')
PREPROCESS_DATA_FILE_PATH = os.path.join(BASE_DIR, 'data/preprocess')

# Configuración de la base de datos mysql
DB_CONFIG = {
    'host': 'localhost',
    'user': 'harmoni_user',
    'password': 'harmoni',
    'database': 'harmoni_db'
}

# Configuracion de la base de datos mongodb Atlas
MONGODB_URI = 'mongodb+srv://guillermomercant:Harmoni.2024@harmoni.on2fogi.mongodb.net/'
MONGODB_DB_NAME = 'harmoni_db'
MONGODB_COLLECTION_NAME = 'components'


# Configuración de la base de datos mongodb local
MONGODB_URI_LOCAL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME_LOCAL = 'harmoni_db'
MONGO_DB_COLLECTION_PARTNUMBER = 'Components'


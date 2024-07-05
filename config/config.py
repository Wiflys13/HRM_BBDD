# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:06:58 2024

@author: HARMONI
"""

# config/config.py
import os
import logging

# Definir la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Definir la ruta al archivo CSV
DATA_FILE_PATH = os.path.join(BASE_DIR, 'data', 'ejemploBOM.csv')

# Definir la ruta para los logs
LOG_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'app.log')

"""
# Definir una configuración de base de datos
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'usuario'
DB_PASSWORD = 'contraseña'
DB_NAME = 'base_de_datos'

# Definir la URL de una API externa
API_URL = 'https://api.example.com/endpoint'

# Ejemplo de configuración de opciones
DEBUG = True
LOG_LEVEL = 'DEBUG'

# Configuración del logging
if not os.path.exists(os.path.dirname(LOG_FILE_PATH)):
    os.makedirs(os.path.dirname(LOG_FILE_PATH))

logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.DEBUG if DEBUG else logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Imprimir las rutas para verificar que son correctas
print(f'BASE_DIR: {BASE_DIR}')
print(f'DATA_FILE_PATH: {DATA_FILE_PATH}')
print(f'LOG_FILE_PATH: {LOG_FILE_PATH}')
print(f'DB_HOST: {DB_HOST}')
print(f'API_URL: {API_URL}')
print(f'DEBUG: {DEBUG}')
print(f'LOG_LEVEL: {LOG_LEVEL}')

# Ejemplo de uso de logging
logging.debug('Esto es un mensaje de depuración.')
logging.info('Esto es un mensaje informativo.')
logging.warning('Esto es un mensaje de advertencia.')
logging.error('Esto es un mensaje de error.')
logging.critical('Esto es un mensaje crítico.')
"""
import sys
# Importar configuraciones desde el módulo config
project_root = 'C:/Users/HARMONI/Documents/HARMONI/HRM_BBDD'
sys.path.append(project_root)
import os
import csv
import pymongo
import pandas as pd
import numpy as np
from pymongo import MongoClient, errors
from pydantic import ValidationError
from typing import List
from app.logs.logger import logger
from config.config import MONGODB_URI_LOCAL, MONGODB_DB_NAME_LOCAL, PREPROCESS_DATA_FILE_PATH
from app.schemas.thermical import ThermicalSchema  
from app.models.thermical import Thermical

def check_mongo_connection(uri: str) -> bool:
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        client.server_info()
        logger.info("Conexión establecida a MongoDB.")
        return True
    except errors.ServerSelectionTimeoutError as err:
        logger.error(f"No se pudo conectar a MongoDB: {err}")
        return False

def create_unique_index(collection, field_name: str) -> bool:
    try:
        collection.create_index([(field_name, pymongo.ASCENDING)], unique=True)
        logger.info(f"Índice único creado en el campo '{field_name}'.")
        return True
    except errors.OperationFailure as e:
        logger.error(f"Error al crear índice único en el campo '{field_name}': {e}")
        return False

def validate_and_clean_data(data: List[dict]) -> List[dict]:
    valid_data = []
    for item in data:
        try:
            valid_data.append(ThermicalSchema(**item).model_dump(exclude_unset=True))
        except ValidationError as e:
            logger.warning(f"Datos inválidos omitidos: {e}")
    return valid_data

def load_thermical_to_mongo(csv_file_path: str):
    """Carga los datos desde un archivo CSV a MongoDB."""
    # Verificar conexión con MongoDB
    if not check_mongo_connection(MONGODB_URI_LOCAL):
        return
    
    try:
        # Leer el archivo CSV usando pandas
        csv_file = os.path.join(PREPROCESS_DATA_FILE_PATH, csv_file_path)
        df = pd.read_csv(csv_file, encoding='latin1')
        
        # Convertir valores nulos a None
        df = df.replace({np.nan: None})

        # Validar y limpiar datos
        valid_data = []
        for index, row in df.iterrows():
            try:
                thermical = Thermical(
                    ci_identification=row.get('ci_identification'),
                    thermical_heat_dissipated=row.get('thermical_heat_dissipated'),
                    thermical_head_load_to_air=row.get('thermical_head_load_to_air'),
                    thermical_head_load_to_coolant=row.get('thermical_head_load_to_coolant'),
                    thermical_skin_temperature_above_ambient=row.get('thermical_skin_temperature_above_ambient'),
                    thermical_requires_cooling=row.get('thermical_requires_cooling')
                )
                valid_data.append(thermical.model_dump(exclude_unset=True))
            except ValidationError as e:
                logger.warning(f"Error de validación en fila {index}: {row}. Error: {e}")

        # Insertar en MongoDB
        if valid_data:
            client = MongoClient(MONGODB_URI_LOCAL)
            db = client[MONGODB_DB_NAME_LOCAL]
            collection = db['Thermical']
            try:
                result = collection.insert_many(valid_data, ordered=False)
                logger.info(f"Datos importados a la colección 'Thermical' en la base de datos '{MONGODB_DB_NAME_LOCAL}'. Se insertaron {len(result.inserted_ids)} documentos.")
            except errors.BulkWriteError as bwe:
                logger.error(f"Error de escritura masiva: {bwe.details}")
            
            if not create_unique_index(collection, 'ci_identification'):
                logger.warning("Hubo un problema al crear el índice único.")
        else:
            logger.info("No se insertaron datos debido a errores de validación.")
        
    except Exception as e:
        logger.error(f"Error al insertar datos en MongoDB: {str(e)}")

if __name__ == "__main__":
    csv_file_path = 'thermical.csv'  # Cambia el nombre del archivo CSV si es necesario
    load_thermical_to_mongo(csv_file_path)
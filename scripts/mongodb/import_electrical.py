import sys
# Importar configuraciones desde el módulo config
project_root = 'C:/Users/HARMONI/Documents/HARMONI/HRM_BBDD'
sys.path.append(project_root)
import os
import csv
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient, errors
from pydantic import ValidationError
from typing import List, Dict
from app.logs.logger import logger
from config.config import MONGODB_URI_LOCAL, MONGODB_DB_NAME_LOCAL
from config.config import PREPROCESS_DATA_FILE_PATH
from app.schemas.electrical import ElectricalSchema  
from app.models.electrical import Electrical

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
            valid_data.append(ElectricalSchema(**item).model_dump())
        except ValidationError as e:
            logger.warning(f"Datos inválidos omitidos: {e}")
    return valid_data

def load_electrical_to_mongo(csv_file_path: str):
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
                electrical = Electrical(
                    ci_identification=row['ci_identification'],
                    electrical_power_budget=row.get('electrical_power_budget'),
                    electrical_current_ps_only=row.get('electrical_current_ps_only'),
                    electrical_voltaje_dc=row.get('electrical_voltaje_dc'),
                    electrical_voltaje_ac=row.get('electrical_voltaje_ac'),
                    electrical_initialization_power=row.get('electrical_initialization_power'),
                    electrical_initialization_current=row.get('electrical_initialization_current'),
                    electrical_standby_power=row.get('electrical_standby_power'),
                    electrical_standby_current=row.get('electrical_standby_current'),
                    electrical_calibration_power=row.get('electrical_calibration_power'),
                    electrical_calibration_current=row.get('electrical_calibration_current'),
                    electrical_observation_power=row.get('electrical_observation_power'),
                    electrical_observation_current=row.get('electrical_observation_current'),
                    electrical_maintenance_power=row.get('electrical_maintenance_power'),
                    electrical_maintenance_current=row.get('electrical_maintenance_current'),
                    electrical_ups_power_required=row.get('electrical_ups_power_required'),
                    electrical_ups_power_time_required_ups=row.get('electrical_ups_power_time_required_ups'),
                    cables_function=row.get('cables_function'),
                    cables_max_length=row.get('cables_max_length'),
                    cables_length=row.get('cables_length'),
                    cables_outer_diameter=row.get('cables_outer_diameter'),
                    cables_min_bending_radius_dynamic=row.get('cables_min_bending_radius_dynamic'),
                    cables_min_bending_radius_static=row.get('cables_min_bending_radius_static'),
                    cables_mass_density=row.get('cables_mass_density')
                )
                valid_data.append(electrical.model_dump(exclude_unset=True))
            except ValidationError as e:
                logger.warning(f"Error de validación en fila {index}: {row}. Error: {e}")

        # Insertar en MongoDB
        if valid_data:
            client = MongoClient(MONGODB_URI_LOCAL)
            db = client[MONGODB_DB_NAME_LOCAL]
            collection = db['Electrical']
            try:
                result = collection.insert_many(valid_data, ordered=False)
                logger.info(f"Datos importados a la colección 'Electrical' en la base de datos '{MONGODB_DB_NAME_LOCAL}'. Se insertaron {len(result.inserted_ids)} documentos.")
            except errors.BulkWriteError as bwe:
                logger.error(f"Error de escritura masiva: {bwe.details}")
            
            if not create_unique_index(collection, 'ci_identification'):
                logger.warning("Hubo un problema al crear el índice único.")
        else:
            logger.info("No se insertaron datos debido a errores de validación.")
        
    except Exception as e:
        logger.error(f"Error al insertar datos en MongoDB: {str(e)}")

if __name__ == "__main__":
    csv_file_path = 'electrical.csv'  # Cambia el nombre del archivo CSV si es necesario
    load_electrical_to_mongo(csv_file_path)
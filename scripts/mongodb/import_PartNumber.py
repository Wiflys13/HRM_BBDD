#import_partnumber.py
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
from app.schemas.partnumber import PartNumberSchema  # Importa el esquema correcto para PartNumber
from app.models.partnumber import PartNumber  # Asegúrate de que el modelo PartNumber esté disponible

def check_mongo_connection(uri: str) -> bool:
    """Verifica la conexión con MongoDB."""
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        client.server_info()
        logger.info("Conexión establecida a MongoDB.")
        return True
    except errors.ServerSelectionTimeoutError as err:
        logger.error(f"No se pudo conectar a MongoDB: {err}")
        return False

def create_unique_index(collection, field_name: str) -> bool:
    """Crea un índice único en el campo especificado."""
    try:
        collection.create_index([(field_name, pymongo.ASCENDING)], unique=True)
        logger.info(f"Índice único creado en el campo '{field_name}'.")
        return True
    except errors.OperationFailure as e:
        logger.error(f"Error al crear índice único en el campo '{field_name}': {e}")
        return False

def validate_and_clean_data(data: List[dict]) -> List[dict]:
    """Valida y limpia los datos antes de insertarlos en MongoDB."""
    valid_data = []
    for item in data:
        try:
            valid_data.append(PartNumberSchema(**item).model_dump())  # Usa el esquema correcto para validar
        except ValidationError as e:
            logger.warning(f"Datos inválidos omitidos: {e}")
    return valid_data

def load_partnumber_to_mongo(csv_file_path: str):
    """Carga los datos de PartNumber desde un archivo CSV a MongoDB."""
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
                part_number = PartNumber(
                    ci_identification=row['ci_identification'],
                    pbs_name=row['pbs_name'],
                    pbs_acronym=row.get('pbs_acronym'),
                    pbs_level=int(row['pbs_level']),
                    pbs_system=int(row['pbs_system']),
                    pbs_subsystem=int(row['pbs_subsystem']),
                    pbs_module=int(row['pbs_module']),
                    pbs_unit=int(row['pbs_unit']),
                    pbs_assembly=int(row['pbs_assembly']),
                    pbs_subassembly=int(row['pbs_subassembly']),
                    pbs_component=int(row['pbs_component']),
                    notes_and_comments=row.get('notes_and_comments')
                )
                valid_data.append(part_number.model_dump(exclude_unset=True))
            except ValidationError as e:
                logger.warning(f"Error de validación en fila {index}: {row}. Error: {e}")

        # Insertar en MongoDB
        if valid_data:
            client = MongoClient(MONGODB_URI_LOCAL)
            db = client[MONGODB_DB_NAME_LOCAL]
            collection = db['PartNumber']
            try:
                result = collection.insert_many(valid_data, ordered=False)
                logger.info(f"Datos importados a la colección 'PartNumber' en la base de datos '{MONGODB_DB_NAME_LOCAL}'. Se insertaron {len(result.inserted_ids)} documentos.")
            except errors.BulkWriteError as bwe:
                logger.error(f"Error de escritura masiva: {bwe.details}")
            
            if not create_unique_index(collection, 'ci_identification'):
                logger.warning("Hubo un problema al crear el índice único.")
        else:
            logger.info("No se insertaron datos debido a errores de validación.")
        
    except Exception as e:
        logger.error(f"Error al insertar datos en MongoDB: {str(e)}")

if __name__ == "__main__":
    csv_file_path = 'part_numbers.csv'  # Cambia el nombre del archivo CSV si es necesario
    load_partnumber_to_mongo(csv_file_path)
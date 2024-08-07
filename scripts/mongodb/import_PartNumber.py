import os
import sys
import csv
import pymongo
import pandas as pd
from pymongo import MongoClient, errors
from pydantic import ValidationError
from typing import List
import logging

# Importar configuraciones desde el módulo config
project_root = 'C:/Users/HARMONI/Documents/HARMONI/HRM_BBDD'
sys.path.append(project_root)
from config.config import MONGODB_URI_LOCAL, MONGODB_DB_NAME_LOCAL, MONGO_DB_COLLECTION_PARTNUMBER
from config.config import DB_CONFIG, DATA_FILE_PATH
from app.schemas.partnumber import PartNumber

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_mongo_connection(uri: str) -> bool:
    """Verifica si se puede conectar a MongoDB."""
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos
        client.server_info()  # Forzar la verificación de la conexión
        logger.info("Conexión establecida a MongoDB.")
        return True
    except errors.ServerSelectionTimeoutError as err:
        logger.error(f"No se pudo conectar a MongoDB: {err}")
        return False

def create_unique_index(collection, field_name: str) -> bool:
    """Crea un índice único en el campo especificado y retorna True si es exitoso."""
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
            # Usa el modelo de Pydantic para validar los datos
            valid_part_number = PartNumber(**item)
            valid_data.append(valid_part_number.to_dict())
        except ValidationError as e:
            logger.warning(f"Datos inválidos omitidos: {e}")
    return valid_data

def load_part_number_to_mongo(csv_file_path: str):
    csv_file = os.path.join(DATA_FILE_PATH, csv_file_path)
    if not check_mongo_connection(MONGODB_URI_LOCAL):
        return
    
    try:
        client = MongoClient(MONGODB_URI_LOCAL)
        db = client[MONGODB_DB_NAME_LOCAL]
        collection = db[MONGO_DB_COLLECTION_PARTNUMBER]
        
        part_numbers = []

        with open(csv_file, newline='', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
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
                    part_numbers.append(part_number.dict(exclude_unset=True))
                except ValidationError as e:
                    logger.warning(f"Error de validación en fila: {row}. Error: {e}")

        # Insertar los datos válidos en la colección de MongoDB
        try:
            if part_numbers:
                result = collection.insert_many(part_numbers, ordered=False)
                logger.info(f"Datos importados a la colección '{MONGO_DB_COLLECTION_PARTNUMBER}' en la base de datos '{MONGODB_DB_NAME_LOCAL}'. Se insertaron {len(result.inserted_ids)} documentos.")
            else:
                logger.info("No se insertaron datos debido a errores de validación.")
        except errors.BulkWriteError as bwe:
            logger.error(f"Error de escritura masiva: {bwe.details}")
            return
        
        # Crear un índice único en 'ci_identification'
        if not create_unique_index(collection, 'ci_identification'):
            logger.warning("Hubo un problema al crear el índice único.")
        
    except Exception as e:
        logger.error(f"Error al insertar datos en MongoDB: {str(e)}")

if __name__ == "__main__":
    # Ruta al archivo CSV
    csv_file_path = 'preprocess/part_numbers.csv'
    
    # Llamada a la función de carga
    load_part_number_to_mongo(csv_file_path)

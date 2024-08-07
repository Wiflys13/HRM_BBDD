import sys
# Importar configuraciones desde el módulo config
project_root = 'C:/Users/HARMONI/Documents/HARMONI/HRM_BBDD'
sys.path.append(project_root)
import os
import csv
import pymongo
from pymongo import MongoClient, errors
from pydantic import ValidationError
from typing import List
from app.logs.logger import logger
from config.config import MONGODB_URI_LOCAL, MONGODB_DB_NAME_LOCAL, PREPROCESS_DATA_FILE_PATH
from app.schemas.mechanical import MechanicalSchema  
from app.models.mechanical import Mechanical

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
            valid_data.append(MechanicalSchema(**item).model_dump(exclude_unset=True))
        except ValidationError as e:
            logger.warning(f"Datos inválidos omitidos: {e}")
    return valid_data

def load_mechanical_to_mongo(csv_file_path: str):
    csv_file = os.path.join(PREPROCESS_DATA_FILE_PATH, csv_file_path)
    if not check_mongo_connection(MONGODB_URI_LOCAL):
        return
    
    try:
        client = MongoClient(MONGODB_URI_LOCAL)
        db = client[MONGODB_DB_NAME_LOCAL]
        collection = db['Mechanical']
        
        mechanicals = []

        with open(csv_file, newline='', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    mechanical = Mechanical(
                        ci_identification=row['ci_identification'],
                        mechanical_mass=float(row.get('mechanical_mass', 0)),
                        mechanical_material=row.get('mechanical_material'),
                        mechanical_treatment=row.get('mechanical_treatment'),
                        mechanical_coating=row.get('mechanical_coating'),
                        mechanical_step_link=row.get('mechanical_step_link')
                    )
                    mechanicals.append(mechanical.model_dump(exclude_unset=True))
                except ValidationError as e:
                    logger.warning(f"Error de validación en fila: {row}. Error: {e}")

        try:
            if mechanicals:
                result = collection.insert_many(mechanicals, ordered=False)
                logger.info(f"Datos importados a la colección 'Mechanical' en la base de datos '{MONGODB_DB_NAME_LOCAL}'. Se insertaron {len(result.inserted_ids)} documentos.")
            else:
                logger.info("No se insertaron datos debido a errores de validación.")
        except errors.BulkWriteError as bwe:
            logger.error(f"Error de escritura masiva: {bwe.details}")
            return
        
        if not create_unique_index(collection, 'ci_identification'):
            logger.warning("Hubo un problema al crear el índice único.")
        
    except Exception as e:
        logger.error(f"Error al insertar datos en MongoDB: {str(e)}")

if __name__ == "__main__":
    csv_file_path = 'mechanical.csv'  # Cambia el nombre del archivo CSV si es necesario
    load_mechanical_to_mongo(csv_file_path)
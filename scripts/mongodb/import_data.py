
import os
import sys
import pymongo
import pandas as pd
from pymongo import MongoClient, errors
# Importar configuraciones desde el módulo config
project_root = 'C:/Users/HARMONI/Documents/HARMONI/HRM_BBDD'
sys.path.append(project_root)
from config.config import MONGODB_URI_LOCAL, MONGODB_DB_NAME_LOCAL, MONGO_DB_COLLECTION_PARTNUMBER
from config.config import DB_CONFIG, DATA_FILE_PATH

def check_mongo_connection(uri: str) -> bool:
    """Verifica si se puede conectar a MongoDB."""
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos
        client.server_info()  # Forzar la verificación de la conexión
        print("Conexión establecida a MongoDB.")
        return True
    except errors.ServerSelectionTimeoutError as err:
        print(f"No se pudo conectar a MongoDB: {err}")
        return False

def create_unique_index(collection, field_name: str) -> bool:
    """Crea un índice único en el campo especificado y retorna True si es exitoso."""
    try:
        collection.create_index([(field_name, 1)], unique=True)
        print(f"Índice único creado en el campo '{field_name}'.")
        return True
    except errors.OperationFailure as e:
        print(f"Error al crear índice único en el campo '{field_name}': {e}")
        return False

def load_part_number_to_mongo(csv_file_path: str):
    """Carga datos de un archivo CSV a MongoDB. Para la carga se comprueba la conexión y crea índice único en ci_identification."""
    # Verificar la conexión a MongoDB
    if not check_mongo_connection(MONGODB_URI_LOCAL):
        return
    
    try:
        # Conectar a MongoDB
        client = MongoClient(MONGODB_URI_LOCAL)
        db = client[MONGODB_DB_NAME_LOCAL]  # Acceder a la base de datos usando el cliente
        collection = db[MONGO_DB_COLLECTION_PARTNUMBER]  # Acceder a la colección
        
        # Leer el archivo CSV y convertirlo en DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Convertir DataFrame a una lista de diccionarios
        part_numbers_dicts = df.to_dict(orient='records')
        
        # Asegúrate de que cada diccionario no tenga '_id' (MongoDB lo generará automáticamente)
        for item in part_numbers_dicts:
            item.pop('_id', None)  # Asegúrate de eliminar '_id' si existe en los datos

        # Insertar los datos en la colección de MongoDB
        try:
            result = collection.insert_many(part_numbers_dicts, ordered=False)  # ordered=False para manejar errores de inserción
            print(f"Datos importados a la colección '{MONGO_DB_COLLECTION_PARTNUMBER}' en la base de datos '{MONGODB_DB_NAME_LOCAL}'. Se insertaron {len(result.inserted_ids)} documentos.")
        except errors.BulkWriteError as bwe:
            print(f"Error de escritura masiva: {bwe.details}")
            print("Algunos documentos no se insertaron debido a errores de duplicación u otros problemas.")
            return
        
        # Crear un índice único en 'ci_identification'
        if not create_unique_index(collection, 'ci_identification'):
            print("Hubo un problema al crear el índice único.")
        
    except Exception as e:
        print(f"Error al insertar datos en MongoDB: {str(e)}")

if __name__ == "__main__":
    # Ruta al archivo CSV
    csv_file_path = 'data/preprocess/part_numbers.csv'
    
    # Llamada a la función de carga
    load_part_number_to_mongo(csv_file_path)
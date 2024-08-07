#repositories/component_repository.py
from db.session import db_client
from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from models.components import Components
from typing import Optional, Dict, Any, List
import logging

# Configurar el logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def search_component(field: str, key: Any, multiple: bool = False) -> Optional[List[Dict[str, Any]]]:
    try:
        logger.debug(f"Buscando componentes con {field}={key}")

        # Verificar el tipo de dato del campo
        if field.startswith('pbs_') and isinstance(key, str) and key.isdigit():
            key = int(key)
        elif field == "_id" and isinstance(key, str):
            key = ObjectId(key)

        if multiple:
            components = list(db_client.Components.find({field: key}))
            for component in components:
                if '_id' in component:
                    component['_id'] = str(component['_id'])
            return components if components else None
        else:
            component = db_client.Components.find_one({field: key})
            if component and '_id' in component:
                component['_id'] = str(component['_id'])
            return [component] if component else None
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise Exception(f"An error occurred: {str(e)}")

async def get_component_by_field(field_name: str, field_value: Any, multiple: bool = False) -> List[Components]:
    try:
        logger.debug(f"get_component_by_field: field_name={field_name}, field_value={field_value}, multiple={multiple}")
        result = search_component(field_name, field_value, multiple)
        if result is None or len(result) == 0:
            logger.debug(f"No se encontraron componentes con {field_name}={field_value}")
            raise HTTPException(status_code=404, detail="Component not found")
        logger.debug(f"Componentes encontrados: {result}")
        return [Components(**component) for component in result]
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Internal Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")








#Funcion sin loggers. Eliminado el 07/08
# #Funcion para buscar un componente en la base de datos.
# def search_component(field: str, key: Any, multiple: bool = False) -> Optional[List[Dict[str, Any]]]:
#     try:
#         if multiple:
#             # Busca todos los componentes que coinciden con el campo y valor proporcionados
#             components = list(db_client.Components.find({field: key}))
#             for component in components:
#                 if '_id' in component:
#                     component['_id'] = str(component['_id'])
#             return components if components else None
#         else:
#             # Busca un solo componente que coincide con el campo y valor proporcionados
#             component = db_client.Components.find_one({field: key})
#             if component and '_id' in component:
#                 component['_id'] = str(component['_id'])
#             return [component] if component else None
#     except Exception as e:
#         raise Exception(f"An error occurred: {str(e)}")

# # Función auxiliar para manejar la búsqueda
# async def get_component_by_field(field_name: str, field_value: Any, multiple: bool = False) -> List[Components]:
#     try:
#         if field_name == "_id":
#             field_value = ObjectId(field_value)
#         # Llama a la función search_component con el campo y valor
#         result = search_component(field_name, field_value, multiple)
#         if result is None or len(result) == 0:
#             raise HTTPException(status_code=404, detail="Component not found")
#         return [Components(**component) for component in result]
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")







### Funciones obsoletas ###
## Las funciones obsoletas han sido reemplazadas por funciones mas genéricas ##
# Eliminadas el dia 05/08/2024
# def get_component_by_id(id: str):
#     try:
#         object_id = ObjectId(id)
#         component = db_client.Components.find_one({"_id": object_id})
#         return component
#     except Exception as e:
#         raise Exception(f"An error occurred: {str(e)}")

# def get_component_by_ci_identification(ci_identification: str):
#     try:
#         component = db_client.Components.find_one({"ci_identification": ci_identification})
#         if component:
#             # Convertir el _id de BSON a string si es necesario
#             component['_id'] = str(component['_id'])
#             return component
#         else:
#             return None
#     except Exception as e:
#         raise Exception(f'An error occurred: {str(e)}')
#repositories/component_repository.py
from db.session import db_client
from pydantic import BaseModel
from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from models.components import Components
from typing import Optional, Dict, Any, List
from logs.logger import logger
from schemas.mapping import model_schemas


#Funciones generales de busqueda por Coleccion
def search_component(model_name: str, field_name: str, field_value: Any, multiple: bool = False) -> List[Dict[str, Any]]:
    try:
        logger.debug(f"search_component called with model_name={model_name}, field_name={field_name}, field_value={field_value}, multiple={multiple}")
        if model_name not in model_schemas:
            raise ValueError(f"Model {model_name} is not recognized")

        collection = getattr(db_client, model_name)

        if field_name == "_id" and isinstance(field_value, str):
            field_value = ObjectId(field_value)
        elif field_name.startswith('pbs_') and isinstance(field_value, str) and field_value.isdigit():
            field_value = int(field_value)

        query = {field_name: field_value}
        if multiple:
            results = list(collection.find(query))
            for result in results:
                if '_id' in result:
                    result['_id'] = str(result['_id'])
            return results
        else:
            result = collection.find_one(query)
            if result and '_id' in result:
                result['_id'] = str(result['_id'])
            return [result] if result else []
    except Exception as e:
        logger.error(f"Error in search_component: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

async def get_item_by_field(model_name: str, field_name: str, field_value: Any, multiple: bool = False) -> List[BaseModel]:
    try:
        results = search_component(model_name, field_name, field_value, multiple)
        schema = model_schemas.get(model_name)
        if not schema:
            raise ValueError(f"No schema found for model {model_name}")
        if not results:
            raise HTTPException(status_code=404, detail="Item not found")
        return [schema(**item) for item in results]
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


### ------------------------------------------------------------------------- ###
#Funciones para busqueda en Coleccion Componets
# def search_component(field: str, key: Any, multiple: bool = False) -> Optional[List[Dict[str, Any]]]:
#     try:
#         logger.debug(f"Buscando componentes con {field}={key}")
#         # Verificar el tipo de dato del campo
#         if field.startswith('pbs_') and isinstance(key, str) and key.isdigit():
#             key = int(key)
#         elif field == "_id" and isinstance(key, str):
#             key = ObjectId(key)

#         if multiple:
#             components = list(db_client.Components.find({field: key}))
#             for component in components:
#                 if '_id' in component:
#                     component['_id'] = str(component['_id'])
#             return components if components else None
#         else:
#             component = db_client.Components.find_one({field: key})
#             if component and '_id' in component:
#                 component['_id'] = str(component['_id'])
#             return [component] if component else None
#     except Exception as e:
#         logger.error(f"An error occurred: {str(e)}")
#         raise Exception(f"An error occurred: {str(e)}")

async def get_component_by_field(field_name: str, field_value: Any, multiple: bool = False) -> List[Components]:
    try:
        logger.debug(f"get_component_by_field: field_name={field_name}, field_value={field_value}, multiple={multiple}")
        result = search_component(field_name, field_value, multiple)
        if result is None or len(result) == 0:
            logger.debug(f"No se encontraron componentes con {field_name}={field_value}")
            raise HTTPException(status_code=404, detail="Component not found")
        logger.debug(f"Componentes encontrados: {len(result)}")
        return [Components(**component) for component in result]
    except HTTPException as e:
        logger.error(f"HTTPException occurred: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"Internal Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    


async def get_advanced_search_results(model_name: str, filters: Dict) -> List[Dict[str, Any]]:
    try:
        collection = getattr(db_client, model_name)
        query = {k: v for k, v in filters.items() if v is not None}
        results = await collection.find(query).to_list(length=100)  # Ajusta el límite según sea necesario
        for result in results:
            if '_id' in result:
                result['_id'] = str(result['_id'])
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")



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
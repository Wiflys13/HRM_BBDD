#repositories/component_repository.py
from db.session import db_client
from bson import ObjectId
from typing import Optional, Dict, Any



def search_component(field: str, key: Any) -> Optional[Dict[str, Any]]:
    try:
        component = db_client.Components.find_one({field: key})
        if component:
            # Convertir el _id de BSON a string si es necesario
            if '_id' in component:
                component['_id'] = str(component['_id'])
            return component
        return None
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")



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
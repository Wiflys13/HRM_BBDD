## components.py

from fastapi import APIRouter, HTTPException, status
from API.db.models.components import components
from API.db.schemas.components import components_schema
from API.db.client import db_client
from bson import ObjectId

router = APIRouter(prefix = "/components", 
                   tags = ["Components"], 
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

 ### Operaciones GET ##

 #GET por ID#
@router.get("/search/id/{id}")  # Path
async def component(id: str):
    object_id = ObjectId(id)
    result = search_component("_id", object_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Component not found")
    
    return result

#GET por ci_identification#
@router.get("/search/ci_identification/{ci_identification}")  # Path
async def search_by_ci_identification(ci_identification: str):
    result = search_component("pbs.ci_identification", ci_identification)
    if result is None:
        raise HTTPException(status_code=404, detail="Component not found")
    
    return result

# Funciones
def search_component(field: str, key):
    try:
        components = db_client.components.find_one({field: key})
        if components:
            return components_schema(components)
        else:
            return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

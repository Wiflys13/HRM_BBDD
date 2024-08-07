## components.py

from fastapi import APIRouter, HTTPException, status
from models.components import Components
from app.schemas import obsolet_components
from repositories.component_repository import search_component
from db.session import db_client
from app.repositories import component_repository
from bson import ObjectId

router = APIRouter(prefix = "/components", 
                   tags = ["Components"], 
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

### Operaciones GET ###
# GET por ID
@router.get("/search/id/{id}")
async def get_component_by_id(id: str):
    object_id = ObjectId(id)
    result = search_component("_id", object_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return obsolet_components(**result)

# GET por ci_identification
@router.get("/search/ci_identification/{ci_identification}")
async def get_component_by_ci(ci_identification: str):
    result = search_component("ci_identification", ci_identification)
    if result is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return obsolet_components(**result)


# Funciones eliminadas del components.py principal el 07/08/2024:
# Eran funcionales antes de la modificación
# Se reestructura la lógica para buscar componentes.

@router.get("/search/id/{id}")
async def get_component_by_id(id: str):
    try:
        object_id = ObjectId(id)
        result = search_component("_id", object_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Component not found")
        return Components(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/search/ci_identification/{ci_identification}")
async def get_component_by_ci(ci_identification: str):
    try:
        result = search_component("ci_identification", ci_identification)
        if result is None:
            raise HTTPException(status_code=404, detail="Component not found")
        return Components(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/search/acronynm/{pbs_acronym}")
async def get_component_by_ci(pbs_acronym: str):
    try:
        result = search_component("pbs_acronym", pbs_acronym)
        if result is None:
            raise HTTPException(status_code=404, detail="Component not found")
        return Components(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
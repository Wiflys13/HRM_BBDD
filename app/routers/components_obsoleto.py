## components.py

from fastapi import APIRouter, HTTPException, status
from models.components import Components
from schemas import components_obsolet
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
    return components_obsolet(**result)

# GET por ci_identification
@router.get("/search/ci_identification/{ci_identification}")
async def get_component_by_ci(ci_identification: str):
    result = search_component("ci_identification", ci_identification)
    if result is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return components_obsolet(**result)

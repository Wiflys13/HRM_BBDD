#routers/components.py
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from models.components import Components
from repositories.component_repository import search_component

router = APIRouter(prefix="/components", tags=["Components"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

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
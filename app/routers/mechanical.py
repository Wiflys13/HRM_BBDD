from fastapi import APIRouter, status
from logs.logger import logger
from repositories.component_repository import get_item_by_field
from schemas.electrical import ElectricalSchema 

# Define el router
router = APIRouter(prefix="/mechanical", tags=["Mechanical"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

## OPERACIONES CRUD ##

### READ ### 
# Endpoint para buscar por ID
@router.get("/search/id/{id}")
async def get_mechanical_by_id(id: str):
    logger.debug(f"-----> Request received: /search/id/{id}")
    return await get_item_by_field("Mechanical", "_id", id)

# Endpoint para buscar por ci_identification
@router.get("/search/ci_identification/{ci_identification}")
async def get_mechanical_by_ci(ci_identification: str):
    logger.debug(f"-----> Request received: /search/ci_identification/{ci_identification}")
    return await get_item_by_field("Mechanical", "ci_identification", ci_identification)

# Endpoint para buscar por otros campos específicos si es necesario
@router.get("/search/some_field/{some_value}")
async def get_mechanical_by_some_field(some_value: str):
    logger.debug(f"-----> Request received: /search/some_field/{some_value}")
    return await get_item_by_field("Mechanical", "some_field", some_value, multiple=True)

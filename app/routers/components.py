#routers/components.py
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from models.components import Components
from repositories.component_repository import search_component, get_component_by_field
from typing import Any


# Define el router
router = APIRouter(prefix="/components", tags=["Components"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

## OPERACIONES CRUD ##

### READ ### 
# Buscar por ID (único)
@router.get("/search/id/{id}")
async def get_component_by_id(id: str):
    return await get_component_by_field("_id", id)

# Buscar por ci_identification (único)
@router.get("/search/ci_identification/{ci_identification}")
async def get_component_by_ci(ci_identification: str):
    return await get_component_by_field("ci_identification", ci_identification)

# Buscar por pbs_acronym (único)
@router.get("/search/acronym/{pbs_acronym}")
async def get_component_by_acronym(pbs_acronym: str):
    return await get_component_by_field("pbs_acronym", pbs_acronym)

# Buscar por pbs_system (múltiples resultados posibles)
@router.get("/search/system/{pbs_system}")
async def get_component_by_system(pbs_system: str):
    return await get_component_by_field("pbs_system", pbs_system, multiple=True)

# Buscar por pbs_subsystem (múltiples resultados posibles)
@router.get("/search/subsystem/{pbs_subsystem}")
async def get_component_by_subsystem(pbs_subsystem: str):
    return await get_component_by_field("pbs_subsystem", pbs_subsystem, multiple=True)

# Buscar por pbs_module (múltiples resultados posibles)
@router.get("/search/module/{pbs_module}")
async def get_component_by_module(pbs_module: str):
    return await get_component_by_field("pbs_module", pbs_module, multiple=True)

# Buscar por pbs_unit (múltiples resultados posibles)
@router.get("/search/unit/{pbs_unit}")
async def get_component_by_unit(pbs_unit: str):
    return await get_component_by_field("pbs_unit", pbs_unit, multiple=True)

# Buscar por pbs_assembly (múltiples resultados posibles)
@router.get("/search/assembly/{pbs_assembly}")
async def get_component_by_assembly(pbs_assembly: str):
    return await get_component_by_field("pbs_assembly", pbs_assembly, multiple=True)

# Buscar por pbs_subassembly (múltiples resultados posibles)
@router.get("/search/subassembly/{pbs_subassembly}")
async def get_component_by_subassembly(pbs_subassembly: str):
    return await get_component_by_field("pbs_subassembly", pbs_subassembly, multiple=True)

# Buscar por pbs_component (múltiples resultados posibles)
@router.get("/search/component/{pbs_component}")
async def get_component_by_component(pbs_component: str):
    return await get_component_by_field("pbs_component", pbs_component, multiple=True)

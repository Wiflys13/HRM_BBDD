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
    



#### Components eliminados el 08/08/2024. Ahora implementado de forma genérica
# # Define el router
# router = APIRouter(prefix="/components", tags=["Components"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

# ## OPERACIONES CRUD ##

# ### READ ### 
# # Endpoint para buscar por ID
# @router.get("/search/id/{id}")
# async def get_component_by_id(id: str):
#     logger.debug(f"-----> Request received: /search/id/{id}")
#     return await get_component_by_field("_id", id)

# # Endpoint para buscar por ci_identification
# @router.get("/search/ci_identification/{ci_identification}")
# async def get_component_by_ci(ci_identification: str):
#     logger.debug(f"-----> Request received: /search/ci_identification/{ci_identification}")
#     return await get_component_by_field("ci_identification", ci_identification)

# # Endpoint para buscar por pbs_acronym
# @router.get("/search/acronym/{pbs_acronym}")
# async def get_component_by_acronym(pbs_acronym: str):
#     logger.debug(f"-----> Request received: /search/acronym/{pbs_acronym}")
#     return await get_component_by_field("pbs_acronym", pbs_acronym)

# # Endpoint para buscar por pbs_system
# @router.get("/search/system/{pbs_system}")
# async def get_component_by_system(pbs_system: str):
#     logger.debug(f"-----> Request received: /search/system/{pbs_system}")
#     return await get_component_by_field("pbs_system", pbs_system, multiple=True)

# # Endpoint para buscar por pbs_subsystem
# @router.get("/search/subsystem/{pbs_subsystem}")
# async def get_component_by_subsystem(pbs_subsystem: str):
#     logger.debug(f"-----> Request received: /search/subsystem/{pbs_subsystem}")
#     return await get_component_by_field("pbs_subsystem", pbs_subsystem, multiple=True)

# # Endpoint para buscar por pbs_module
# @router.get("/search/module/{pbs_module}")
# async def get_component_by_module(pbs_module: str):
#     logger.debug(f"-----> Request received: /search/module/{pbs_module}")
#     return await get_component_by_field("pbs_module", pbs_module, multiple=True)

# # Endpoint para buscar por pbs_unit
# @router.get("/search/unit/{pbs_unit}")
# async def get_component_by_unit(pbs_unit: str):
#     logger.debug(f"-----> Request received: /search/unit/{pbs_unit}")
#     return await get_component_by_field("pbs_unit", pbs_unit, multiple=True)

# # Endpoint para buscar por pbs_assembly
# @router.get("/search/assembly/{pbs_assembly}")
# async def get_component_by_assembly(pbs_assembly: str):
#     logger.debug(f"-----> Request received: /search/assembly/{pbs_assembly}")
#     return await get_component_by_field("pbs_assembly", pbs_assembly, multiple=True)

# # Endpoint para buscar por pbs_subassembly
# @router.get("/search/subassembly/{pbs_subassembly}")
# async def get_component_by_subassembly(pbs_subassembly: str):
#     logger.debug(f"-----> Request received: /search/subassembly/{pbs_subassembly}")
#     return await get_component_by_field("pbs_subassembly", pbs_subassembly, multiple=True)

# # Endpoint para buscar por pbs_component
# @router.get("/search/component/{pbs_component}")
# async def get_component_by_component(pbs_component: str):
#     logger.debug(f"-----> Request received: /search/component/{pbs_component}")
#     return await get_component_by_field("pbs_component", pbs_component, multiple=True)

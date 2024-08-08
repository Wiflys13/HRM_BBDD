#routers/components.py
from fastapi import APIRouter, status
from pydantic import BaseModel
from logs.logger import logger
from repositories.component_repository import get_component_by_field
from schemas.components import ComponentsSchema
from typing import List



def create_search_router(model_name: str, schema: BaseModel):
    search_router = APIRouter()

    @search_router.get("/search/id/{id}", response_model=List[schema])
    async def get_by_id(id: str):
        logger.debug(f"-----> Request received: /search/id/{id}")
        return await get_component_by_field(model_name, "_id", id)

    @search_router.get("/search/ci_identification/{ci_identification}", response_model=List[schema])
    async def get_by_ci(ci_identification: str):
        logger.debug(f"-----> Request received: /search/ci_identification/{ci_identification}")
        return await get_component_by_field(model_name, "ci_identification", ci_identification)

    @search_router.get("/search/acronym/{pbs_acronym}", response_model=List[schema])
    async def get_by_acronym(pbs_acronym: str):
        logger.debug(f"-----> Request received: /search/acronym/{pbs_acronym}")
        return await get_component_by_field(model_name, "pbs_acronym", pbs_acronym)

    @search_router.get("/search/system/{pbs_system}", response_model=List[schema])
    async def get_by_system(pbs_system: str):
        logger.debug(f"-----> Request received: /search/system/{pbs_system}")
        return await get_component_by_field(model_name, "pbs_system", pbs_system, multiple=True)

    @search_router.get("/search/subsystem/{pbs_subsystem}", response_model=List[schema])
    async def get_by_subsystem(pbs_subsystem: str):
        logger.debug(f"-----> Request received: /search/subsystem/{pbs_subsystem}")
        return await get_component_by_field(model_name, "pbs_subsystem", pbs_subsystem, multiple=True)

    @search_router.get("/search/module/{pbs_module}", response_model=List[schema])
    async def get_by_module(pbs_module: str):
        logger.debug(f"-----> Request received: /search/module/{pbs_module}")
        return await get_component_by_field(model_name, "pbs_module", pbs_module, multiple=True)

    @search_router.get("/search/unit/{pbs_unit}", response_model=List[schema])
    async def get_by_unit(pbs_unit: str):
        logger.debug(f"-----> Request received: /search/unit/{pbs_unit}")
        return await get_component_by_field(model_name, "pbs_unit", pbs_unit, multiple=True)

    @search_router.get("/search/assembly/{pbs_assembly}", response_model=List[schema])
    async def get_by_assembly(pbs_assembly: str):
        logger.debug(f"-----> Request received: /search/assembly/{pbs_assembly}")
        return await get_component_by_field(model_name, "pbs_assembly", pbs_assembly, multiple=True)

    @search_router.get("/search/subassembly/{pbs_subassembly}", response_model=List[schema])
    async def get_by_subassembly(pbs_subassembly: str):
        logger.debug(f"-----> Request received: /search/subassembly/{pbs_subassembly}")
        return await get_component_by_field(model_name, "pbs_subassembly", pbs_subassembly, multiple=True)

    @search_router.get("/search/component/{pbs_component}", response_model=List[schema])
    async def get_by_component(pbs_component: str):
        logger.debug(f"-----> Request received: /search/component/{pbs_component}")
        return await get_component_by_field(model_name, "pbs_component", pbs_component, multiple=True)

    return search_router

# Define el router principal
router = APIRouter(prefix="/components", tags=["Components"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

# Agregamos el router creado
router.include_router(create_search_router("Components", ComponentsSchema))

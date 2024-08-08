#routers/electrical.py
from typing import List
from fastapi import APIRouter, HTTPException, status
from logs.logger import logger
from repositories.component_repository import get_item_by_field
from schemas.electrical import ElectricalSchema
from pydantic import BaseModel


def create_search_router(model_name: str, schema: BaseModel):
    search_router = APIRouter()

    @search_router.get("/search/id/{id}", response_model=List[schema])
    async def get_by_id(id: str):
        logger.debug(f"-----> Request received: /search/id/{id}")
        return await get_item_by_field(model_name, "_id", id)

    @search_router.get("/search/ci_identification/{ci_identification}", response_model=List[schema])
    async def get_by_ci(ci_identification: str):
        logger.debug(f"-----> Request received: /search/ci_identification/{ci_identification}")
        return await get_item_by_field(model_name, "ci_identification", ci_identification)

    @search_router.get("/search/electrical_power_budget/{electrical_power_budget}", response_model=List[schema])
    async def get_by_power_budget(electrical_power_budget: float):
        logger.debug(f"-----> Request received: /search/electrical_power_budget/{electrical_power_budget}")
        return await get_item_by_field(model_name, "electrical_power_budget", electrical_power_budget, multiple=True)

    @search_router.get("/search/electrical_current_ps_only/{electrical_current_ps_only}", response_model=List[schema])
    async def get_by_current_ps_only(electrical_current_ps_only: float):
        logger.debug(f"-----> Request received: /search/electrical_current_ps_only/{electrical_current_ps_only}")
        return await get_item_by_field(model_name, "electrical_current_ps_only", electrical_current_ps_only, multiple=True)

    @search_router.get("/search/electrical_voltaje_dc/{electrical_voltaje_dc}", response_model=List[schema])
    async def get_by_voltaje_dc(electrical_voltaje_dc: float):
        logger.debug(f"-----> Request received: /search/electrical_voltaje_dc/{electrical_voltaje_dc}")
        return await get_item_by_field(model_name, "electrical_voltaje_dc", electrical_voltaje_dc, multiple=True)

    @search_router.get("/search/electrical_voltaje_ac/{electrical_voltaje_ac}", response_model=List[schema])
    async def get_by_voltaje_ac(electrical_voltaje_ac: float):
        logger.debug(f"-----> Request received: /search/electrical_voltaje_ac/{electrical_voltaje_ac}")
        return await get_item_by_field(model_name, "electrical_voltaje_ac", electrical_voltaje_ac, multiple=True)

    @search_router.get("/search/electrical_initialization_power/{electrical_initialization_power}", response_model=List[schema])
    async def get_by_initialization_power(electrical_initialization_power: float):
        logger.debug(f"-----> Request received: /search/electrical_initialization_power/{electrical_initialization_power}")
        return await get_item_by_field(model_name, "electrical_initialization_power", electrical_initialization_power, multiple=True)

    @search_router.get("/search/electrical_initialization_current/{electrical_initialization_current}", response_model=List[schema])
    async def get_by_initialization_current(electrical_initialization_current: float):
        logger.debug(f"-----> Request received: /search/electrical_initialization_current/{electrical_initialization_current}")
        return await get_item_by_field(model_name, "electrical_initialization_current", electrical_initialization_current, multiple=True)

    @search_router.get("/search/electrical_standby_power/{electrical_standby_power}", response_model=List[schema])
    async def get_by_standby_power(electrical_standby_power: float):
        logger.debug(f"-----> Request received: /search/electrical_standby_power/{electrical_standby_power}")
        return await get_item_by_field(model_name, "electrical_standby_power", electrical_standby_power, multiple=True)

    @search_router.get("/search/electrical_standby_current/{electrical_standby_current}", response_model=List[schema])
    async def get_by_standby_current(electrical_standby_current: float):
        logger.debug(f"-----> Request received: /search/electrical_standby_current/{electrical_standby_current}")
        return await get_item_by_field(model_name, "electrical_standby_current", electrical_standby_current, multiple=True)

    @search_router.get("/search/electrical_calibration_power/{electrical_calibration_power}", response_model=List[schema])
    async def get_by_calibration_power(electrical_calibration_power: float):
        logger.debug(f"-----> Request received: /search/electrical_calibration_power/{electrical_calibration_power}")
        return await get_item_by_field(model_name, "electrical_calibration_power", electrical_calibration_power, multiple=True)

    @search_router.get("/search/electrical_calibration_current/{electrical_calibration_current}", response_model=List[schema])
    async def get_by_calibration_current(electrical_calibration_current: float):
        logger.debug(f"-----> Request received: /search/electrical_calibration_current/{electrical_calibration_current}")
        return await get_item_by_field(model_name, "electrical_calibration_current", electrical_calibration_current, multiple=True)

    @search_router.get("/search/electrical_observation_power/{electrical_observation_power}", response_model=List[schema])
    async def get_by_observation_power(electrical_observation_power: float):
        logger.debug(f"-----> Request received: /search/electrical_observation_power/{electrical_observation_power}")
        return await get_item_by_field(model_name, "electrical_observation_power", electrical_observation_power, multiple=True)

    @search_router.get("/search/electrical_observation_current/{electrical_observation_current}", response_model=List[schema])
    async def get_by_observation_current(electrical_observation_current: float):
        logger.debug(f"-----> Request received: /search/electrical_observation_current/{electrical_observation_current}")
        return await get_item_by_field(model_name, "electrical_observation_current", electrical_observation_current, multiple=True)

    @search_router.get("/search/electrical_maintenance_power/{electrical_maintenance_power}", response_model=List[schema])
    async def get_by_maintenance_power(electrical_maintenance_power: float):
        logger.debug(f"-----> Request received: /search/electrical_maintenance_power/{electrical_maintenance_power}")
        return await get_item_by_field(model_name, "electrical_maintenance_power", electrical_maintenance_power, multiple=True)

    @search_router.get("/search/electrical_maintenance_current/{electrical_maintenance_current}", response_model=List[schema])
    async def get_by_maintenance_current(electrical_maintenance_current: float):
        logger.debug(f"-----> Request received: /search/electrical_maintenance_current/{electrical_maintenance_current}")
        return await get_item_by_field(model_name, "electrical_maintenance_current", electrical_maintenance_current, multiple=True)

    @search_router.get("/search/electrical_ups_power_required/{electrical_ups_power_required}", response_model=List[schema])
    async def get_by_ups_power_required(electrical_ups_power_required: bool):
        logger.debug(f"-----> Request received: /search/electrical_ups_power_required/{electrical_ups_power_required}")
        return await get_item_by_field(model_name, "electrical_ups_power_required", electrical_ups_power_required, multiple=True)

    @search_router.get("/search/electrical_ups_power_time_required_ups/{electrical_ups_power_time_required_ups}", response_model=List[schema])
    async def get_by_ups_power_time_required_ups(electrical_ups_power_time_required_ups: float):
        logger.debug(f"-----> Request received: /search/electrical_ups_power_time_required_ups/{electrical_ups_power_time_required_ups}")
        return await get_item_by_field(model_name, "electrical_ups_power_time_required_ups", electrical_ups_power_time_required_ups, multiple=True)

    @search_router.get("/search/cables_function/{cables_function}", response_model=List[schema])
    async def get_by_cables_function(cables_function: str):
        logger.debug(f"-----> Request received: /search/cables_function/{cables_function}")
        return await get_item_by_field(model_name, "cables_function", cables_function, multiple=True)

    @search_router.get("/search/cables_max_length/{cables_max_length}", response_model=List[schema])
    async def get_by_cables_max_length(cables_max_length: float):
        logger.debug(f"-----> Request received: /search/cables_max_length/{cables_max_length}")
        return await get_item_by_field(model_name, "cables_max_length", cables_max_length, multiple=True)

    @search_router.get("/search/cables_length/{cables_length}", response_model=List[schema])
    async def get_by_cables_length(cables_length: float):
        logger.debug(f"-----> Request received: /search/cables_length/{cables_length}")
        return await get_item_by_field(model_name, "cables_length", cables_length, multiple=True)

    @search_router.get("/search/cables_min_diameter/{cables_min_diameter}", response_model=List[schema])
    async def get_by_cables_min_diameter(cables_min_diameter: float):
        logger.debug(f"-----> Request received: /search/cables_min_diameter/{cables_min_diameter}")
        return await get_item_by_field(model_name, "cables_min_diameter", cables_min_diameter, multiple=True)

    @search_router.get("/search/cables_diameter/{cables_diameter}", response_model=List[schema])
    async def get_by_cables_diameter(cables_diameter: float):
        logger.debug(f"-----> Request received: /search/cables_diameter/{cables_diameter}")
        return await get_item_by_field(model_name, "cables_diameter", cables_diameter, multiple=True)

    @search_router.get("/search/cables_required/{cables_required}", response_model=List[schema])
    async def get_by_cables_required(cables_required: int):
        logger.debug(f"-----> Request received: /search/cables_required/{cables_required}")
        return await get_item_by_field(model_name, "cables_required", cables_required, multiple=True)

    @search_router.get("/search/cables_used/{cables_used}", response_model=List[schema])
    async def get_by_cables_used(cables_used: int):
        logger.debug(f"-----> Request received: /search/cables_used/{cables_used}")
        return await get_item_by_field(model_name, "cables_used", cables_used, multiple=True)

    return search_router

# Define el router principal
router = APIRouter(prefix="/electrical", tags=["Electrical"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

# Agregamos el router creado
router.include_router(create_search_router("Electrical", ElectricalSchema))
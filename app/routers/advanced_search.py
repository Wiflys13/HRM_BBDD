# routers/advanced_search.py
from typing import List, Optional
from fastapi import APIRouter, Query
from logs.logger import logger
from repositories.advanced_search_repository import search_by_criteria
from schemas.components import ComponentsSchema

# Crear el router de búsqueda avanzada
advanced_search_router = APIRouter(prefix="/advanced_search", tags=["Advanced Search"])

@advanced_search_router.get("/search", response_model=List[ComponentsSchema])
async def advanced_search(
    pbs_system: Optional[int] = Query(None),
    pbs_subsystem: Optional[int] = Query(None),
    pbs_module: Optional[int] = Query(None),
    pbs_unit: Optional[int] = Query(None),
    pbs_assembly: Optional[int] = Query(None),
    pbs_subassembly: Optional[int] = Query(None),
    pbs_component: Optional[int] = Query(None)
):
    logger.debug(f"-----> Request received: /advanced_search with multiple criteria")
    
    # Construir el diccionario de criterios
    criteria = {}
    
    if pbs_system is not None:
        criteria['pbs_system'] = pbs_system
    if pbs_subsystem is not None:
        criteria['pbs_subsystem'] = pbs_subsystem
    if pbs_module is not None:
        criteria['pbs_module'] = pbs_module
    if pbs_unit is not None:
        criteria['pbs_unit'] = pbs_unit
    if pbs_assembly is not None:
        criteria['pbs_assembly'] = pbs_assembly
    if pbs_subassembly is not None:
        criteria['pbs_subassembly'] = pbs_subassembly
    if pbs_component is not None:
        criteria['pbs_component'] = pbs_component
    
    # Llamar a la función de búsqueda en el repositorio
    results = await search_by_criteria("Components", criteria)
    
    return results

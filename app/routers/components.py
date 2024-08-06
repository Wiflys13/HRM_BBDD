#routers/components.py
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from db.session import db_client
from models.components import Components
from models.partnumber import PartNumber
from models.electrical import Electrical
from models.mechanical import Mechanical
from models.procurement import Procurement
from models.thermical import Thermical
from repositories.component_repository import get_component_by_id, get_component_by_ci_identification
import logging
import math

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/components", tags=["Components"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

### Operaciones GET ##
# GET por ID (para Components)
@router.get("/{id}", response_model=Components)
async def get_component(id: str):
    component = get_component_by_id(id)
    if component is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return Components(**component)

# GET por ci_identification
@router.get("/search/ci_identification/{ci_identification}")
async def get_component_by_ci(ci_identification: str):
    result = get_component_by_ci_identification(ci_identification)
    if result is None:
        raise HTTPException(status_code=404, detail="Component not found")
    return PartNumber(**result)

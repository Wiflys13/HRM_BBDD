#models/partnumber.py
from pydantic import BaseModel, field_validator
from typing import Optional, Literal

class PartNumber(BaseModel):
    """
    Modelo para los datos de PartNumber de un componente
    """
    _id: Optional[str]
    ci_identification: str   
    pbs_name: str
    pbs_acronym: Optional[str] = None
    pbs_level: int
    pbs_system: int
    pbs_subsystem: int
    pbs_module: int
    pbs_unit: int
    pbs_assembly: int
    pbs_subassembly: int
    pbs_component: int
    notes_and_comments: Optional[str] = None
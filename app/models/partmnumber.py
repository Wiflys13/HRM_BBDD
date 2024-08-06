#Clase componentes
from pydantic import BaseModel
from typing import Optional

class PartNumber(BaseModel):
    #pbs
    id: Optional[str]
    ci_identification: str   
    pbs_number: str
    pbs_name: str
    pbs_acronym: str
    pbs_level: int
    pbs_system: int
    pbs_subsystem: int
    pbs_module: int
    pbs_unit: int
    pbs_assembly: int
    pbs_subassembly: int
    pbs_component: int
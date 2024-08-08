#schemas/mecanical.py
from pydantic import BaseModel
from typing import Optional

class MechanicalSchema(BaseModel):
    _id: Optional[str] = None
    ci_identification: str
    mechanical_mass: Optional[float] = None
    mechanical_material: Optional[str] = None
    mechanical_treatment: Optional[str] = None
    mechanical_coating: Optional[str] = None
    mechanical_step_link: Optional[str] = None
    
    class Config:
        json_schema_extra  = {
            "example": {
                "id": "603d2149e4b0a2b7c7d06f5e",
                "ci_identification": "315111 - 0000",
                "mechanical_mass": 20.0,
                "mechanical_material": "Steel",
                "mechanical_treatment": "Heat Treatment",
                "mechanical_coating": "Powder Coating",
                "mechanical_step_link": "Link to step",
                # Incluye valores de ejemplo para otros campos si es necesario
            }
        }
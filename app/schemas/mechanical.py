#schemas/mecanical.py
from pydantic import BaseModel
from typing import Optional

class MechanicalSchema(BaseModel):
    _id: Optional[str] = None
    ci_identification: str
    mechanical_mass: float
    mechanical_material: str
    mechanical_treatment: str
    mechanical_coating: str
    mechanical_step_link: str
    
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
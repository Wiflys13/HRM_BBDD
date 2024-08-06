#models/mechanical.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Mechanical(BaseModel):
    """
    Modelo para los datos mecánicos de un componente
    """
    id: Optional[str]
    ci_identification: str       
    mechanical_mass: float
    mechanical_material: str
    mechanical_treatment: str
    mechanical_coating: str
    mechanical_step_link: str
    
    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v
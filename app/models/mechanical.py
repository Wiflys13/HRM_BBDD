#models/mechanical.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Mechanical(BaseModel):
    """
    Modelo para los datos mecánicos de un componente
    """
    _id: Optional[str] = None
    ci_identification: str
    mechanical_mass: Optional[float] = None
    mechanical_material: Optional[str] = None
    mechanical_treatment: Optional[str] = None
    mechanical_coating: Optional[str] = None
    mechanical_step_link: Optional[str] = None
    
    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v
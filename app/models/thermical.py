#models/thermical.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Thermical(BaseModel):
    """
    Modelo para los datos térmicos de un componente
    """
    _id: Optional[str] = None
    ci_identification: str
    thermical_heat_dissipated: Optional[float] = None
    thermical_head_load_to_air: Optional[float] = None
    thermical_head_load_to_coolant: Optional[float] = None
    thermical_skin_temperature_above_ambient: Optional[float] = None
    thermical_requires_cooling: Optional[float] = None

    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v
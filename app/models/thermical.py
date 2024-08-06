#models/thermical.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Thermical(BaseModel):
    """
    Modelo para los datos térmicos de un componente
    """
    id: Optional[str]
    ci_identification: str   #Clave primaria única
    thermical_heat_dissipated: Optional[float]
    thermical_head_load_to_air: Optional[float]
    thermical_head_load_to_coolant: Optional[float]
    thermical_skin_temperature_above_ambient: Optional[float]         #pendiente de determinar
    thermical_requires_cooling: Optional[float]  

    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v
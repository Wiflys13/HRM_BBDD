#models/electrical.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Electrical(BaseModel):
    """
    Modelo para los datos eléctricos de un componente
    """
    id: Optional[str]
    ci_identification: str       #Clave primaria unica
    electrical_power_budget: float
    electrical_current_ps_only: Optional[str]                     #Pendiente de determinar
    electrical_voltaje_dc: Optional[float]
    electrical_voltaje_ac: Optional[float]
    electrical_initialization_power: Optional[float]
    electrical_initialization_current: Optional[float]
    electrical_standby_power: Optional[float]
    electrical_standby_current: Optional[float]
    electrical_calibration_power: Optional[float]
    electrical_calibration_current: Optional[float]
    electrical_observation_power: Optional[float]
    electrical_observation_current: Optional[float]
    electrical_maintenance_power: Optional[float]
    electrical_maintenance_current: Optional[float]
    electrical_ups_power_required: Optional[str]                       #pendiente de determinar
    electrical_ups_power_time_required_ups: Optional[str] 
    cables_function: Optional[str]
    cables_max_length: Optional[float]
    cables_length: Optional[float]
    cables_outer_diameter: Optional[float]
    cables_min_bending_radius_dynamic: Optional[float]
    cables_min_bending_radius_static: Optional[float]
    cables_mass_density: Optional[float]
    
    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v

# Se pueden añadir mas validadores, como para que no haya números negativos, etc... 

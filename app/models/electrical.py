#models/electrical.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Electrical(BaseModel):
    _id: Optional[str] = None
    ci_identification: str
    electrical_power_budget: Optional[float] = None
    electrical_current_ps_only: Optional[float] = None
    electrical_voltaje_dc: Optional[float] = None
    electrical_voltaje_ac: Optional[float] = None
    electrical_initialization_power: Optional[float] = None
    electrical_initialization_current: Optional[float] = None
    electrical_standby_power: Optional[float] = None
    electrical_standby_current: Optional[float] = None
    electrical_calibration_power: Optional[float] = None
    electrical_calibration_current: Optional[float] = None
    electrical_observation_power: Optional[float] = None
    electrical_observation_current: Optional[float] = None
    electrical_maintenance_power: Optional[float] = None
    electrical_maintenance_current: Optional[float] = None
    electrical_ups_power_required: Optional[bool] = None
    electrical_ups_power_time_required_ups: Optional[float] = None
    cables_function: Optional[str] = None
    cables_max_length: Optional[float] = None
    cables_length: Optional[float] = None
    cables_outer_diameter: Optional[float] = None
    cables_min_bending_radius_dynamic: Optional[float] = None
    cables_min_bending_radius_static: Optional[float] = None
    cables_mass_density: Optional[float] = None
    
    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v

# Se pueden añadir mas validadores, como para que no haya números negativos, etc... 

#schemas/electrical.py

from pydantic import BaseModel
from typing import Optional

class ElectricalSchema(BaseModel):
    id: Optional[str]
    ci_identification: str
    electrical_power_budget: float
    electrical_current_ps_only: Optional[str]
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
    electrical_ups_power_required: Optional[str]
    electrical_ups_power_time_required_ups: Optional[str]
    cables_function: Optional[str]
    cables_max_length: Optional[float]
    cables_length: Optional[float]
    cables_outer_diameter: Optional[float]
    cables_min_bending_radius_dynamic: Optional[float]
    cables_min_bending_radius_static: Optional[float]
    cables_mass_density: Optional[float]
    
    class Config:
        schema_extra = {
            "example": {
                "id": "603d2149e4b0a2b7c7d06f5d",
                "ci_identification": "315112-0000",
                "electrical_power_budget": 150.0,
                "electrical_current_ps_only": "Details",
                "electrical_voltaje_dc": 12.0,
                "electrical_voltaje_ac": 220.0,
            }
        }
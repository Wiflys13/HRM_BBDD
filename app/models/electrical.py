from pydantic import BaseModel
from typing import Optional

class Electrical(BaseModel):
    # electrical
    id: Optional[str]
    ci_identification: str       
    electrical_power_budget: float
    electrical_current_ps_only: str                     #Pendiente de determinar
    electrical_voltaje_dc: float
    electrical_voltaje_ac: float
    electrical_initialization_power: float
    electrical_initialization_current: float
    electrical_standby_power: float
    electrical_standby_standby: float
    electrical_calibration_power: float
    electrical_calibration_current: float
    electrical_observation_power: float
    electrical_observation_current: float
    electrical_maintenance_power: float
    electrical_maintenance_current: float
    electrical_ups_power_required: str                       #pendiente de determinar
    electrical_ups_power_time_required_ups: str 
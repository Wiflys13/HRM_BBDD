from pydantic import BaseModel
from typing import Optional


#Clase componentes
class components(BaseModel):
    #pbs
    id: Optional[str]   
    pbs_number: str
    pbs_name: str
    pbs_acronym: str
    pbs_level: int
    pbs_system: int
    pbs_subsystem: int
    pbs_module: int
    pbs_unit: int
    pbs_assembly: int
    pbs_subassembly: int
    pbs_component: int

    # component
    pbs_is_component: bool
    component_status: str
    component_description: str
    component_type: str
    component_field:str

    # procurement
    procurement_supplier: str
    procurement_manufacturer: str
    manufacturer_part_number: str
    procurement_catalog_reference: str
    procurement_cost_unit: float
    procurement_cost_status: str
    procurement_quantity: int

    # mechanical
    mechanical_mass: float
    mechanical_material: str
    mechanical_treatment: str
    mechanical_coating: str
    mechanical_step_link: str

    # electrical
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
    electrical_ups_power_time_required_ups: str              #pendiente de determinar

    # thermical
    thermical_heat_dissipated: float
    thermical_head_load_to_air: float
    thermical_head_load_to_coolant: float
    thermical_skin_temperature_above_ambient: float         #pendiente de determinar
    thermical_requires_cooling: float                       #pendiente de determinar

    # cables
    cables_function: str
    cables_max_length: float
    cables_length: float
    cables_outer_diameter: float
    cables_min_bending_radius_dynamic: float
    cables_min_bending_radius_static: float
    cables_mass_density: float
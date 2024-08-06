## Components Schema ##


import math

def safe_value(value):
    """Convert NaN to None for JSON serialization."""
    if isinstance(value, float) and math.isnan(value):
        return None
    return value

def components_schema(components) -> dict:
    return {
        "id": str(components.get("_id")),
        # pbs
        "pbs_number": safe_value(components.get("pbs", {}).get("ci_identification", None)),
        "pbs_name": safe_value(components.get("pbs", {}).get("name", None)),
        "pbs_acronym": safe_value(components.get("pbs", {}).get("acronym", None)),
        "pbs_level": safe_value(components.get("pbs", {}).get("level", None)),
        "pbs_system": safe_value(components.get("pbs", {}).get("structure", {}).get("system", None)),
        "pbs_subsystem": safe_value(components.get("pbs", {}).get("structure", {}).get("subsystem", None)),
        "pbs_module": safe_value(components.get("pbs", {}).get("structure", {}).get("module", None)),
        "pbs_unit": safe_value(components.get("pbs", {}).get("structure", {}).get("unit", None)),
        "pbs_assembly": safe_value(components.get("pbs", {}).get("structure", {}).get("assembly", None)),
        "pbs_subassembly": safe_value(components.get("pbs", {}).get("structure", {}).get("subassembly", None)),
        "pbs_component": safe_value(components.get("pbs", {}).get("structure", {}).get("component", None)),
        # Components
        "pbs_is_component": safe_value(components.get("component", {}).get("is_component", None)),
        "component_status": safe_value(components.get("component", {}).get("status", None)),
        "component_description": safe_value(components.get("component", {}).get("description", None)),
        "component_type": safe_value(components.get("component", {}).get("type", None)),
        "component_field": safe_value(components.get("component", {}).get("field", None)),
        # Procurement
        "procurement_supplier": safe_value(components.get("procurement", {}).get("supplier", None)),
        "procurement_manufacturer": safe_value(components.get("procurement", {}).get("manufacturer", None)),
        "manufacturer_part_number": safe_value(components.get("procurement", {}).get("part_number", None)),
        "procurement_catalog_reference": safe_value(components.get("procurement", {}).get("catalog_reference", None)),
        "procurement_cost_unit": safe_value(components.get("procurement", {}).get("cost_unit", None)),
        "procurement_cost_status": safe_value(components.get("procurement", {}).get("cost_status", None)),
        "procurement_quantity": safe_value(components.get("procurement", {}).get("quantity", None)),
        # Mechanical
        "mechanical_mass": safe_value(components.get("mechanical", {}).get("mass", None)),
        "mechanical_material": safe_value(components.get("mechanical", {}).get("material", None)),
        "mechanical_treatment": safe_value(components.get("mechanical", {}).get("treatment", None)),
        "mechanical_coating": safe_value(components.get("mechanical", {}).get("coating", None)),
        "mechanical_step_link": safe_value(components.get("mechanical", {}).get("step_link", None)),
        # Electrical
        "electrical_power_budget": safe_value(components.get("electrical", {}).get("electrical_power_budget", None)),
        "electrical_current_ps_only": safe_value(components.get("electrical", {}).get("current_ps_only", None)),
        "electrical_voltaje_dc": safe_value(components.get("electrical", {}).get("voltaje_dc", None)),
        "electrical_voltaje_ac": safe_value(components.get("electrical", {}).get("voltaje_ac", None)),
        "electrical_initialization_power": safe_value(components.get("electrical", {}).get("initialization", {}).get("power", None)),
        "electrical_initialization_current": safe_value(components.get("electrical", {}).get("initialization", {}).get("current", None)),
        "electrical_standby_power": safe_value(components.get("electrical", {}).get("standby", {}).get("power", None)),
        "electrical_standby_current": safe_value(components.get("electrical", {}).get("standby", {}).get("standby", None)),
        "electrical_calibration_power": safe_value(components.get("electrical", {}).get("calibration", {}).get("power", None)),
        "electrical_calibration_current": safe_value(components.get("electrical", {}).get("calibration", {}).get("current", None)),
        "electrical_observation_power": safe_value(components.get("electrical", {}).get("observation", {}).get("power", None)),
        "electrical_observation_current": safe_value(components.get("electrical", {}).get("observation", {}).get("current", None)),
        "electrical_maintenance_power": safe_value(components.get("electrical", {}).get("maintenance", {}).get("power", None)),
        "electrical_maintenance_current": safe_value(components.get("electrical", {}).get("maintenance", {}).get("current", None)),
        "electrical_ups_power_required": safe_value(components.get("electrical", {}).get("ups_power", {}).get("required", None)),
        "electrical_ups_power_time_required_ups": safe_value(components.get("electrical", {}).get("ups_power", {}).get("time_required_ups", None)),
        # Thermical
        "thermical_heat_dissipated": safe_value(components.get("thermical", {}).get("heat_dissipated", None)),
        "thermical_head_load_to_air": safe_value(components.get("thermical", {}).get("head_load_to_air", None)),
        "thermical_head_load_to_coolant": safe_value(components.get("thermical", {}).get("head_load_to_coolant", None)),
        "thermical_skin_temperature_above_ambient": safe_value(components.get("thermical", {}).get("skin_temperature_above_ambient", None)),
        "thermical_requires_cooling": safe_value(components.get("thermical", {}).get("requires_cooling", None)),
        # Cables
        "cables_function": safe_value(components.get("cables", {}).get("function", None)),
        "cables_max_length": safe_value(components.get("cables", {}).get("max_length", None)),
        "cables_length": safe_value(components.get("cables", {}).get("length", None)),
        "cables_outer_diameter": safe_value(components.get("cables", {}).get("outer_diameter", None)),
        "cables_min_bending_radius_dynamic": safe_value(components.get("cables", {}).get("min_bending_radius_dynamic", None)),
        "cables_min_bending_radius_static": safe_value(components.get("cables", {}).get("min_bending_radius_static", None)),
        "cables_mass_density": safe_value(components.get("cables", {}).get("mass_density", None))
    }

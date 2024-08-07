#schemas/components.py

from pydantic import BaseModel, field_validator
from typing import Optional, Literal, Any

class ComponentsSchema(BaseModel):
    _id: Optional[str]
    ci_identification: str
    pbs_name: str
    pbs_acronym: Optional[str] = None
    pbs_level: int
    pbs_system: int
    pbs_subsystem: int
    pbs_module: int
    pbs_unit: int
    pbs_assembly: int
    pbs_subassembly: int
    pbs_component: int
    pbs_is_component: Optional[bool] = None
    component_type: Optional[str] = None
    component_field: Optional[bool] = None
    component_status: Optional[str] = None
    component_description: Optional[str] = None
    component_lab_tool: Optional[str] = None
    institution_responsible: Optional[str] = None
    notes_and_comments: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "_id": "603d2149e4b0a2b7c7d06f5c",
                "ci_identification": "315111-000",
                "pbs_name": "ICU Integrating Sphere Structure",
                "pbs_acronym": "CM IISS",
                "pbs_level": 6,
                "pbs_system": 3,
                "pbs_subsystem": 1,
                "pbs_module": 5,
                "pbs_unit": 1,
                "pbs_assembly": 1,
                "pbs_subassembly": 1,
                "pbs_component": 0,
                "pbs_is_component": True,
                "component_type": "Mechanical",
                "component_field": True,
                "component_status": "Active",
                "component_description": "Description of the component",
                "component_lab_tool": "Tool Name",
                "institution_responsible": "CAB",
                "notes_and_comments": "notas y comentarios"
            }
        }
#models/is_components.py
from pydantic import BaseModel, field_validator
from typing import Optional, Literal

# Define your models
class IsComponent(BaseModel):
    _id: Optional[str] = None
    ci_identification: str
    pbs_is_component: Optional[bool] = None
    component_type: Optional[str] = None
    component_field: Optional[bool] = None
    component_status: Optional[str] = None
    component_description: Optional[str] = None
    component_lab_tool: Optional[bool] = None
    institution_responsible: Optional[str] = None
    notes_and_comments: Optional[str] = None
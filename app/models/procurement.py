#models/procurement.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Procurement(BaseModel):
    """
    Modelo para los datos de compras de un componente
    """
    _id: Optional[str] = None
    ci_identification: str 
    procurement_supplier: Optional[str] = None
    procurement_manufacturer: Optional[str] = None
    manufacturer_part_number: Optional[str] = None
    procurement_catalog_reference: Optional[str] = None
    procurement_cost_unit: Optional[float] = None
    procurement_cost_status: Optional[str] = None
    procurement_quantity: Optional[float] = None
    
    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v
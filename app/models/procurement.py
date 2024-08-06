#models/procurement.py
from pydantic import BaseModel, field_validator
from typing import Optional

class Procurement(BaseModel):
    """
    Modelo para los datos de compras de un componente
    """
    id: Optional[str]
    ci_identification: str
    procurement_supplier: str
    procurement_manufacturer: str
    manufacturer_part_number: str
    procurement_catalog_reference: str
    procurement_cost_unit: float
    procurement_cost_status: str
    procurement_quantity: int
    
    @field_validator('ci_identification')
    def validate_ci_identification(cls, v):
        if not v:
            raise ValueError('ci_identification cannot be empty')
        return v
#schemas/procurement.py

from pydantic import BaseModel
from typing import Optional

class ProcurementSchema(BaseModel):
    _id: Optional[str] = None
    ci_identification: str 
    procurement_supplier: Optional[str] = None
    procurement_manufacturer: Optional[str] = None
    manufacturer_part_number: Optional[str] = None
    procurement_catalog_reference: Optional[str] = None
    procurement_cost_unit: Optional[float] = None
    procurement_cost_status: Optional[str] = None
    procurement_quantity: Optional[float] = None
    
    class Config:
        json_schema_extra  = {
            "example": {
                "id": "603d2149e4b0a2b7c7d06f5f",
                "ci_identification": "315111-00001",
                "procurement_supplier": "Supplier Name",
                "procurement_manufacturer": "Manufacturer Name",
                "manufacturer_part_number": "MPN123",
                "procurement_catalog_reference": "CatalogRef123",
                "procurement_cost_unit": 50.0,
                "procurement_cost_status": "Available",
                "procurement_quantity": 100,
                # Incluye valores de ejemplo para otros campos si es necesario
            }
        }
#schemas/procurement.py

from pydantic import BaseModel
from typing import Optional

class ProcurementSchema(BaseModel):
    id: Optional[str]
    ci_identification: str
    procurement_supplier: str
    procurement_manufacturer: str
    manufacturer_part_number: str
    procurement_catalog_reference: str
    procurement_cost_unit: float
    procurement_cost_status: str
    procurement_quantity: int
    
    class Config:
        schema_extra = {
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
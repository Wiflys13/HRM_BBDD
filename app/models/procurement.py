from pydantic import BaseModel
from typing import Optional

class Procurement(BaseModel):
    # procurement
    id: Optional[str]
    ci_identification: str
    procurement_supplier: str
    procurement_manufacturer: str
    manufacturer_part_number: str
    procurement_catalog_reference: str
    procurement_cost_unit: float
    procurement_cost_status: str
    procurement_quantity: int
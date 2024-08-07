# routers/combined.py
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from repositories.combined_repository import get_combined_data

router = APIRouter(prefix="/combined", tags=["Combined"], responses={404: {"description": "Not found"}})

@router.get("/{ci_identification}", response_model=Dict[str, Any])
async def get_combined_data_by_ci(ci_identification: str):
    try:
        data = await get_combined_data(ci_identification)
        if not data:
            raise HTTPException(status_code=404, detail="Data not found")
        return data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

from fastapi import APIRouter, HTTPException, Body
from models import HMO
from database import *
from typing import List, Union

router = APIRouter()

# HMO Endpoints
@router.post("/", response_model=List[HMO])
async def post_hmo(hmo: Union[HMO, List[HMO]] = Body(...)):
    if isinstance(hmo, HMO):
        hmo = [hmo]  # Convert to a list with a single item if it's not already a list

    response = []
    for item in hmo:
        created_hmo = await create_hmo(item)
        if created_hmo:
            response.append(created_hmo)
        else:
            raise HTTPException(status_code=400, detail="Something went wrong with one of the HMOs")

    return response


@router.get("/{id}/", response_model=HMO)
async def get_hmo(id: str):
    response = await fetch_one_hmo(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No HMO found with the id {id}")

@router.get("/", response_model=List[HMO])
async def get_hmos():
    response = await fetch_hmos()
    return response

@router.put("/{id}/", response_model=HMO)
async def put_hmo(id: str, update_data: HMO):
    update_data_dict = update_data.model_dump(exclude_unset=True)  # Create a dict from the model
    response = await update_hmo(id, update_data_dict)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No hmo found with the id {id}")


@router.delete("/{id}/")
async def delete_hmo(id: str):
    response = await remove_hmo(id)
    if response:
        return {"message": "Successfully deleted HMO"}
    raise HTTPException(status_code=404, detail=f"No HMO found with the id {id}")


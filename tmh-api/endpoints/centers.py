from fastapi import APIRouter, HTTPException, Body
from models import Centers
from database import *
from typing import List, Union

router = APIRouter()

# Center Endpoints
@router.post("/", response_model=List[Centers])
async def post_center(center: Union[Centers, List[Centers]] = Body(...)):
    if isinstance(center, Centers):
        center = [center]  # Convert to a list with a single item if it's not already a list

    response = []
    for item in center:
        created_center = await create_center(item)
        if created_center:
            response.append(created_center)
        else:
            raise HTTPException(status_code=400, detail="Something went wrong with one of the centers")

    return response


@router.get("/{id}/", response_model=Centers)
async def get_center(id: str):
    response = await fetch_one_center(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")

@router.get("/", response_model=List[Centers])
async def get_centers():
    response = await fetch_centers()
    return response


@router.put("/{id}/", response_model=Centers)
async def put_center(id: str, update_data: Centers):
    update_data_dict = update_data.model_dump(exclude_unset=True)  # Create a dict from the model
    response = await update_center(id, update_data_dict)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")

@router.delete("/{id}/")
async def delete_center(id: str):
    response = await remove_center(id)
    if response:
        return {"message": "Successfully deleted center"}
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")


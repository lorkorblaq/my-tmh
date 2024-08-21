from fastapi import APIRouter, HTTPException
from models import Centers
from database import *

router = APIRouter()

# Center Endpoints
@router.post("/center/", response_model=Centers)
async def post_center(center: Centers):
    response = await create_center(center)  # Convert the Pydantic model to a dict
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@router.get("/center/{id}/", response_model=Centers)
async def get_center(id: str):
    response = await fetch_one_center(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")

@router.get("/centers/", response_model=List[Centers])
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

@router.delete("/center/{id}/")
async def delete_center(id: str):
    response = await remove_center(id)
    if response:
        return {"message": "Successfully deleted center"}
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")


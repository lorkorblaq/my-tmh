from fastapi import APIRouter, HTTPException
from models import Users
from database import *

router = APIRouter()

@router.post("/", response_model=Users)
async def post_user(user: Users):
    response = await create_user(user)
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@router.get("/{id}/", response_model=Users)
async def get_user(id: str):
    response = await fetch_one_user(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No user found with the id {id}")

@router.get("/", response_model=List[Users])
async def get_users():
    response = await fetch_users()
    return response

@router.put("/{id}/", response_model=Users)
async def put_user(id: str, update_data: Users):
    update_data_dict = update_data.model_dump(exclude_unset=True)  # Create a dict from the model
    response = await update_user(id, update_data_dict)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No user found with the id {id}")


@router.delete("/{id}/")
async def delete_user(id: str):
    response = await remove_user(id)
    if response:
        return {"message": "Successfully deleted user"}
    raise HTTPException(status_code=404, detail=f"No user found with the id {id}")

from fastapi import APIRouter, HTTPException, Body
from models import Tests
from database import *
from typing import List, Union

router = APIRouter()

@router.post("/", response_model=List[Tests])
async def post_tests(tests: Union[Tests, List[Tests]] = Body(...)):
    if isinstance(tests, Tests):
        tests = [tests]  # Convert to a list with a single item if it's not already a list

    response = []
    for test in tests:
        created_test = await create_tests(test)
        if created_test:
            response.append(created_test)
        else:
            raise HTTPException(status_code=400, detail="Something went wrong with one of the tests")
    
    return response

@router.get("/{id}/", response_model=Tests)
async def get_tests(id: str):
    response = await fetch_one_tests(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No Tests found with the id {id}")

@router.get("/", response_model=List[Tests])
async def get_tests():
    response = await fetch_tests()
    return response

@router.put("/{id}/", response_model=Tests)
async def put_tests(id: str, update_data: Tests):
    update_data_dict = update_data.model_dump(exclude_unset=True)  # Create a dict from the model
    response = await update_tests(id, update_data_dict)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No tests found with the id {id}")



@router.delete("/{id}/")
async def delete_tests(id: str):
    response = await remove_tests(id)
    if response:
        return {"message": "Successfully deleted Tests"}
    raise HTTPException(status_code=404, detail=f"No Tests found with the id {id}")


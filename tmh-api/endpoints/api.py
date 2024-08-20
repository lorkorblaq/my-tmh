from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Users, HMO, Centers, Todo
from database import *

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def read_root():
    return {"endpoints": "api"}

# User Endpoints
@app.post("/api/user/", response_model=Users)
async def post_user(user: Users):
    response = await create_user(user)  # Convert the Pydantic model to a dict
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@app.get("/api/user/{id}/", response_model=Users)
async def get_user(id: str):
    response = await fetch_one_user(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No user found with the id {id}")

@app.get("/api/users/", response_model=List[Users])
async def get_users():
    response = await fetch_users()
    return response

@app.put("/api/user/{id}/", response_model=Users)
async def put_user(id: str, update_data: Users):
    response = await update_user(id, update_data(exclude_unset=True))  # Convert to dict
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No user found with the id {id}")

@app.delete("/api/user/{id}/")
async def delete_user(id: str):
    response = await remove_user(id)
    if response:
        return {"message": "Successfully deleted user"}
    raise HTTPException(status_code=404, detail=f"No user found with the id {id}")

# HMO Endpoints
@app.post("/api/hmo/", response_model=HMO)
async def post_hmo(hmo: HMO):
    response = await create_hmo(hmo)  # Convert the Pydantic model to a dict
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@app.get("/api/hmo/{id}/", response_model=HMO)
async def get_hmo(id: str):
    response = await fetch_one_hmo(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No HMO found with the id {id}")

@app.get("/api/hmos/", response_model=List[HMO])
async def get_hmos():
    response = await fetch_hmos()
    return response

@app.put("/api/hmo/{id}/", response_model=HMO)
async def put_hmo(id: str, desc: str):
    response = await update_hmo(id, {"description": desc})
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No HMO found with the id {id}")

@app.delete("/api/hmo/{id}/")
async def delete_hmo(id: str):
    response = await remove_hmo(id)
    if response:
        return {"message": "Successfully deleted HMO"}
    raise HTTPException(status_code=404, detail=f"No HMO found with the id {id}")

# Center Endpoints
@app.post("/api/center/", response_model=Centers)
async def post_center(center: Centers):
    response = await create_center(center)  # Convert the Pydantic model to a dict
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@app.get("/api/center/{id}/", response_model=Centers)
async def get_center(id: str):
    response = await fetch_one_center(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")

@app.get("/api/centers/", response_model=List[Centers])
async def get_centers():
    response = await fetch_centers()
    return response

@app.put("/api/center/{id}/", response_model=Centers)
async def put_center(id: str, desc: str):
    response = await update_center(id, {"description": desc})
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")

@app.delete("/api/center/{id}/")
async def delete_center(id: str):
    response = await remove_center(id)
    if response:
        return {"message": "Successfully deleted center"}
    raise HTTPException(status_code=404, detail=f"No center found with the id {id}")

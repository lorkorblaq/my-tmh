import motor.motor_asyncio
from bson import ObjectId
from models import Users, HMO, Centers, Todo
from typing import Optional, List

# Database connection
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.tmh

# Collection references
users_collection = database.users
hmo_collection = database.hmo
centers_collection = database.centers
todo_collection = database.todo

# Helper function to handle ObjectId conversion
def str_to_objectid(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except Exception as e:
        raise ValueError(f"Invalid ID format: {e}")

# Users
async def create_user(user: Users) -> dict:
    user_dict = user.model_dump()
    result = await users_collection.insert_one(user_dict)
    return await users_collection.find_one({"_id": result.inserted_id})

async def update_user(id: str, data: dict) -> Optional[dict]:
    object_id = str_to_objectid(id)
    await users_collection.update_one({"_id": object_id}, {"$set": data})
    return await users_collection.find_one({"_id": object_id})

async def fetch_one_user(id: str) -> Optional[dict]:
    return await users_collection.find_one({"_id": str_to_objectid(id)})

async def fetch_users() -> List[dict]:
    users = []
    async for document in users_collection.find({}):
        users.append(document)
    return users

async def remove_user(id: str) -> bool:
    result = await users_collection.delete_one({"_id": str_to_objectid(id)})
    return result.deleted_count > 0

# HMO
async def create_hmo(hmo: HMO) -> dict:
    hmo_dict = hmo.model_dump()
    result = await hmo_collection.insert_one(hmo_dict)
    return await hmo_collection.find_one({"_id": result.inserted_id})

async def update_hmo(id: str, data: dict) -> Optional[dict]:
    object_id = str_to_objectid(id)
    await hmo_collection.update_one({"_id": object_id}, {"$set": data})
    return await hmo_collection.find_one({"_id": object_id})

async def fetch_one_hmo(id: str) -> Optional[dict]:
    return await hmo_collection.find_one({"_id": str_to_objectid(id)})

async def fetch_hmos() -> List[dict]:
    hmos = []
    async for document in hmo_collection.find({}):
        hmos.append(document)
    return hmos

async def remove_hmo(id: str) -> bool:
    result = await hmo_collection.delete_one({"_id": str_to_objectid(id)})
    return result.deleted_count > 0

# Centers
async def create_center(center: Centers) -> dict:
    center_dict = center.model_dump()
    result = await centers_collection.insert_one(center_dict)
    return await centers_collection.find_one({"_id": result.inserted_id})

async def update_center(id: str, data: dict) -> Optional[dict]:
    object_id = str_to_objectid(id)
    await centers_collection.update_one({"_id": object_id}, {"$set": data})
    return await centers_collection.find_one({"_id": object_id})

async def fetch_one_center(id: str) -> Optional[dict]:
    return await centers_collection.find_one({"_id": str_to_objectid(id)})

async def fetch_centers() -> List[dict]:
    centers = []
    async for document in centers_collection.find({}):
        centers.append(document)
    return centers

async def remove_center(id: str) -> bool:
    result = await centers_collection.delete_one({"_id": str_to_objectid(id)})
    return result.deleted_count > 0

# Todos
async def create_todo(todo: Todo) -> dict:
    todo_dict = todo.model_dump()
    result = await todo_collection.insert_one(todo_dict)
    return await todo_collection.find_one({"_id": result.inserted_id})

async def update_todo(title: str, desc: str) -> Optional[dict]:
    await todo_collection.update_one({"title": title}, {"$set": {"description": desc}})
    return await todo_collection.find_one({"title": title})

async def fetch_one_todo(title: str) -> Optional[dict]:
    return await todo_collection.find_one({"title": title})

async def fetch_all_todos() -> List[Todo]:
    todos = []
    async for document in todo_collection.find({}):
        todos.append(Todo(**document))
    return todos

async def remove_todo(title: str) -> bool:
    result = await todo_collection.delete_one({"title": title})
    return result.deleted_count > 0

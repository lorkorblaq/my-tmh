from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from typing import List, Optional
from validators import validate_name, validate_ids, convert_mongo_id

# Constants for field validation
PHONE_REGEX = r'^\+?[1-9]\d{1,14}$'  # E.164 format


class Users(BaseModel):
    id: Optional[str] = None 
    name: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)
    email: EmailStr
    password: str = Field(..., min_length=8)
    hmo_ids: List[str] = Field(default_factory=list)  # List of HMO IDs associated with the user

    @field_validator('name')
    def validate_name(cls, value):
        return validate_name(value)
    @model_validator(mode='before')
    def convert_mongo_id(cls, values):
        return convert_mongo_id(values)

class HMO(BaseModel):
    id: Optional[str] = None 
    name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    address: str
    phone: str = Field(..., pattern=PHONE_REGEX)
    email: EmailStr
    website: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    @model_validator(mode='before')
    def convert_mongo_id(cls, values):
        return convert_mongo_id(values)

class Centers(BaseModel):
    id: Optional[str] = None 
    name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    address: str
    phone: str = Field(..., pattern=PHONE_REGEX)
    email: EmailStr
    website: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    hmo: List[str] = Field(default_factory=list)  # List of HMO IDs associated with the center

    @field_validator('hmo')
    def validate_ids(cls, value):
        return validate_ids(value)
    @model_validator(mode='before')
    def convert_mongo_id(cls, values):
        return convert_mongo_id(values)
    
class Tests(BaseModel):
    id: Optional[str] = None 
    name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    description: str
    price: float = Field(..., gt=0)
    center_id: list[str]  # ID of the center where the test is performed
    
    @field_validator('center_id')
    def validate_ids(cls, value):
        return validate_ids(value)
    @model_validator(mode='before')
    def convert_mongo_id(cls, values):
        return convert_mongo_id(values)
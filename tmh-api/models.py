from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List

# Constants for field validation
PHONE_REGEX = r'^\+?[1-9]\d{1,14}$'  # E.164 format

class Todo(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    description: str

class Users(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, strip_whitespace=True)
    email: EmailStr
    password: str = Field(..., min_length=8)
    hmo_ids: List[str] = Field(default_factory=list)  # List of HMO IDs associated with the user

    @field_validator('name')
    def validate_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError('Name must contain only alphabetic characters and spaces')
        return value

class HMO(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    address: str
    phone: str = Field(..., pattern=PHONE_REGEX)
    email: EmailStr
    website: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)

class Centers(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    address: str
    phone: str = Field(..., pattern=PHONE_REGEX)
    email: EmailStr
    website: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    hmo: List[str] = Field(default_factory=list)  # List of HMO IDs associated with the center

    @field_validator('hmo')
    def validate_hmo_ids(cls, value):
        if not all(isinstance(item, str) and len(item) == 24 for item in value):
            raise ValueError('Each HMO ID must be a valid 24-character MongoDB ObjectId string')
        return value

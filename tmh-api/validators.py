from typing import List


# Function to validate the name field
def validate_name(value: str) -> str:
    if not value.replace(" ", "").isalpha():
        raise ValueError('Name must contain only alphabetic characters and spaces')
    return value

# Function to validate HMO IDs
def validate_ids(value: List[str]) -> List[str]:
    if not all(isinstance(item, str) and len(item) == 24 for item in value):
        raise ValueError('Each ID must be a valid 24-character MongoDB ObjectId string')
    return value

# Function to convert MongoDB _id to id if it exists
def convert_mongo_id(values: dict) -> dict:
    if '_id' in values:
        values['id'] = str(values.pop('_id'))
    return values

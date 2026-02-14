from pydantic import BaseModel,Field, EmailStr

class UserCreate(BaseModel):
    name: str =  Field(min_length=3 , max_length=50)
    email : EmailStr


class UserUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=50)

class UserResponse(BaseModel):
    id : int
    name : str
    email = EmailStr
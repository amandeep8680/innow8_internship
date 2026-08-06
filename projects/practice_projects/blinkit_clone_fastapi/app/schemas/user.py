from pydantic import BaseModel, EmailStr
from datetime import datetime


# Data coming from client

class UserCreate(BaseModel):
    ''' This schema is used to create the  user.'''

    name: str
    email: EmailStr
    password: str


# Data sent back to client
class UserResponse(BaseModel):
    ''' This schema is the response when admin is created.'''
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True



class UserUpdate(BaseModel):
    ''' Schema used to update the user's data'''
    name: str
    updated_at: datetime


class UpdatedUserResponse(BaseModel):
    ''' This schema is the response when admin is updated , 
    right now it is only name .'''
    id: int
    name: str
    email: EmailStr
    is_active: bool
    updated_at : datetime

    class Config:
        from_attributes = True



class UserDeleteResponse(BaseModel):
    ''' Schema to delete the user'''
    id : int
    name : str
    message : str

    class Config:
           from_attributes = True
   
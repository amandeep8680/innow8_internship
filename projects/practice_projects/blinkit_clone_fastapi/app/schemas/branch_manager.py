from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from .branch import BranchResponse
# Data coming from client

class BranchManagerCreate(BaseModel):
    ''' This schema is used to create the branch manager.'''

    name: str
    unique_id : str
    email: EmailStr
    password: str


# Data sent back to client
class BranchManagerResponse(BaseModel):
    ''' Response schema of Branch Manager.'''
    unique_id : str
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at : datetime

    branch : Optional[BranchResponse] = None

    class Config:
        from_attributes = True



class BranchManagerUpdate(BaseModel):
    ''' Schema used to update the branch manager  data'''
    name: str
    updated_at: datetime

class UpdatedBranchManagerResponse(BaseModel):
    ''' Response schema when admin is updated , 
    right now it is only name .'''
    unique_id : str
    name: str
    email: EmailStr
    is_active: bool
    updated_at : datetime

    class Config:
        from_attributes = True



class BranchManagerDeleteResponse(BaseModel):
    ''' Schema to delete the branch manager'''
    unique_id : str
    name : str
    message : str

    class Config:
           from_attributes = True
   
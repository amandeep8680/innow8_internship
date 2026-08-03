from pydantic import BaseModel, EmailStr
from datetime import datetime


class BranchManagerCreate(BaseModel):
    ''' This schema is used to create the  branch_manager's id  by the super admin'''
    name: str
    email: EmailStr
    password: str


class BranchManagerResponse(BaseModel):
    ''' This schema is the response when admin created the _manager.'''

    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
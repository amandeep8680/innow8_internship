from pydantic import BaseModel
from datetime import datetime


class BranchCreate(BaseModel):
    ''' This schema is used to create the  branch by the super admin'''
    name: str
    address: str
    city: str
    pincode: str
    manager_id: int


class BranchResponse(BaseModel):
    ''' This schema is the response when admin created the branch.'''
    id: int
    name: str
    address: str
    city: str
    pincode: str
    manager_id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
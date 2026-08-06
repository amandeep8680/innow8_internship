from pydantic import BaseModel
from datetime import datetime



class BranchCreate(BaseModel):
    ''' This schema is used to create the  branch by the super admin'''
    name: str
    branch_unique_id : str
    address: str
    city: str
    pincode: str
    manager_unique_id: int


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




class BranchUpdate(BaseModel):
    ''' This schema is used to update the  branch by the super admin'''
    name: str
    address: str
    city: str
    pincode: str


class BranchManagerUpdate(BaseModel):
    ''' This schema is used to update the branch manager in the branch'''
    manager_id : int


class BranchManagerUpdateResponse(BaseModel):
    ''' This Response for updated the branch manager in the branch'''
    branch_unique_id : int
    name : str
    manager_id : int

class BranchDeleteResponse(BaseModel):
    branch_unique_id :  str
    name : str
    msg : str

    class config:
        from_attributes = True



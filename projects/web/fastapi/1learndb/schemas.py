from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class ShowBlog(BaseModel):
    title :str
    body:str
    class config():
        orm_mode=True


class UserCreate(BaseModel):
    name :str
    email:str
    password : str
    


class ShowUser(BaseModel):
    id : int
    name: str
    email : str
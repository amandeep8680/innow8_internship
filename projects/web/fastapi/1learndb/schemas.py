from pydantic import BaseModel
from typing import List


class BaseBlog(BaseModel):
    title:str
    body:str

 
class Blog(BaseBlog):
     class config():
          orm_mode = True



class UserCreate(BaseModel):
    name :str
    email:str
    password : str
    


class ShowUser(BaseModel):
 
    name: str
    email : str
    blog :  List[Blog] = []
    class config():
            orm_mode=True



class ShowBlog(BaseModel):
    title :str
    body:str
    creator :ShowUser
    class config():
        orm_mode=True
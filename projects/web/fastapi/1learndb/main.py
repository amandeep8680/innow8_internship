from fastapi import FastAPI , Depends ,  HTTPException , status
from typing import List
from . import models
from . import schemas
from .database import engine , SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog/",
    status_code=status.HTTP_201_CREATED )
def create(request: schemas.Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title , body = request.body , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog/",response_model = List[schemas.ShowBlog])
def get_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if blogs is None:
        raise HTTPException(status_code=404,detail="Blog Not Found")
    return blogs


@app.get("/blog/{id}/",response_model = List[schemas.ShowBlog])
def get_blog(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
            raise HTTPException(status_code=404,detail= f"{id},Blog Not Found")
    return blog


## udating the blog]
# @app.put("/blog/{id}/",status_code=status.HTTP_201_CREATED)
# def update_blog(id:int , request : schemas.Blog, db : Session = Depends(get_db)):
#     blog = (
#           db.query(models.Blog).filter(models.Blog.id==id).first()
#      )
#     if blog is None: 
#           raise HTTPException(
#                status_code = status.HTTP_404_NOT_FOUND,
#                detail="Blog not found"
#           )
    
#     blog.title = request.title
#     blog.body = request.body

#     db.commit()
#     db.refresh(blog)
#     return blog


## updating in a second way 
@app.put("/blog/{id}/",status_code=status.HTTP_201_CREATED)
def update_blog(id:int , request : schemas.Blog, db : Session = Depends(get_db)):
    blog = ( 
          db.query(models.Blog).filter(models.Blog.id==id)
          
     )
    if blog is None: 
          raise HTTPException(
               status_code = status.HTTP_404_NOT_FOUND,
               detail="Blog not found"
          )
    blog.update(request)

    db.commit()
    db.refresh(blog)
    return blog



# Deleting in db
@app.delete("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if blog is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    db.delete(blog)
    db.commit()
  






pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

# users
@app.post("/users/",response_model=schemas.ShowUser)
def create_users(request : schemas.UserCreate ,db : Session=Depends(get_db)):
    hashedpassword = pwd_cxt.hash(request.password)
    new_users = models.User(name = request.name ,email = request.email , password = hashedpassword )
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users




## Getting Users
@app.get("/users/",response_model=List[schemas.ShowUser])
def get_users(db:Session=Depends(get_db)):
    users  = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    return users


@app.get("/users/{id}",response_model=schemas.ShowUser)
def get_user(id = int ,db:Session=Depends(get_db)):
    users  = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    return users







############################### login   ##############################################
class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        return pwd_cxt.verify(plain_password, hashed_password)
     

@app.post("/login")
def login(request:schemas.login , db : Session = Depends(get_db)):
    

    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
         raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail="User Not Found"
                )

    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    return user
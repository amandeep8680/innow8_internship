from fastapi import  APIRouter , Depends , HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate , UserResponse , UserUpdate ,  UpdatedUserResponse , UserDeleteResponse
from app.services.user_service import UserService
import app.exceptions.custom_exceptions as exc
import app.exceptions.http_exception as http_exc
router = APIRouter(
    prefix="/super-user",
    tags=["Users"]
)
# variable is decalre to use Userservice class
user_service = UserService()
DBSession = Annotated[Session ,Depends(get_db)]


@router.post("/create",response_model=UserResponse)
def create_super_admin(
    user : UserCreate,
    db : DBSession,
):
    try:
        return user_service.create_super_admin(db=db , user = user)

    except exc.SuperAdminAlreadyExistsException:
            http_exc.super_admin_already_exists
    


@router.get("/Get",response_model=UserResponse)
def get_admin(
     email : str,
     db : DBSession
    ):
    try :
         return user_service.get_admin(db=db , email= email)

    except exc.UserNotFoundException:
         http_exc.user_not_found
    

@router.patch("/update",response_model=UpdatedUserResponse)
def update_super_admin(
    user : UserUpdate,
    db : DBSession,
):
    try:
        return user_service.update_super_admin(db=db , user = user)

    except exc.UserNotFoundException:
             http_exc.user_not_found
    



@router.delete("/delete",response_model=UserDeleteResponse)
def delete_admin(
     email : str,
     db : DBSession
    ):
    try :
         return user_service.delete_admin(db=db , email= email)

    except exc.UserNotFoundException:
             http_exc.user_not_found

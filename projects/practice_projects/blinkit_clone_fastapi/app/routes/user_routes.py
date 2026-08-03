from fastapi import  APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate , UserResponse
from app.services.user_service import UserService
from app.exceptions.custom_exceptions import SuperAdminAlreadyExistsException
from app.exceptions.messages import SUPER_ADMIN_ALREADY_EXISTS

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

user_service = UserService()


@router.post("/create-super-admin",response_model=UserResponse)
def create_super_admin(
    user : UserCreate,
    db : Session = Depends(get_db)
):
    try:
        return user_service.create_super_admin(db=db , user = user)

    except SuperAdminAlreadyExistsException:
        raise HTTPException(
            status_code=400,
            detail=SUPER_ADMIN_ALREADY_EXISTS
        )




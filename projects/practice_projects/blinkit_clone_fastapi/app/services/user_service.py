from sqlalchemy.orm import Session
from app.models.user import User 
from app.schemas.user import UserCreate
from app.database.database import get_db
from app.utils.security import hash_password
from app.exceptions.messages import SUPER_ADMIN_ALREADY_EXISTS 
from app.exceptions.custom_exceptions import SuperAdminAlreadyExistsException


class UserService:

    def create_super_admin( self,db : Session , user : UserCreate):
        existing_admin  = db.query(User).first()

        if existing_admin:
            raise SuperAdminAlreadyExistsException


        new_admin = User(
            name=user.name,
            email = user.email,
            password_hash = hash_password(user.password)
            )

        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)

        return new_admin
from sqlalchemy.orm import Session
from app.models.user import BranchManager 
from app.schemas.user import UserCreate , UserUpdate 
from app.utils.security import hash_password
from app.exceptions.messages import SUPER_ADMIN_ALREADY_EXISTS 
import app.exceptions.custom_exceptions as exc


class BranchManagerServices:
    
    def create_branch_manager( self,db : Session , user : UserCreate):
        '''
            this is BranchManager which is  getting requet from {routes/branchmanager_routes.py},
            from try block,
        
            work is to create check the user then create if exist then raise exception ,
            otherwise create new admin and save in db,
        
            We use hash_password to store password securily
        '''
        existing_manager = (
            db.query(BranchManager)
            .filter(BranchManager.email == user.email)
            .first()
        )

        if existing_manager:
            raise exc.BranchManagerAlreadyExistsException


        new_manager = BranchManager(
            name=user.name,
            email = user.email,
            unique_id = user.unique_id,
            password_hash = hash_password(user.password)
            )

        db.add(new_manager)
        db.commit()
        db.refresh(new_manager)

        return new_manager



    def get_branch_manager(self, db :Session , email : str):
        ''' Service to get the user details'''
        existing_user = db.query(BranchManager).filter(BranchManager.email == email).first()
        if not existing_user:
            raise exc.UserNotFoundException()

        return existing_user


    def update_branch_Manager(self, db: Session , user : UserUpdate ):
        ''' service to update the user'''

        existing_admin = db.query(BranchManager).first()

        if not existing_admin:
            raise exc.UserNotFoundException

        existing_admin.name = user.name
        db.commit()
        db.refresh(existing_admin)

        return existing_admin

    def delete_branch_manager(self, db :Session , email : str):
            ''' Service to delete the user.'''
            existing_user = db.query(BranchManager).filter(BranchManager.email == email).first()
            if not existing_user:
                raise exc.UserNotFoundException()
            response = {
                "message": "User deleted successfully",
                "unique_id": existing_user.unique_id,
                "name": existing_user.name,
            }
            db.delete(existing_user)
            db.commit()
            
            return response
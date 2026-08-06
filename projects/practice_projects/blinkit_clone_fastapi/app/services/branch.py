from sqlalchemy.orm import Session
from app.models.user import Branches  , BranchManager
from app.schemas.branch import BranchCreate ,BranchUpdate , BranchManagerUpdate
from app.utils.security import hash_password
from app.exceptions.messages import SUPER_ADMIN_ALREADY_EXISTS 
import app.exceptions.custom_exceptions as exc


class BranchServices:
    
    def create_branch( self,db : Session , branch : BranchCreate):
        '''
            this is Branch which is  getting requet from {routes/branchmanager_routes.py},
            from try block,
        
            work is to create check the user then create if exist then raise exception ,
            otherwise create new admin and save in db,
        
            We use hash_password to store password securily
        '''
        existing_branch = (
            db.query(Branches).filter(Branches.branch_unique_id == branch.branch_unique_id)
            .first()
        )

        if existing_branch:
            raise exc.BranchAlreadyExistsException


        new_branch = Branches(
            name=branch.name,
            branch_unique_id = branch.branch_unique_id,
            address = branch.address,
            city = branch.city,
            pincode = branch.pincode,
            manager_id =branch.manager_unique_id,
            )

        db.add(new_branch)
        db.commit()
        db.refresh(new_branch)

        return new_branch


    def get_branches(self, db :Session):
        ''' Service to get the all branch details'''
        branches = db.query(Branches).all()
        if not branches:
            raise exc.BranchNotFoundException()

        return branches

    def get_branch(self, db :Session , branch_unique_id : str):
        ''' Service to get the branch details'''
        existing_branch = db.query(Branches).filter(Branches.branch_unique_id == branch_unique_id).first()
        if not existing_branch:
            raise exc.BranchNotFoundException()

        return existing_branch




    def update_branch(self, db: Session , branch_unique_id : str , branch : BranchUpdate):
        ''' service to update the branch'''

        existing_branch = db.query(Branches).filter(Branches.branch_unique_id == branch_unique_id).first()

        if not existing_branch:
            raise exc.BranchNotFoundException

        existing_branch.name = branch.name
        existing_branch.address = branch.address
        existing_branch.city = branch.city
        existing_branch.pincode = branch.pincode
        db.commit()
        db.refresh(existing_branch)

        return existing_branch



    def delete_branch(self, db: Session, branch_unique_id: str):

        existing_branch = (
            db.query(Branches).filter(Branches.branch_unique_id == branch_unique_id).first()
        )
        if not existing_branch:
            raise exc.BranchNotFoundException()

        response = {
            "branch_unique_id": existing_branch.branch_unique_id,          
            "name": existing_branch.name,
            "msg": "Branch deleted successfully"
        }

        db.delete(existing_branch)
        db.commit()
        return response


    def update_branch_manager(self, db: Session , branch_unique_id : str , branch : BranchManagerUpdate):

        existing_branch = (
                    db.query(Branches).filter(Branches.branch_unique_id == branch_unique_id).first()
                )
        if not existing_branch:
            raise exc.BranchNotFoundException()
        
        manager = (db.query(BranchManager).filter(BranchManager.id == branch.manager_id).first())
        
        if not manager:
            raise exc.BranchManagerNotFoundException()
        
        existing_branch.manager_id = branch.manager_id

        db.commit()
        db.refresh(existing_branch)
        
        return existing_branch
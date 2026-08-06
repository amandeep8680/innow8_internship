from fastapi import  APIRouter , Depends , HTTPException
from typing import Annotated , List
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.branch import BranchCreate , BranchResponse , BranchDeleteResponse ,BranchUpdate ,BranchManagerUpdate, BranchManagerUpdateResponse
from app.services.branch import BranchServices
import app.exceptions.custom_exceptions as exc
import app.exceptions.http_exception as http_exc

\
router = APIRouter(
    prefix="/branch",
    tags=["Branch"]
)
# variable is decalre to use Userservice class
branch_services = BranchServices()
DBSession = Annotated[Session ,Depends(get_db)]


@router.post("/create",response_model=BranchResponse)
def create_branch(
    branch : BranchCreate,
    db : DBSession,
):
    try:
        return branch_services.create_branch(db, branch )

    except exc.BranchAlreadyExistsException:
            http_exc.branch_already_exists
    


@router.get("/get/",response_model=BranchResponse)
def get_branch(
     branch_unique_id : str,
     db : DBSession
    ):
    try :
         return branch_services.get_branch(db=db , branch_unique_id= branch_unique_id)

    except exc.UserNotFoundException:
         http_exc.branch_not_found



@router.get("/getbranches/",response_model=List[BranchResponse])
def get_branches(db : DBSession):
    try :
         return branch_services.get_branches(db=db)
    except exc.BranchNotFoundException:
         http_exc.branch_not_found

    

@router.patch("/update/{branch_unique_id}",response_model=BranchResponse)
def update_branch(
    branch_unique_id : str,
    branch : BranchUpdate,
    db : DBSession,
):
    try:
        return branch_services.update_branch(db=db , branch_unique_id=branch_unique_id ,branch=branch)

    except exc.BranchNotFoundException:
            http_exc.branch_not_found
    


@router.delete("/delete", response_model=BranchDeleteResponse)
def delete(
    branch_unique_id: str,
    db: DBSession
):
    try:
        return branch_services.delete_branch(db=db,branch_unique_id=branch_unique_id
        )
    except exc.BranchNotFoundException:
            http_exc.branch_not_found 



@router.patch("/update-manager", response_model=BranchManagerUpdateResponse)
def  update_branch_manager(branch_unique_id : str, db:DBSession , branch : BranchManagerUpdate):
    try:
         return branch_services.update_branch_manager(db , branch_unique_id , branch)     
    except exc.BranchNotFoundException:
         http_exc.branch_not_found
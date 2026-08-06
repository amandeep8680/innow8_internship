from fastapi import  APIRouter , Depends , HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.branch_manager import BranchManagerCreate , BranchManagerResponse , BranchManagerUpdate ,  BranchManagerResponse , BranchManagerDeleteResponse
from app.services.branchmanager import BranchManagerServices
import app.exceptions.custom_exceptions as exc
import app.exceptions.http_exception as http_exc

router = APIRouter(
    prefix="/branch-manager",
    tags=["Branch Manager"]
)
# variable is decalre to use Userservice class
branch_manager_services = BranchManagerServices()
DBSession = Annotated[Session ,Depends(get_db)]


@router.post("/create",response_model=BranchManagerResponse)
def create_branch_manager(
    user : BranchManagerCreate,
    db : DBSession,
):
    try:
        return branch_manager_services.create_branch_manager(db=db , user = user)

    except exc.UserNotFoundException:
             http_exc.branch_manager_exists
    


@router.get("/get/",response_model=BranchManagerResponse)
def get_branch_manager(
     email : str,
     db : DBSession
    ):
    try :
         return branch_manager_services.get_branch_manager(db=db , email= email)

    except exc.UserNotFoundException:
             http_exc.user_not_found

    

@router.patch("/update",response_model=BranchManagerUpdate)
def update_branch_manager(
    user : BranchManagerUpdate,
    db : DBSession,
):
    try:
        return branch_manager_services.update_branch_Manager(db=db , user = user)

    except exc.UserNotFoundException:
             http_exc.user_not_found



@router.delete("/delete",response_model=BranchManagerDeleteResponse)
def branch_manager(
     email : str,
     db : DBSession
    ):
    try :
         return branch_manager_services.delete_branch_manager(db=db , email= email)

    except exc.UserNotFoundException:
             http_exc.user_not_found

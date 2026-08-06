from fastapi import HTTPException

import app.exceptions.messages as msg


def super_admin_already_exists():
    raise HTTPException(
        status_code=400,
        detail=msg.SUPER_ADMIN_ALREADY_EXISTS
    )


def user_not_found():
    raise HTTPException(
        status_code=404,
        detail=msg.USER_NOT_FOUND
    )



def branch_manager_exists():
    raise HTTPException(
        status_code=400,
        detail=msg.BRANCH_MANAGER_ALREADY_EXISTS
    )


def branch_already_exists():
    raise HTTPException(
        status_code=400,
        detail=msg.BRANCH_ALREADY_EXISTS
    )


def branch_not_found():
    raise HTTPException(
        status_code=404,
        detail = msg.BRANCH_NOT_FOUND
    )


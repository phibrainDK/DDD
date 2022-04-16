from fastapi import APIRouter, Body, Depends, status
from api.schemas import PaginationParams, UserApi, UserSchema, UserBodyIn
from business_logic.business_logic import get_filter_users, create_user_db
from business_logic.schemas import UserStatus, UsersOut
from typing import List, Optional

router = APIRouter()


@router.get("/users", status_code=status.HTTP_200_OK, response_model=UsersOut)
def get_users(
    pagination_params: PaginationParams = Depends(PaginationParams),
    user_in: UserSchema = Depends(),
):
    """
    🤔🤔👀👀😎😎
    Return the list of users filtered by UserSchema
    """
    name = getattr(user_in, "name")
    from_age: Optional[int] = getattr(user_in, "from_age")
    to_age: Optional[int] = getattr(user_in, "to_age")
    status_option: List[UserStatus] = getattr(user_in, "status_option")
    return get_filter_users(
        name=name,
        from_age=from_age,
        to_age=to_age,
        status_option=status_option,
        order=pagination_params.order,
        page=pagination_params.page,
        page_size=pagination_params.page_size,
    )


@router.post("/users", status_code=status.HTTP_200_OK, response_model=UserApi)
def create_user(user_in: UserBodyIn = Body(..., description="User fields to create")):
    """
    🤔🤔👀👀😎😎
    Create a given user
    """
    return create_user_db(cmd=user_in)

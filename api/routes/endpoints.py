from fastapi import APIRouter, Depends, status
from api.schemas import PaginationParams
from api.schemas import UserSchema
from business_logic.business_logic import get_filter_users
from business_logic.schemas import UserStatus, UsersOut
from typing import List, Optional

router = APIRouter()


@router.get("/users", status_code=status.HTTP_200_OK, response_model=UsersOut)
def get_users(
    pagination_params: PaginationParams = Depends(PaginationParams),
    user_in: UserSchema = Depends(),
):
    """
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

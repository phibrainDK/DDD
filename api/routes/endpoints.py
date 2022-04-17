from uuid import UUID
from fastapi import APIRouter, Body, Depends, status, Path
from api.schemas import (
    PaginationParams,
    UserApi,
    UserSchema,
    UserBodyIn,
    UserBodyUpdateIn,
    UserQueryParamsIn,
    UserUpdateIn,
)
from business_logic.business_logic import (
    get_filter_users,
    create_user_db,
    update_user_db,
)
from business_logic.schemas import UsersOut

router = APIRouter()

# TODO: Find a way to convert the @dataclass defined in dao.database.commands into
# the one defined in api.schemas -> cause FastAPI use Path, Query, Body, etc


@router.get("/users/", status_code=status.HTTP_200_OK, response_model=UsersOut)
def get_users(
    pagination_params: PaginationParams = Depends(PaginationParams),
    user_in: UserSchema = Depends(),
):
    """
    🤔🤔👀👀😎😎
    Return the list of users filtered by UserSchema
    """
    filter_users_cmd = UserQueryParamsIn()
    filter_users_cmd.name = getattr(user_in, "name")
    filter_users_cmd.from_age = getattr(user_in, "from_age")
    filter_users_cmd.to_age = getattr(user_in, "to_age")
    filter_users_cmd.status_option = getattr(user_in, "status_option")
    filter_users_cmd.order = pagination_params.order
    filter_users_cmd.page = pagination_params.page
    filter_users_cmd.page_size = pagination_params.page_size
    return get_filter_users(filter_users_cmd=filter_users_cmd)


@router.post("/users/", status_code=status.HTTP_200_OK, response_model=UserApi)
def create_user(
    user_body_in: UserBodyIn = Body(..., description="User fields to create"),
):
    """
    🤔🤔👀👀😎😎
    Create a given user
    """
    return create_user_db(create_user_cmd=user_body_in)


@router.patch(
    "/users/{user_id}/", status_code=status.HTTP_200_OK, response_model=UserApi
)
def update_user(
    user_update_in: UserBodyUpdateIn = Body(..., description="User fields to create"),
    user_id: UUID = Path(..., title="User ID", description="ID of the given user"),
):
    """
    🤔🤔👀👀😎😎
    Update a given user
    """
    update_user_cmd = UserUpdateIn(user_id, user_update_in)
    return update_user_db(update_user_cmd=update_user_cmd)

from dao.database.commands import (
    GetUsers,
    CreateUser,
    EditUser,
)
from dao.database.controllers import (
    get_users_from_db,
    create_user_from_db,
    update_user_from_db,
)
from business_logic.schemas import (
    UsersOut,
    User,
)


def get_filter_users(filter_users_cmd: GetUsers) -> UsersOut:
    return get_users_from_db(cmd=filter_users_cmd)


def create_user_db(create_user_cmd: CreateUser) -> User:
    return create_user_from_db(cmd=create_user_cmd)


def update_user_db(update_user_cmd: EditUser) -> User:
    return update_user_from_db(cmd=update_user_cmd)

from dao.database.controllers import get_users_from_db
from business_logic.schemas import UserStatus, OrderStatus, UsersOut
from typing import List, Optional


def get_filter_users(
    status_option: List[UserStatus],
    order: OrderStatus,
    page: int,
    page_size: int,
    name: Optional[str],
    from_age: Optional[int],
    to_age: Optional[int],
) -> UsersOut:
    resp = get_users_from_db(
        name=name,
        status_option=status_option,
        from_age=from_age,
        to_age=to_age,
        order=order,
        page=page,
        page_size=page_size,
    )
    return resp

from business_logic.schemas import UserStatus, User
from typing import Optional, List
from pydantic.dataclasses import dataclass
from pydantic import PositiveInt
from fastapi import Query
from business_logic.schemas import OrderStatus

UserStatusApi = UserStatus
UserApi = User
OrderStatus = OrderStatus


class PaginationParams:
    def __init__(
        self,
        order: OrderStatus = OrderStatus.ASCENDING,
        page: PositiveInt = 1,
        page_size: PositiveInt = 10,
    ):
        self.page = page
        self.page_size = page_size
        self.order = order


@dataclass
class UserSchema:
    name: Optional[str] = Query(
        None,
        description=("name to filter, it is not necesary to be complete "),
        example="Einstein Flores, Helard Gomez",
    )
    from_age: Optional[int] = Query(
        None, description="age from which it will be filtered", example=10
    )
    to_age: Optional[int] = Query(
        None, description="age to which it will be filtered", example=30
    )
    status_option: Optional[List[UserStatus]] = Query(
        [],
        description=("The user status. You can request multiple status"),
        example=["active", "inactive"],
    )

from pydantic import Field
from dataclasses import dataclass
from typing import Optional, List
from uuid import UUID
from dao.database.options import OrderOption, Status


@dataclass
class Pagination:
    order: OrderOption = Field(..., description="order status")
    page: int = Field(..., description="The number of page")
    page_size: int = Field(..., description="Size of each page")


@dataclass
class CreateUser:
    full_name: str = Field(..., description="Full name of the given user")
    age: int = Field(..., description="Age of the given User")


@dataclass
class EditUser:
    id: Optional[UUID] = Field(None, description="ID of the given user")
    full_name: Optional[str] = Field(None, description="Full name to update")
    age: str = Field(None, description="Age to be updated")


@dataclass
class EditStatusUser:
    id: Optional[UUID] = Field(None, description="ID of the given user")
    status: Status = Field(..., description="The transition status to be updated")


@dataclass
class GetUsers(Pagination):
    name: Optional[str] = Field(
        None,
        description="name to filter, it is not necesary to be complete",
    )
    from_age: Optional[int] = Field(
        None,
        description="age from which it will be filtered",
    )
    to_age: Optional[int] = Field(
        None,
        description="age to which it will be filtered",
    )
    status_option: Optional[List[Status]] = Field(
        None,
        description="The user status as multioption",
    )

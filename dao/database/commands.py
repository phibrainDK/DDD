from pydantic import Field
from dataclasses import dataclass
from typing import Optional, List
from uuid import UUID
from dao.database.options import OrderOption, Status


@dataclass
class Pagination:
    order: OrderOption = Field(..., description="Order status")
    page: int = Field(..., description="The number of page")
    page_size: int = Field(..., description="Size of each page")


@dataclass
class CreateUser:
    full_name: str = Field(..., description="Full name of the given user")
    age: int = Field(..., description="Age of the given User")


@dataclass
class UpdateUserSchema:
    full_name: Optional[str] = Field(None, description="Full name to update")
    age: Optional[str] = Field(None, description="Age to be updated")
    status: Status = Field(None, description="The transition status to be updated")


@dataclass
class EditUser:
    id: Optional[UUID] = Field(None, description="ID of the given user")
    full_name: Optional[str] = Field(None, description="Full name to update")
    age: Optional[str] = Field(None, description="Age to be updated")


@dataclass
class EditStatusUser:
    id: Optional[UUID] = Field(None, description="ID of the given user")
    status: Status = Field(..., description="The transition status to be updated")


@dataclass
class UpdateUser:
    edit_user: EditUser = Field(..., description="Edit user schema")
    edit_status_user: Optional[EditStatusUser] = Field(
        None, description="Edit status schema",
    )

    def __init__(self, id: UUID, cmd: UpdateUserSchema):
        new_edit_user = EditUser()
        new_edit_user.id = id
        new_edit_user.full_name = cmd.full_name
        new_edit_user.age = cmd.age
        self.edit_user = new_edit_user
        self.edit_status_user = None
        if cmd.status:
            new_edit_status_user = EditStatusUser()
            new_edit_status_user.id = id
            new_edit_status_user.status = cmd.status
            self.edit_status_user = new_edit_status_user


@dataclass
class GetUsers(Pagination):
    name: Optional[str] = Field(
        None,
        description="Name to filter, it is not necesary to be complete",
    )
    from_age: Optional[int] = Field(
        None,
        description="Age from which it will be filtered",
    )
    to_age: Optional[int] = Field(
        None,
        description="Age to which it will be filtered",
    )
    status_option: Optional[List[Status]] = Field(
        None,
        description="The user status as multioption",
    )

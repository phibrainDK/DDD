from pydantic import BaseModel as _BaseModel
from pydantic import PositiveInt
from dao.database.models import Status, OrderStatus
from uuid import UUID
from typing import List, Iterable, Tuple
from django.db.models import QuerySet
from django.core import paginator


UserStatus = Status
OrderStatus = OrderStatus


class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, orm_objects: Iterable):
        """
        🤔🤔👀👀😎😎
        Converts each of the ORM Django objects from the iterable into their respective
        Pydantic schema (FastAPI -> Pydantic)
        """
        return [cls.from_orm(orm_object) for orm_object in orm_objects]


def paginate_orms(
    orm_objects: QuerySet, page: int, page_size: int
) -> Tuple[paginator.Page, paginator.Paginator]:
    """
    🤔🤔👀👀😎😎
    Paginates an iterable of ORM Django objects constraining the maximum page number
    to the last one available (check paginator documentation for more information)
    """
    paginator_func = paginator.Paginator(orm_objects, page_size)
    results_page = paginator_func.page(min(page, paginator_func.num_pages))
    return results_page, paginator_func


class User(BaseModel):
    id: UUID
    full_name: str
    age: int
    status: UserStatus

    class Config:
        orm_mode = True


class UsersOut(BaseModel):
    count: int = 0
    page: int = 1
    page_size: PositiveInt = 1
    num_pages: PositiveInt = 1
    users: List[User]

    @classmethod
    def from_orms(
        cls,
        users: QuerySet,
        page: int = 1,
        page_size: int = 10,
    ):
        """
        Creates the Pydantic schema from an iterable of (Django) ORM objects
        """
        users_page, paginator = paginate_orms(
            orm_objects=users,
            page=page,
            page_size=page_size,
        )
        return cls(
            users=User.from_orms(users_page),
            count=paginator.count,
            num_pages=paginator.num_pages,
            page=page,
            page_size=page_size,
        )

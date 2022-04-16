from dataclasses import dataclass
from django.db import models
import uuid
from typing import Optional

from business_logic.exceptions import InvalidEditStatus
from pydantic import Field


class OrderStatus(models.TextChoices):
    ASCENDING = "ascending"
    DESCENDING = "descending"


class Status(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"


@dataclass
class CreatePerson:
    full_name: str = Field(..., description="Full name of the given user")
    age: int = Field(..., description="Age of the given person")


@dataclass
class EditPerson:
    id: Optional[uuid.UUID] = Field(None, description="ID of the given user")
    full_name: Optional[str] = Field(None, description="Full name to update")
    age: str = Field(None, description="Age to be updated")


class EditStatusPerson:
    id: uuid.UUID
    status: Status


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    full_name = models.CharField(
        default="",
        max_length=100,
    )

    age = models.IntegerField(default=0)

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def custom_create(self, cmd: CreatePerson):
        self.full_name = cmd.full_name
        self.age = cmd.age

    def handle_person(self, cmd: EditPerson) -> None:
        if self.status == Status.INACTIVE:
            raise InvalidEditStatus
        self.full_name = cmd.full_name
        self.age = cmd.age

    def handle_status(self, cmd: EditStatusPerson) -> None:
        if self.status == cmd.status:
            raise InvalidEditStatus
        self.status = cmd.status

    class Meta:
        db_table = "table_person"
        app_label = "DDD"

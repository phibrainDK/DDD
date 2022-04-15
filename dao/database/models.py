from django.db import models
import uuid
from typing import Optional
from business_logic.exceptions import InvalidEditStatus


class OrderStatus(models.TextChoices):
    ASCENDING = "ascending"
    DESCENDING = "descending"


class Status(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"


class CreatePerson:
    full_name: str
    age: str


class EditPerson:
    id: uuid.UUID
    full_name: Optional[str]
    age: str


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

    def __init__(self, cmd: CreatePerson) -> None:
        self.full_name = cmd.full_name
        self.status = Status.ACTIVE
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

from django.db import models
import uuid

from business_logic.exceptions import InvalidEditStatus
from dao.database.commands import (
    CreateUser,
    EditUser,
    EditStatusUser,
)
from dao.database.options import Status


class User(models.Model):
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

    def custom_create(self, cmd: CreateUser):
        self.full_name = cmd.full_name
        self.age = cmd.age

    def handle_user(self, cmd: EditUser) -> None:
        if self.status == Status.INACTIVE:
            raise InvalidEditStatus
        self.full_name = cmd.full_name
        self.age = cmd.age

    def handle_status(self, cmd: EditStatusUser) -> None:
        if self.status == cmd.status:
            raise InvalidEditStatus
        self.status = cmd.status

    class Meta:
        db_table = "table_User"
        app_label = "DDD"

from dao.database.commands import GetUsers, CreateUser, UpdateUser
from business_logic.constants import LIMIT_SIMILARITY
from business_logic.schemas import UsersOut, User
from dao.database import models
from django.contrib.postgres.search import TrigramSimilarity
from dao.database.options import OrderOption


def get_users_from_db(cmd: GetUsers) -> UsersOut:
    users = models.User.objects.all()
    if cmd.status_option:
        users = users.filter(status__in=cmd.status_option)
    if cmd.name:
        users = users.annotate(
            similarity=TrigramSimilarity("full_name", cmd.name)
        ).filter(similarity__gt=LIMIT_SIMILARITY)
    if cmd.from_age:
        users = users.filter(age__gt=cmd.from_age)
    if cmd.to_age:
        users = users.filter(age__lt=cmd.to_age)
    users = users.order_by("age" if cmd.order == OrderOption.ASCENDING else "-age")
    return UsersOut.from_orms(users, cmd.page, cmd.page_size)


def create_user_from_db(cmd: CreateUser) -> User:
    current_user = models.User()
    current_user.custom_create(cmd)
    current_user.save()
    return User.from_orm(current_user)


def update_user_from_db(cmd: UpdateUser) -> User:
    current_user = models.User.objects.get(id=cmd.edit_user.id)
    update_fields = []
    if cmd.edit_status_user:
        current_user.handle_status(cmd.edit_status_user)
        update_fields.append("status")
    update_fields.extend(current_user.handle_user(cmd.edit_user))
    current_user.save(update_fields=update_fields)
    return User.from_orm(current_user)

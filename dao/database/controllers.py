from business_logic.constants import LIMIT_SIMILARITY
from business_logic.schemas import UserStatus, UsersOut
from typing import List, Optional
from dao.database import models
from django.contrib.postgres.search import TrigramSimilarity


def get_users_from_db(
    status_option: List[UserStatus],
    order: models.OrderStatus,
    page: int,
    page_size: int,
    name: Optional[str],
    from_age: Optional[int],
    to_age: Optional[int],
) -> UsersOut:
    users = models.Person.objects.all()
    if status_option:
        users = users.filter(status__in=status_option)
    if name:
        users = users.annotate(similarity=TrigramSimilarity("full_name", name)).filter(
            similarity__gt=LIMIT_SIMILARITY
        )
    if from_age:
        users = users.filter(age__gt=from_age)
    if to_age:
        users = users.filter(age__lt=to_age)
    users = users.order_by("age" if order == models.OrderStatus.ASCENDING else "-age")
    return UsersOut.from_orms(users, page, page_size)

from business_logic.constants import LIMIT_SIMILARITY
from business_logic.schemas import UserStatus, UsersOut
from typing import List, Optional
from dao.database import models
from django.contrib.postgres.search import TrigramSimilarity


def get_users(
    name: str,
    status_option: List[UserStatus],
    from_age: Optional[int],
    to_age: Optional[int],
    order: models.OrderStatus,
) -> UsersOut:
    users = models.Person.objects.all()
    if name:
        users = users.annotate(similarity=TrigramSimilarity("full_name", name)).filter(
            similarity__gt=LIMIT_SIMILARITY
        )
    if status_option:
        users = users.filter(status__in=status_option)
    if from_age:
        users = users.filter(age__gt=from_age)
    if to_age:
        users = users.filter(to_age__lt=to_age)
    users = users.order_by("age" if order == models.OrderStatus.ASCENDING else "-age")
    return UsersOut.from_orms(users)

from django.db import models


class OrderOption(models.TextChoices):
    ASCENDING = "ascending"
    DESCENDING = "descending"


class Status(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"

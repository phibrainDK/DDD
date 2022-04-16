from faker.providers import BaseProvider
import factory
from faker import Faker
from dao.database.models import User, Status
from typing import Any, Iterable
from factory.random import randgen


def random_choice(sequence: Iterable[Any]) -> Any:
    """
    Picks an element from the sequence at random
    Returns None if the sequence is empty
    """
    if not sequence:
        return None
    return randgen.choice(list(sequence))


class GeneralProvider(BaseProvider):
    def User_status(self):
        return random_choice(Status.values)


faker = Faker()
faker.add_provider(GeneralProvider)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # Foreign keys

    # Attributes
    status = factory.LazyAttribute(lambda _: faker.User_status())
    age = factory.LazyAttribute(lambda _: faker.random_number(digits=2))
    full_name = factory.LazyAttribute(lambda _: faker.name())

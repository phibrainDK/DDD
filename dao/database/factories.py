from faker.providers import BaseProvider
import factory
from faker import Faker
from dao.database.models import Person, Status


class GeneralProvider(BaseProvider):
    def person_status(self):
        return self.random_element([item for item in Status])


faker = Faker()
faker.add_provider(GeneralProvider)


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    # Foreign keys

    # Attributes
    status = factory.LazyAttribute(lambda _: faker.person_status())
    age = factory.LazyAttribute(lambda _: faker.random_number(digits=2))
    full_name = factory.LazyAttribute(lambda _: faker.name())

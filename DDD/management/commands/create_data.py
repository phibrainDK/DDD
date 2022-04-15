from django.core.management.base import BaseCommand
from dao.database.models import Person
from dao.database.factories import PersonFactory


class Command(BaseCommand):
    def create_data(self):
        PersonFactory.create_batch(100)

    def handle(self, *args, **kwargs):
        Person.objects.all().delete()
        self.create_data()

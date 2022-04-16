from django.core.management.base import BaseCommand
from dao.database.models import User
from dao.database.factories import UserFactory


class Command(BaseCommand):
    def create_data(self):
        UserFactory.create_batch(100)

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        self.create_data()

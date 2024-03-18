from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User

class Command(BaseCommand):
    help = 'Seeds the database'

    def handle(self, *args, **kwargs):
        Group.objects.create(name='admin')
        Group.objects.create(name='user')

        User.objects.create(email='test@test.com',username='octoadmin',first_name='octo', last_name='admin',phone='55555555555',password='string159357')
        self.stdout.write(self.style.SUCCESS('Database seeded!'))

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from search.models import OctoModel

class Command(BaseCommand):
    help = 'Seeds the database'

    def handle(self, *args, **kwargs):
        OctoModel.objects.create(Hostname='test.com',Ip='octoadmin')
        self.stdout.write(self.style.SUCCESS('Database seeded!'))

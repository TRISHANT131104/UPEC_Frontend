import json
from django.core.management.base import BaseCommand
from api.models import Client
from api.fake_data.client import client_data

class Command(BaseCommand):
    help = 'Add data to the Client table'

    def handle(self, *args, **options):
        for client_entry in client_data:
            Client.objects.create(**client_entry)

        self.stdout.write(self.style.SUCCESS('Successfully added client data'))

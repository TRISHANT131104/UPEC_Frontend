import json

from api.fake_data.client import client_data
from api.models import Client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Add data to the Client table"

    def handle(self, *args, **options):
        for client_entry in client_data:
            Client.objects.create(**client_entry)

        self.stdout.write(self.style.SUCCESS("Successfully added client data"))

import json

from api.fake_data.project import projects_data
from api.models import Project
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Add data to the projects table"

    def handle(self, *args, **options):
        for projects_entry in projects_data:
            # Replace None values with None
            for key, value in projects_entry.items():
                Project.objects.create(**projects_entry)

        self.stdout.write(self.style.SUCCESS("Successfully added projects data"))

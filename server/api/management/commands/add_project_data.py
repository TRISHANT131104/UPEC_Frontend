import json
from django.core.management.base import BaseCommand
from api.models import Project
from api.fake_data.project import projects_data

class Command(BaseCommand):
    help = 'Add data to the projects table'

    def handle(self, *args, **options):
        for projects_entry in projects_data:
            Project.objects.create(**projects_entry)

        self.stdout.write(self.style.SUCCESS('Successfully added projects data'))

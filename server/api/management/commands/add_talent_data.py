import json
from django.core.management.base import BaseCommand
from api.models import Talent
from api.fake_data.talent import talent_data
class Command(BaseCommand):
    help = 'Add data to the Talent table'

    def handle(self, *args, **options):
        


        for talent_entry in talent_data:
            Talent.objects.create(**talent_entry)

        self.stdout.write(self.style.SUCCESS('Successfully added talent data'))

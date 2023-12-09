import json
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId for generating unique IDs
from api.fake_data.project import projects_data

class Command(BaseCommand):
    help = 'Add data to the projects collection in MongoDB'

    def handle(self, *args, **options):
        # Connect to the local MongoDB server
        client = MongoClient('localhost', 27017)
        db = client["TRUMIO"]
        collection = db["api_project"]

        for project_entry in projects_data:
            project_entry["id"] = str(ObjectId())
            collection.insert_one(project_entry)

        self.stdout.write(self.style.SUCCESS('Successfully added projects data to MongoDB'))

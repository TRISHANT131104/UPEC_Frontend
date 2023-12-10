# yourapp/management/commands/generate_fake_data.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Generate fake data for User model"

    def handle(self, *args, **options):
        fake = Faker()

        # You can customize the number of fake users you want to generate
        num_users = 200

        for _ in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            first_name = fake.first_name()
            last_name = fake.last_name()

            User.objects.create_user(username=username, email=email, password=password)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {num_users} fake users")
        )

# yourapp/management/commands/generate_fake_data.py

from api.models import Project  # Update this import
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Generate fake data for YourModel model"

    def handle(self, *args, **options):
        fake = Faker()

        # You can customize the number of fake instances you want to generate
        num_instances = 10

        for _ in range(num_instances):
            title = fake.word()
            description = fake.text()
            start_date = fake.date_time_this_decade()
            end_date = fake.date_time_between_dates(datetime_start=start_date)
            bid_price = fake.pydecimal(left_digits=5, right_digits=2)
            status = fake.random_element(elements=("Open", "Closed", "In Progress"))
            learning_resources = fake.text()
            related_techstacks = fake.words(nb=3)
            created_at = fake.date_time_this_year()
            updated_at = fake.date_time_this_year()
            created_by = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
            )
            chat_group_id = (
                None  # You may need to modify this based on your requirements
            )

            your_model_instance = Project.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                bid_price=bid_price,
                status=status,
                Learning_resources=learning_resources,
                related_techstacks=related_techstacks,
                created_at=created_at,
                updated_at=updated_at,
                created_by=created_by,
                chat_group_id=chat_group_id,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully generated {num_instances} fake instances of YourModel"
            )
        )

import random
from faker import Faker
from django.core.management.base import BaseCommand
from transactions.models import User, Category, Transaction


class Command(BaseCommand):

    help = "generates transactions for testing"

    def handle(self, *args, **options):
        fake = Faker()

        # create categories
        categories = [
            "Salary",
            "Gambling",
            "Groceries",
            "Gas",
            "Baby",
            "Rent",
            "Entertainment",
            "Transport",
            "Health",
            "Subscriptions",
            "Eating out",
            "Cat",
            "Other",
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)

        # create users
        user = User.objects.get(username="nicolas")

        categories = Category.objects.all()
        types = ["Income", "Expense"]

        for i in range(20):
            Transaction.objects.create(
                user=user,
                category=random.choice(categories),
                amount=random.randint(1, 1000),
                date=fake.date_between(start_date="-2y", end_date="today"),
                description=fake.text(),
                type=random.choice(types),
            )

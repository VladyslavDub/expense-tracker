import random
from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand

from expenses.models import Expense

# category -> list of (title, description), plus the price range for the category
# Titles are kept short (under 20 characters) to fit the model's max_length.
SAMPLE_DATA = {
    "Groceries": {
        "items": [
            ("Bread", "Fresh bread from the bakery"),
            ("Milk", "Milk for the week"),
            ("Farmers market", "Cucumbers, tomatoes, herbs"),
            ("Supermarket", "Weekend grocery run"),
            ("Fruit", "Apples and bananas"),
        ],
        "price_range": (3, 90),
    },
    "Transport": {
        "items": [
            ("Monthly pass", "Monthly public transport pass"),
            ("Taxi", "Ride home"),
            ("Fuel", "Filling up the car"),
            ("Metro card", "Metro card top-up"),
        ],
        "price_range": (2, 150),
    },
    "Cafe": {
        "items": [
            ("Coffee", "Takeaway coffee"),
            ("Lunch", "Lunch with colleagues"),
            ("Pizza", "Dinner with friends"),
            ("Dessert", "Cake and tea"),
        ],
        "price_range": (5, 80),
    },
    "Entertainment": {
        "items": [
            ("Cinema", "Ticket for a new movie"),
            ("Subscription", "Monthly streaming plan"),
            ("Video game", "Bought a game online"),
            ("Concert", "Concert ticket"),
        ],
        "price_range": (10, 200),
    },
    "Health": {
        "items": [
            ("Pharmacy", "Vitamins and medicine"),
            ("Doctor", "Doctor consultation"),
            ("Gym", "Monthly gym membership"),
        ],
        "price_range": (8, 180),
    },
}


class Command(BaseCommand):
    help = "Create random test expenses for the last 90 days."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=40,
            help="How many expenses to create (default: 40).",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete ALL existing expenses and stop (nothing new is created).",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            deleted, _ = Expense.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Deleted {deleted} expenses."))
            return

        expenses = []
        for _ in range(options["count"]):
            category = random.choice(list(SAMPLE_DATA))
            data = SAMPLE_DATA[category]
            title, description = random.choice(data["items"])
            low, high = data["price_range"]

            amount = (Decimal(random.randint(low * 100, high * 100)) / 100).quantize(
                Decimal("0.01")
            )
            spent_on = date.today() - timedelta(days=random.randint(0, 90))

            expenses.append(
                Expense(
                    title=title,
                    description=description,
                    amount=amount,
                    category=category,
                    date_of_expenditure=spent_on,
                )
            )

        Expense.objects.bulk_create(expenses)
        self.stdout.write(
            self.style.SUCCESS(f"Created {len(expenses)} test expenses.")
        )
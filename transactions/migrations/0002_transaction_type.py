# Generated by Django 5.1.4 on 2024-12-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="type",
            field=models.CharField(
                choices=[("Income", "Income"), ("Expense", "Expense")],
                default="Expense",
                max_length=10,
            ),
        ),
    ]

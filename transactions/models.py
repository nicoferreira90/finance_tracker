from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name[:30]


class Transaction(models.Model):

    TRANSACTION_TYPE = (
        ("Income", "Income"),
        ("Expense", "Expense"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE, default="Expense")

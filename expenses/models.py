from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20)
    date_of_expenditure = models.DateField()

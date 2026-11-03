from django.db import models


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('Transport', 'Transport'),
        ('Rent', 'Rent'),
        ('Utilities', 'Utilities'),
        ('Salary', 'Salary'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    expense_date = models.DateField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
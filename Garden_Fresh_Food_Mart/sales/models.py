from django.db import models
from inventory.models import Product


class Sale(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sales'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    customer_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    sale_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.name} - UGX {self.amount}"
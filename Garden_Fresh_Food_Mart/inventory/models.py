from django.db import models
from django.db.models import Sum


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    buying_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def total_sales(self):
        return (
            self.sales.aggregate(
                total=Sum('amount')
            )['total']
            or 0
        )

    @property
    def total_investment(self):

        investment = self.investments.aggregate(
            total=Sum('amount')
        )['total']

        if investment:
            return investment

        return self.buying_price

    @property
    def remaining_recovery(self):

        remaining = (
            self.total_investment -
            self.total_sales
        )

        return max(remaining, 0)

    @property
    def profit(self):

        if self.total_sales > self.total_investment:

            return (
                self.total_sales -
                self.total_investment
            )

        return 0

    @property
    def recovery_percentage(self):

        if self.total_investment == 0:
            return 0

        percentage = (
            self.total_sales /
            self.total_investment
        ) * 100

        return round(percentage, 2)

    @property
    def stock_status(self):

        percentage = self.recovery_percentage

        if percentage < 70:
            return "IN_STOCK"

        elif percentage < 100:
            return "LOW_STOCK"

        elif percentage == 100:
            return "REORDER"

        return "PROFITABLE"

    def __str__(self):
        return self.name


class StockInvestment(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='investments'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    investment_date = models.DateField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return (
            f"{self.product.name} - "
            f"UGX {self.amount}"
        )
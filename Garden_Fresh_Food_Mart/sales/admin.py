from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'amount',
        'customer_name',
        'sale_date',
    )

    search_fields = (
        'product__name',
        'customer_name',
    )
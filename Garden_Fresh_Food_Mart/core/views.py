from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.db.models import Sum

from inventory.models import Product
from sales.models import Sale
from expenses.models import Expense


@login_required
def home(request):

    products_count = Product.objects.count()

    total_sales_today = (
        Sale.objects.aggregate(
            total=Sum('amount')
        )['total']
        or 0
    )

    sales_count = Sale.objects.count()

    expenses_count = Expense.objects.count()

    context = {
        'products_count': products_count,
        'total_sales_today': total_sales_today,
        'sales_count': sales_count,
        'expenses_count': expenses_count,
    }

    return render(
        request,
        'core/home.html',
        context
    )
from decimal import Decimal

from django.shortcuts import render
from django.db.models import Sum

from inventory.models import Product
from expenses.models import Expense

from django.contrib.auth.decorators import login_required

from accounts.decorators import (
    manager_required
)

@login_required
@manager_required
def dashboard(request):

    products = Product.objects.all()

    total_investment = Decimal("0.00")
    total_revenue = Decimal("0.00")
    total_profit = Decimal("0.00")

    for product in products:

        total_investment += product.total_investment

        total_revenue += product.total_sales

        total_profit += product.profit

    remaining_recovery = (
        total_investment - total_revenue
    )

    if remaining_recovery < 0:
        remaining_recovery = Decimal("0.00")

    total_expenses = (
        Expense.objects.aggregate(
            total=Sum('amount')
        )['total']
        or Decimal("0.00")
    )

    net_profit = (
        total_profit - total_expenses
    )

    context = {
        'product_count': products.count(),
        'total_investment': total_investment,
        'total_revenue': total_revenue,
        'remaining_recovery': remaining_recovery,
        'total_profit': total_profit,
        'expenses': total_expenses,
        'net_profit': net_profit,
        'products': products,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )
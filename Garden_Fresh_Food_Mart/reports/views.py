from decimal import Decimal

from django.shortcuts import render
from django.db.models import Sum

from sales.models import Sale
from expenses.models import Expense
from django.contrib.auth.decorators import login_required
from accounts.decorators import (
    manager_required
)


@login_required
@manager_required
def financial_report(request):

    sales = Sale.objects.none()

    revenue = Decimal("0.00")
    expenses = Decimal("0.00")
    net_profit = Decimal("0.00")

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:

        sales = Sale.objects.filter(
            sale_date__date__range=[
                start_date,
                end_date
            ]
        )

        revenue = (
            sales.aggregate(
                total=Sum('amount')
            )['total']
            or Decimal("0.00")
        )

        expenses = (
            Expense.objects.filter(
                expense_date__range=[
                    start_date,
                    end_date
                ]
            ).aggregate(
                total=Sum('amount')
            )['total']
            or Decimal("0.00")
        )

        net_profit = revenue - expenses

    top_products = (
        sales.values('product__name')
        .annotate(
            total_sales=Sum('amount')
        )
        .order_by('-total_sales')
    )

    context = {
        'sales': sales,
        'revenue': revenue,
        'expenses': expenses,
        'net_profit': net_profit,
        'top_products': top_products,
    }

    return render(
        request,
        'reports/financial_report.html',
        context
    )
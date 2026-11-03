from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ExpenseForm
from .models import Expense


def expense_list(request):

    expenses = Expense.objects.order_by(
        '-expense_date'
    )

    total_expenses = sum(
        expense.amount
        for expense in expenses
    )

    context = {
        'expenses': expenses,
        'total_expenses': total_expenses
    }

    return render(
        request,
        'expenses/expense_list.html',
        context
    )


def add_expense(request):

    form = ExpenseForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Expense saved successfully."
        )

        return redirect(
            'expense_list'
        )

    return render(
        request,
        'expenses/add_expense.html',
        {'form': form}
    )
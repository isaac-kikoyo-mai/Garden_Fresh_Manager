from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = [
            'title',
            'category',
            'amount',
            'expense_date',
            'notes'
        ]

        widgets = {
            'expense_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
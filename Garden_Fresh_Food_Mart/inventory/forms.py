from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class RestockForm(forms.Form):

    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        label="Additional Investment"
    )
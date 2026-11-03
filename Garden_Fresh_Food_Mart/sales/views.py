from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SaleForm
from .models import Sale
from django.contrib.auth.decorators import login_required


@login_required
def sale_list(request):

    sales = Sale.objects.order_by(
        '-sale_date'
    )

    return render(
        request,
        'sales/sale_list.html',
        {'sales': sales}
    )

@login_required
def create_sale(request):

    form = SaleForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Sale recorded successfully."
        )

        return redirect(
            'sale_list'
        )

    return render(
        request,
        'sales/create_sale.html',
        {'form': form}
    )
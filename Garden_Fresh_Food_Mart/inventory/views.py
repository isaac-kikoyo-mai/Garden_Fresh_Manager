from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, RestockForm
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        'inventory/product_list.html',
        {'products': products}
    )

@login_required
def add_product(request):

    form = ProductForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(
        request,
        'inventory/add_product.html',
        {'form': form}
    )

@login_required
def restock_product(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    form = RestockForm(
        request.POST or None
    )

    if form.is_valid():

        additional_amount = form.cleaned_data[
            'amount'
        ]

        product.buying_price += additional_amount

        product.save()

        messages.success(
            request,
            f"{product.name} restocked successfully."
        )

        return redirect(
            'product_list'
        )

    return render(
        request,
        'inventory/restock_product.html',
        {
            'product': product,
            'form': form
        }
    )
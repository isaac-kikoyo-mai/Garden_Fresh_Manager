from django.urls import path
from . import views

urlpatterns = [

    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    path(
        'products/add/',
        views.add_product,
        name='add_product'
    ),
    path(
        'products/<int:pk>/restock/',
        views.restock_product,
        name='restock_product'
    ),
]
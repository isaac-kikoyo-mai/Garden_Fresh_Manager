from django.urls import path
from . import views

urlpatterns = [

    path(
        'sales/',
        views.sale_list,
        name='sale_list'
    ),

    path(
        'sales/add/',
        views.create_sale,
        name='create_sale'
    ),
]
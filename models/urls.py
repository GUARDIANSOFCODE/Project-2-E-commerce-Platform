from django.urls import path
from .views import product_view

urlpatterns = [
    path('products/', product_view.product_list, name='product_list'),
]

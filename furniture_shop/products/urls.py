from django.urls import path, include
from .views import IndexView, ProductsView


app_name = 'products'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='product_list'),
]
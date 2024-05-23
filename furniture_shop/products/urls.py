from django.urls import path, include
from .views import index, product_list


app_name = 'products'


urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
]
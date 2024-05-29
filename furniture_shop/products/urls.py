from django.urls import path, include
from .views import IndexView, ProductsView, ProductDetailView


app_name = 'products'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='product_list'),
    path('products/<str:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]
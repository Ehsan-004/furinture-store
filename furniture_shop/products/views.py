from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

app_name = 'products'


class IndexView(View):
    http_method_names = ['get', 'post']

    def get(self, request: any) -> HttpResponse:
        return render(request, 'index.html')


class ProductsView(View):
    http_method_names = ['get', 'post']

    def get(self, request: any) -> HttpResponse:
        return render(request, 'product.html')


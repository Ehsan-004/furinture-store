from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Product, Image, Comment, Category


app_name = 'products'


class IndexView(View):
    http_method_names = ['get', 'post']


    def get(self, request: any) -> HttpResponse:
        products = Product.objects.all()[:6]
        indexed_products = Product.objects.all().filter(firs_page=True)
        product_details = []
        indexed_product_details = []
        # === === === === === === === === === === === === === === === === === ===
        # 6 products in the index page
        for product in products:
            images = Image.objects.all().filter(product__name=product.name)
            product_details.append({
                'name': product.name,
                'price': product.price,
                'image': images[0],
            })
        # === === === === === === === === === === === === === === === === === ===
        # 4 products which are indexed in the index page
        for product in indexed_products:
            image = Image.objects.all().filter(product__name=product.name)
            indexed_product_details.append({
                'name': product.name,
                'price': product.price,
                'image': image[0],
                'description': product.description,
            })
        # === === === === === === === === === === === === === === === === === ===
        context = {
            'product_details': product_details,
            'indexed_products': indexed_product_details,
        }
        return render(request, 'index.html', context)


class ProductsView(View):
    http_method_names = ['get', 'post']

    def get(self, request: any) -> HttpResponse:
        products = Product.objects.all()
        product_details = []
        for product in products:
            images = Image.objects.all().filter(product__name=product.name)
            product_details.append({
                'name': product.name,
                'price': product.price,
                'image': images[0],
            })

        context = {'product_details': product_details}
        return render(request, 'product.html', context)

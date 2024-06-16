from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Product, Image, Comment, Category
from random import shuffle


app_name = 'products'


class IndexView(View):
    http_method_names = ['get', 'post']

    def get(self, request: any) -> HttpResponse:
        products = Product.objects.all()[:6]
        indexed_products = Product.objects.filter(firs_page=True)
        product_details = []
        indexed_product_details = []
        # === === === === === === === === === === === === === === === === === ===
        # 6 products in the index page
        for product in products:
            images = Image.objects.filter(product__name=product.name)
            product_details.append({
                'name': product.name,
                'price': product.price,
                'image': images[0],
                'product_id': str(product.id),
            })
        shuffle(product_details)
        # === === === === === === === === === === === === === === === === === ===
        # 4 products which are indexed in the index page
        for product in indexed_products:
            image = Image.objects.filter(product__name=product.name)
            indexed_product_details.append({
                'name': product.name,
                'price': product.price,
                'image': image[0],
                'description': product.description,
                'product_id': str(product.id),
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
            images = Image.objects.filter(product__name=product.name)
            product_details.append({
                'name': product.name,
                'price': product.price,
                'image': images[0],
                'product_id': str(product.id),
            })
        context = {'product_details': product_details}
        return render(request, 'product.html', context)


class ProductDetailView(View):
    http_method_names = ['get', 'post']

    def get(self, request: any, product_id: str) -> HttpResponse:
        pid = int(product_id)
        product = Product.objects.get(pk=pid)
        images = Image.objects.filter(product__name=product.name)
        comments = Comment.objects.filter(product__name=product.name)
        comment_details = []
        for comment in comments:
            comment_details.append({
                'author': comment.author.user_profile.username,
                'content': comment.content,
                'rate': str(comment.rating)
            })

        context = {
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'special_property': product.special_property,
            'category': product.category,
            'images': images,
            'comments': comments,
            }

        return render(request, 'single.html', context)

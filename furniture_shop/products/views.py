from django.shortcuts import render

app_name = 'products'

def index(request):
    return render(request, 'index.html')


def product_list(request):
    return render(request, 'product.html')

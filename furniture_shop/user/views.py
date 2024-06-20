from django.db import IntegrityError
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from products.views import IndexView
from django.contrib.auth.models import User
from .models import Customer
from products.models import Product, Basket, BoughtItem



class LoginView(View):
    http_method_names = ['get', 'post']
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user:profile')
        return render(request, 'login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('user:profile')
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if False in [username, password]:
            return render(request, 'login.html', {'error': "enter username and password"})

        user = authenticate(username=username, password=password)

        if user in User.objects.filter(username=username):
            try:
                login(request, user)
                return redirect('products:index')
            except user.DoesNotExist:
                return render(request, 'login.html', {'error': "this username does not exist!"})
        return render(request, 'login.html', {'error': "wrong username or password!"})


class RegisterView(View):
    http_method_names = ['get', 'post']
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user:profile')
        return render(request, 'register.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('user:profile')
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        email = request.POST.get('email', False)
        if False in [username, password, email]:
            return render(request, 'register.html', {'error': "enter username and password!"})
        user = authenticate(username=username, password=password, email=email)
        if user in User.objects.filter(username=username):
            return render(request, 'register.html', {'error': "this username already exists!"})
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            costumer = Customer.objects.create(user_profile=user)
            costumer.save()
            login(request, user)
            return redirect('user:profile')
        except IntegrityError:
            return render(request, 'register.html', {'error': "this email already exists!"})


class UserProfileView(View):
    http_method_names = ['get',]
    template_name = 'profile.html'

    def get(self, request):
        basket = []
        bought_items = []
        user_basket = Basket.objects.filter(user_id=request.user.id)
        user_bought_items = BoughtItem.objects.filter(user_id=request.user.id)
        profile_picture = Customer.objects.get(user_profile_id=request.user.id).profile_picture
        for basket_item in user_basket:
            basket.append({
                'product_id': basket_item.id,
                'name': basket_item.name,
                'price': basket_item.price,
            })

        for bought_item in user_bought_items:
            bought_items.append({
                'product_id': bought_item.id,
                'name': bought_item.name,
                'price': bought_item.price,
            })
        context = {
            'basket': basket,
            'bought_items': bought_items,
            'profile_picture': profile_picture.url,
        }

        return render(request, self.template_name, context)


class UserProfileEdit(View):
    http_method_names = ['get', 'post']
    template_name = 'edit_profile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('user:login')
        customer = Customer.objects.get(user_profile_id=request.user.id)
        profile_pic = customer.profile_picture.url
        return render(request, self.template_name, {'profile_pic': profile_pic})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('user:login')
        user = request.user
        customer = Customer.objects.get(user_profile_id=request.user.id)

        new_first_name = request.POST.get('new_first_name', False)
        new_last_name = request.POST.get('new_last_name', False)
        new_email = request.POST.get('new_email', False)
        new_profile = request.FILES.get('new_profile_picture', False)

        if new_profile:
            customer.profile_picture = new_profile
            customer.save()
        if new_first_name:
            user.first_name = new_first_name
            user.save()
        if new_last_name:
            user.last_name = new_last_name
            user.save()
        if new_email:
            user.email = new_email
            user.save()
        return redirect('user:profile')

def logout_view(req):
    if not req.user.is_authenticated:
        return redirect('products:index')
    user = req.user
    logout(req)
    return redirect('products:index')

from django.urls import path, include
from .views import about, contact, services


app_name = 'about'


urlpatterns = [
    path('', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]

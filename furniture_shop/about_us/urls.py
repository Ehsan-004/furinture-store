from django.urls import path, include
from .views import AboutUs, Contact, Services


app_name = 'about'


urlpatterns = [
    path('', AboutUs.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services.as_view(), name='services'),
]

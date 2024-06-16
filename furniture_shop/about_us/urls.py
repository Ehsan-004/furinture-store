from django.conf.urls.static import static
from django.urls import path, include
from .views import AboutUs, Contact, Services
from furniture_shop.settings import MEDIA_URL, MEDIA_ROOT



app_name = 'about'


urlpatterns = [
    path('', AboutUs.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services.as_view(), name='services'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

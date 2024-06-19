from django.urls import path
from .views import LoginView, RegisterView, UserProfileView, logout_view, UserProfileEdit
from django.conf.urls.static import static
from furniture_shop.settings import MEDIA_ROOT, MEDIA_URL

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', UserProfileEdit.as_view(), name='profile_edit'),
] + static(MEDIA_URL,document_root=MEDIA_ROOT)

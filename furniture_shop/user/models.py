# from products.models import Product
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures')

    def __str__(self):
        return self.user_profile.username

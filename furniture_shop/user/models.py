from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=Product, blank=True, null=True)

    def __str__(self):
        return self.user.username +  " basket"


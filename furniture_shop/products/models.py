from django.db import models
from user.models import Customer
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    special_property = models.TextField()
    firs_page = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=Product)


class Comment(models.Model):
    rate = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    ]
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True, blank=True)
    author  = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    rating = models.CharField(choices=rate, default=0, max_length=5)


    def __str__(self):
        return self.content


class Image(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    # each product has images and each image has one product
    image = models.ImageField(upload_to='files/')


    def __str__(self):
        return self.image.url

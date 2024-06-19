from django.db import models
from user.models import Customer
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    special_property = models.TextField()
    firs_page = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=Product)

    class Meta:
        db_table = 'basket'
        verbose_name = 'basket'
        verbose_name_plural = 'basket'


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

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.content


class BoughtItem(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bought_item'
        verbose_name = 'bought_item'
        verbose_name_plural = 'bought_items'

    def __str__(self):
        return self.user.user_profile.username + " bought items"


class Image(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    # each product has images and each image has one product
    image = models.ImageField(upload_to='product_pictures/')

    class Meta:
        db_table = 'image'
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.image.url

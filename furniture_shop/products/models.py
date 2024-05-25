from django.db import models
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = QuillField()
    price = models.IntegerField()
    special_property = QuillField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    # each product has comments and each comments has one product
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Image(models.Model):
    # each product has images and each image has one product
    image = models.ImageField(upload_to='files/')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

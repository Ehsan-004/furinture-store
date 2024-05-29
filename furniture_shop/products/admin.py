from django.contrib import admin
from .models import Product, Category, Comment, Image
# from .models import Product, Category, Comment, Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'content')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Image, ImageAdmin)

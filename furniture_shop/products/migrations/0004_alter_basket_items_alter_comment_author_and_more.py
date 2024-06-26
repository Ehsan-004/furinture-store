# Generated by Django 5.0.2 on 2024-05-26 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment_author_alter_comment_product_and_more'),
        ('user', '0002_customer_delete_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(to='products.product'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]

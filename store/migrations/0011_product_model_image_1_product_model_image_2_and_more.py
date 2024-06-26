# Generated by Django 5.0.4 on 2024-04-29 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model_image_1',
            field=models.ImageField(default=None, upload_to='', verbose_name='uploads/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='model_image_2',
            field=models.ImageField(default=None, upload_to='', verbose_name='uploads/products'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 4, 29, 18, 54, 12, 585603)),
        ),
    ]

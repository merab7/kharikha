# Generated by Django 5.0.4 on 2024-07-01 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_alter_cuponcode_date_creted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuponcode',
            name='date_creted',
        ),
        migrations.AddField(
            model_name='cuponcode',
            name='date_created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='cuponcode',
            name='code',
            field=models.CharField(max_length=7, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='cuponcode',
            name='sale_percentage',
            field=models.IntegerField(default=0, verbose_name='sale percentage'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=150000, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fullname',
            field=models.CharField(max_length=300, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='order',
            name='per_id',
            field=models.CharField(max_length=200, null=True, verbose_name='personal ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False, verbose_name='shipped'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='shipped date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_paid_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total paid amount'),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='size',
            field=models.CharField(default='', max_length=100, verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='add_information',
            field=models.TextField(null=True, verbose_name='additional information'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=200, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=200, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='email',
            field=models.CharField(max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='fullname',
            field=models.CharField(max_length=300, verbose_name='fullname'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='per_id',
            field=models.CharField(max_length=200, null=True, verbose_name='personal ID'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=200, verbose_name='zipcode'),
        ),
    ]

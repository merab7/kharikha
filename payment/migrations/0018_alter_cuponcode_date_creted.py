# Generated by Django 5.0.4 on 2024-06-30 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0017_remove_cuponcode_date_cuponcode_date_creted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuponcode',
            name='date_creted',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now),
        ),
    ]
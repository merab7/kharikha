# Generated by Django 5.0.4 on 2024-04-27 17:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('store', '0004_alter_order_order_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Profile',
        ),
    ]
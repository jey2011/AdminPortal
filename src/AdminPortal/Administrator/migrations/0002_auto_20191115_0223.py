# Generated by Django 2.2.3 on 2019-11-15 02:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Administrator', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Administrator',
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-01 14:50

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]

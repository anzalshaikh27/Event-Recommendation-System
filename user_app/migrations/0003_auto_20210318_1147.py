# Generated by Django 3.0.7 on 2021-03-18 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_usersearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='time_details',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 11, 47, 40, 684610)),
        ),
    ]
# Generated by Django 3.0.7 on 2021-05-26 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0016_auto_20210526_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='time_details',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 10, 34, 48, 649362)),
        ),
    ]

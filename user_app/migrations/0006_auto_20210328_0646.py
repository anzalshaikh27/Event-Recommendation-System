# Generated by Django 3.0.7 on 2021-03-28 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20210328_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='time_details',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 6, 46, 29, 812988)),
        ),
    ]
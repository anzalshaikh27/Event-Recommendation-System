# Generated by Django 3.1.2 on 2021-05-27 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0024_auto_20210526_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_user_log',
            name='timedetails',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 27, 20, 1, 6, 933318)),
        ),
    ]
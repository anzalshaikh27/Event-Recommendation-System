# Generated by Django 3.0.7 on 2021-03-28 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0009_auto_20210318_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_user_log',
            name='timedetails',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 4, 39, 14, 793651)),
        ),
    ]

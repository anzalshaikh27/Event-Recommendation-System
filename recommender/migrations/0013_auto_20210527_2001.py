# Generated by Django 3.1.2 on 2021-05-27 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0012_auto_20210526_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyrecommendedevents',
            name='latest_update',
            field=models.DateField(default=datetime.date(2021, 5, 27)),
        ),
    ]
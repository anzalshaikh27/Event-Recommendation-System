# Generated by Django 3.0.7 on 2021-03-05 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0006_auto_20210305_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyrecommendedevents',
            name='latest_update',
            field=models.DateField(default=datetime.date(2021, 3, 5)),
        ),
    ]
# Generated by Django 3.0.7 on 2021-05-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_events_model_e_regis_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_category_model',
            name='image_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
# Generated by Django 3.0.7 on 2021-05-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_category_model_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='events_model',
            name='e_image_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
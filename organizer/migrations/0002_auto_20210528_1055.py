# Generated by Django 3.0.7 on 2021-05-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='ecat',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='edesc',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='eguest',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='eloc',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='ename',
            field=models.CharField(max_length=200),
        ),
    ]
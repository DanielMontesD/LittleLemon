# Generated by Django 4.2.17 on 2025-01-07 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]

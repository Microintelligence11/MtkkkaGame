# Generated by Django 3.1.1 on 2020-10-04 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_great_india_points_kalyan_day_points_moon_night_points'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Great_India_Chart',
        ),
        migrations.DeleteModel(
            name='Great_India_points',
        ),
        migrations.DeleteModel(
            name='jay_Bharat_Chart',
        ),
        migrations.DeleteModel(
            name='jay_Bharat_points',
        ),
        migrations.DeleteModel(
            name='Kalyan_day_Chart',
        ),
        migrations.DeleteModel(
            name='Kalyan_day_points',
        ),
        migrations.DeleteModel(
            name='Moon_night_Chart',
        ),
        migrations.DeleteModel(
            name='Moon_night_points',
        ),
    ]

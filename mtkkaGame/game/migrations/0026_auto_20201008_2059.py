# Generated by Django 3.1.1 on 2020-10-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0025_auto_20201008_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kalyan_day_chart',
            name='Date',
            field=models.CharField(default='*', max_length=100),
        ),
    ]
# Generated by Django 3.1.1 on 2020-10-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greatindia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kalyanday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Moonnight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(max_length=100)),
            ],
        ),
    ]

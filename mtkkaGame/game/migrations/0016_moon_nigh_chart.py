# Generated by Django 3.1.1 on 2020-10-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_jay_bharat_chart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moon_nigh_chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.CharField(max_length=100)),
                ('tus', models.CharField(max_length=100)),
                ('wed', models.CharField(max_length=100)),
                ('thu', models.CharField(max_length=100)),
                ('fri', models.CharField(max_length=100)),
                ('sat', models.CharField(max_length=100)),
                ('sun', models.CharField(max_length=100)),
            ],
        ),
    ]
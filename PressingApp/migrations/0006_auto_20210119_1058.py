# Generated by Django 3.0.8 on 2021-01-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PressingApp', '0005_auto_20210118_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestataire_service',
            name='service',
        ),
        migrations.AddField(
            model_name='prestataire_service',
            name='service',
            field=models.ManyToManyField(to='PressingApp.Service'),
        ),
    ]

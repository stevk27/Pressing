# Generated by Django 3.0.8 on 2021-01-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PressingApp', '0009_auto_20210114_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='prestataire',
            field=models.ManyToManyField(through='PressingApp.Ligne_commande', to='PressingApp.Prestataire_Service'),
        ),
    ]
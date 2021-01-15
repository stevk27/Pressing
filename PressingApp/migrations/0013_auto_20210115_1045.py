# Generated by Django 3.0.8 on 2021-01-15 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PressingApp', '0012_remove_commande_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='prestataire',
        ),
        migrations.RemoveField(
            model_name='ligne_commande',
            name='prestataire',
        ),
        migrations.AddField(
            model_name='commande',
            name='services',
            field=models.ManyToManyField(through='PressingApp.Ligne_commande', to='PressingApp.Service'),
        ),
        migrations.AddField(
            model_name='commande',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='ligne_commande',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PressingApp.Service'),
        ),
    ]
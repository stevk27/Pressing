# Generated by Django 3.1 on 2021-01-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PressingApp', '0007_auto_20210119_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adressepretataire',
            name='latitude_presta',
            field=models.DecimalField(decimal_places=15, max_digits=199),
        ),
        migrations.AlterField(
            model_name='adressepretataire',
            name='longitude_presta',
            field=models.DecimalField(decimal_places=15, max_digits=199),
        ),
    ]

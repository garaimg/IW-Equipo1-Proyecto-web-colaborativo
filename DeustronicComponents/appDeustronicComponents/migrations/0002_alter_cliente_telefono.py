# Generated by Django 5.0.4 on 2024-04-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustronicComponents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustronicComponents', '0004_remove_pedidoproducto_precio_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]

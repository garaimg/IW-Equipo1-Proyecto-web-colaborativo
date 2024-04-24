# Generated by Django 5.0.4 on 2024-04-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustronicComponents', '0002_alter_cliente_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='precio_total',
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustronicComponents', '0007_alter_cliente_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(default='en proceso', max_length=20),
        ),
    ]

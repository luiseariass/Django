# Generated by Django 3.0.5 on 2020-04-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.IntegerField(max_length=12),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Pedidos', '0009_auto_20200423_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ['nombre']},
        ),
        migrations.AddField(
            model_name='pedidos',
            name='articulos',
            field=models.ManyToManyField(to='Gestion_Pedidos.Articulos'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=60, verbose_name='La dirección'),
        ),
    ]

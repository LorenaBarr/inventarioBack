# Generated by Django 5.1.2 on 2024-10-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_bodega_remove_sale_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AlterField(
            model_name='inventario',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
    ]

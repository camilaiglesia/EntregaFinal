# Generated by Django 4.1.7 on 2023-03-16 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_compra_precio_alter_venta_precio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producto',
            new_name='Bien',
        ),
    ]

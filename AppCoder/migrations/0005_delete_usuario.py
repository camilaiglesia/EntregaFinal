# Generated by Django 4.1.7 on 2023-03-25 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_rename_producto_bien'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
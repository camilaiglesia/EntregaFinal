# Generated by Django 4.1.7 on 2023-03-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
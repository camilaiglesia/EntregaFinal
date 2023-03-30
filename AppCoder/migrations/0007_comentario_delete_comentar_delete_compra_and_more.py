# Generated by Django 4.1.7 on 2023-03-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_comentar_profile_delete_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Comentar',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/'),
        ),
    ]

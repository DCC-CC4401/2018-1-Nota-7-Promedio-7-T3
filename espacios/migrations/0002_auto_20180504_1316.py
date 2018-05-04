# Generated by Django 2.0.4 on 2018-05-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacios',
            name='estado_espacio',
            field=models.IntegerField(choices=[(1, 'Disponible'), (2, 'Prestado'), (3, 'Reparación')], default=1),
        ),
        migrations.AlterField(
            model_name='espacios',
            name='foto_espacio',
            field=models.ImageField(upload_to='uploads/fotos_espacios'),
        ),
    ]
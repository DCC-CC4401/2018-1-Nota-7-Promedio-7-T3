# Generated by Django 2.0.5 on 2018-06-13 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20180504_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='id_articulo',
        ),
    ]

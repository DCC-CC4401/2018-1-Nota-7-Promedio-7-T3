# Generated by Django 2.0.5 on 2018-06-14 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0003_auto_20180513_1702'),
        ('reservas', '0002_auto_20180614_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrestamoArticulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_reserva', models.IntegerField(choices=[(1, 'Vigente'), (2, 'Caducado'), (3, 'Perdido')], default=1)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Perfil')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.ReservaArticulo')),
            ],
        ),
        migrations.CreateModel(
            name='PrestamoEspacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_reserva', models.IntegerField(choices=[(1, 'Vigente'), (2, 'Caducado'), (3, 'Perdido')], default=1)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Perfil')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.ReservaEspacio')),
            ],
        ),
    ]
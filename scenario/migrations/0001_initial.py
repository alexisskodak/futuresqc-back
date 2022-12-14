# Generated by Django 4.0.4 on 2022-05-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escenariosview',
            fields=[
                ('idescenario', models.AutoField(db_column='IdEscenario', primary_key=True, serialize=False)),
                ('nombreescenario', models.CharField(blank=True, db_column='nombreEscenario', max_length=50, null=True)),
                ('idusuario', models.CharField(blank=True, db_column='idUsuario', max_length=24, null=True)),
                ('idestacion', models.CharField(blank=True, db_column='idEstacion', max_length=24, null=True)),
                ('idmaquina', models.CharField(blank=True, db_column='idMaquina', max_length=24, null=True)),
                ('idproducto', models.CharField(blank=True, db_column='idProducto', max_length=24, null=True)),
                ('idformato', models.CharField(blank=True, db_column='idFormato', max_length=24, null=True)),
                ('tipo', models.CharField(blank=True, max_length=2, null=True)),
                ('pausa', models.CharField(blank=True, max_length=2, null=True)),
                ('columnas', models.CharField(blank=True, max_length=500, null=True)),
                ('nombrepantalla', models.CharField(blank=True, db_column='nombrePantalla', max_length=100, null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('statusfavorito', models.BooleanField(blank=True, db_column='statusFavorito', null=True)),
            ],
            options={
                'db_table': 'escenariosView',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('idescenario', models.AutoField(db_column='IdEscenario', primary_key=True, serialize=False)),
                ('nombreescenario', models.CharField(blank=True, db_column='nombreEscenario', max_length=50, null=True)),
                ('idusuario', models.CharField(blank=True, max_length=15, null=True)),
                ('idestacion', models.CharField(blank=True, max_length=15, null=True)),
                ('idmaquina', models.CharField(blank=True, max_length=15, null=True)),
                ('idproducto', models.CharField(blank=True, max_length=15, null=True)),
                ('idformato', models.CharField(blank=True, max_length=15, null=True)),
                ('tipo', models.CharField(blank=True, max_length=2, null=True)),
                ('pausa', models.CharField(blank=True, max_length=2, null=True)),
                ('columnas', models.CharField(blank=True, max_length=500, null=True)),
                ('nombrepantalla', models.CharField(blank=True, db_column='nombrePantalla', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Escenarios',
                'managed': False,
            },
        ),
    ]

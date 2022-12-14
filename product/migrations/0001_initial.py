# Generated by Django 4.0.4 on 2022-05-18 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones',
            fields=[
                ('accionid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre1', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'acciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bitacoras',
            fields=[
                ('bitacoraid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre1', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bitacoras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('caracteristicaid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
                ('tipoanalisis', models.CharField(blank=True, db_column='Tipoanalisis', max_length=1, null=True)),
            ],
            options={
                'db_table': 'caracteristicas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Claves',
            fields=[
                ('claveid', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'claves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estaciones',
            fields=[
                ('estacionid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'estaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exu',
            fields=[
                ('usuarioid', models.OneToOneField(db_column='usuarioid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.user')),
            ],
            options={
                'db_table': 'exu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('favoritoid', models.AutoField(db_column='FavoritoID', primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Favoritos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formatos',
            fields=[
                ('formatoid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'formatos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GageAdmin',
            fields=[
                ('clave', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('nserie', models.CharField(blank=True, max_length=20, null=True)),
                ('gagestaid', models.CharField(blank=True, db_column='GageStaId', max_length=15, null=True)),
                ('frecuencia', models.IntegerField(blank=True, db_column='Frecuencia', null=True)),
                ('ultimacalibracion', models.CharField(blank=True, db_column='UltimaCalibracion', max_length=8, null=True)),
                ('proximacalibracion', models.CharField(blank=True, db_column='ProximaCalibracion', max_length=8, null=True)),
                ('documento', models.CharField(blank=True, db_column='Documento', max_length=50, null=True)),
                ('interfase', models.CharField(blank=True, db_column='Interfase', max_length=50, null=True)),
                ('imagen', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'gage_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GageDepartamentos',
            fields=[
                ('gagedepaid', models.CharField(db_column='GageDepaId', max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'gage_departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GageEstatus',
            fields=[
                ('gagestaid', models.CharField(db_column='GageStaId', max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'gage_estatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GageFabricantes',
            fields=[
                ('gagefabid', models.CharField(db_column='GageFabId', max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'gage_fabricantes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GageTipos',
            fields=[
                ('gagetipoid', models.CharField(db_column='GageTipoId', max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'gage_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Headgraf',
            fields=[
                ('etiqueta', models.SmallIntegerField(db_column='Etiqueta', primary_key=True, serialize=False)),
                ('status', models.BooleanField(blank=True, db_column='Status', null=True)),
                ('posx', models.FloatField(blank=True, db_column='PosX', null=True)),
                ('posy', models.FloatField(blank=True, db_column='PosY', null=True)),
                ('alineacion', models.SmallIntegerField(blank=True, db_column='Alineacion', null=True)),
            ],
            options={
                'db_table': 'HeadGraf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_frm', models.CharField(db_column='Cve_frm', max_length=13)),
                ('es', models.CharField(blank=True, max_length=150, null=True)),
                ('en', models.CharField(blank=True, max_length=150, null=True)),
                ('pt', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'Idiomas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('instrumentoid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('parametros', models.CharField(blank=True, max_length=10, null=True)),
                ('terminado', models.CharField(blank=True, max_length=3, null=True)),
                ('tipo', models.CharField(blank=True, max_length=1, null=True)),
                ('numcols', models.SmallIntegerField(blank=True, db_column='NumCols', null=True)),
                ('validacon', models.CharField(blank=True, db_column='ValidaCon', max_length=50, null=True)),
                ('envia', models.CharField(blank=True, max_length=50, null=True)),
                ('posini', models.CharField(blank=True, db_column='PosIni', max_length=250, null=True)),
                ('posfin', models.CharField(blank=True, db_column='PosFin', max_length=250, null=True)),
                ('longitud', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instrumentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Limites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(db_column='Fecha')),
                ('lse', models.FloatField(blank=True, null=True)),
                ('lie', models.FloatField(blank=True, null=True)),
                ('lsn', models.FloatField(blank=True, null=True)),
                ('lmn', models.FloatField(blank=True, null=True)),
                ('lin', models.FloatField(blank=True, null=True)),
                ('lsr', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Limites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Maquinas',
            fields=[
                ('maquinaid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'maquinas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preferencias',
            fields=[
                ('usuarioid', models.OneToOneField(db_column='UsuarioID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.user')),
                ('limi', models.CharField(blank=True, db_column='Limi', max_length=2, null=True)),
                ('cols', models.TextField(blank=True, db_column='Cols', null=True)),
                ('cltm', models.SmallIntegerField(blank=True, db_column='ClTM', null=True)),
                ('coly', models.SmallIntegerField(blank=True, db_column='ColY', null=True)),
                ('inte', models.SmallIntegerField(blank=True, db_column='Inte', null=True)),
                ('sigm', models.FloatField(blank=True, db_column='Sigm', null=True)),
                ('tpar', models.CharField(blank=True, db_column='Tpar', max_length=1, null=True)),
                ('font', models.CharField(blank=True, db_column='Font', max_length=25, null=True)),
                ('ptos', models.SmallIntegerField(blank=True, db_column='Ptos', null=True)),
                ('negr', models.SmallIntegerField(blank=True, db_column='Negr', null=True)),
                ('ital', models.SmallIntegerField(blank=True, db_column='Ital', null=True)),
                ('pxgr', models.SmallIntegerField(blank=True, db_column='PxGR', null=True)),
                ('tics', models.SmallIntegerField(blank=True, db_column='Tics', null=True)),
                ('tesc', models.CharField(blank=True, db_column='TEsc', max_length=2, null=True)),
                ('pesc', models.CharField(blank=True, db_column='PEsc', max_length=6, null=True)),
                ('grid', models.CharField(blank=True, db_column='Grid', max_length=1, null=True)),
                ('idio', models.CharField(blank=True, db_column='Idio', max_length=2, null=True)),
                ('alrm', models.CharField(blank=True, db_column='Alrm', max_length=1, null=True)),
                ('bita', models.CharField(blank=True, db_column='Bita', max_length=1, null=True)),
                ('ccpk', models.CharField(blank=True, db_column='CCpk', max_length=1, null=True)),
                ('norm', models.CharField(blank=True, db_column='Norm', max_length=1, null=True)),
                ('corr', models.SmallIntegerField(blank=True, db_column='Corr', null=True)),
                ('xfec', models.SmallIntegerField(blank=True, db_column='xFec', null=True)),
                ('exac', models.SmallIntegerField(blank=True, db_column='Exac', null=True)),
                ('fijl', models.SmallIntegerField(blank=True, db_column='FijL', null=True)),
                ('colc', models.SmallIntegerField(blank=True, db_column='ColC', null=True)),
                ('ngru', models.SmallIntegerField(blank=True, db_column='Ngru', null=True)),
                ('tlot', models.FloatField(blank=True, db_column='Tlot', null=True)),
                ('nins', models.SmallIntegerField(blank=True, db_column='NIns', null=True)),
                ('naql', models.FloatField(blank=True, db_column='NAQL', null=True)),
                ('tlov', models.FloatField(blank=True, db_column='TloV', null=True)),
                ('ninv', models.SmallIntegerField(blank=True, db_column='NInV', null=True)),
                ('naqv', models.FloatField(blank=True, db_column='NAQV', null=True)),
                ('comentario', models.CharField(blank=True, max_length=70, null=True)),
                ('colo1', models.FloatField(blank=True, null=True)),
                ('colo2', models.FloatField(blank=True, null=True)),
                ('fontable', models.CharField(blank=True, db_column='Fontable', max_length=25, null=True)),
                ('ptostable', models.SmallIntegerField(blank=True, null=True)),
                ('negrtable', models.SmallIntegerField(blank=True, null=True)),
                ('italtable', models.SmallIntegerField(blank=True, null=True)),
                ('p_por', models.SmallIntegerField(blank=True, db_column='P_por', null=True)),
                ('mlims', models.CharField(blank=True, db_column='MLims', max_length=1, null=True)),
                ('clpr', models.CharField(blank=True, db_column='ClPr', max_length=50, null=True)),
                ('parte', models.CharField(blank=True, db_column='Parte', max_length=50, null=True)),
                ('cort', models.CharField(blank=True, db_column='Cort', max_length=50, null=True)),
                ('entr', models.CharField(blank=True, db_column='Entr', max_length=50, null=True)),
                ('most', models.CharField(blank=True, db_column='Most', max_length=50, null=True)),
                ('porc', models.CharField(blank=True, db_column='Porc', max_length=50, null=True)),
                ('obje', models.CharField(blank=True, db_column='Obje', max_length=50, null=True)),
                ('btndef', models.SmallIntegerField(blank=True, null=True)),
                ('btnparte', models.SmallIntegerField(blank=True, null=True)),
                ('cortecpk', models.IntegerField(blank=True, null=True)),
                ('metacppp', models.IntegerField(blank=True, db_column='Metacppp', null=True)),
                ('metacpk', models.FloatField(blank=True, db_column='MetaCpK', null=True)),
                ('metacp', models.FloatField(blank=True, db_column='MetaCp', null=True)),
                ('browserhtml', models.CharField(blank=True, db_column='Browserhtml', max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=1, null=True)),
                ('priograf', models.CharField(blank=True, db_column='PrioGraf', max_length=1, null=True)),
                ('celdacolorbackz1', models.FloatField(blank=True, db_column='CeldaColorBackZ1', null=True)),
                ('celdacolorbackz2', models.FloatField(blank=True, db_column='CeldaColorBackZ2', null=True)),
                ('celdacolorbackz3', models.FloatField(blank=True, db_column='CeldaColorBackZ3', null=True)),
                ('celdacolorbackfz1', models.FloatField(blank=True, db_column='CeldaColorBackFZ1', null=True)),
                ('celdacolorbackfz2', models.FloatField(blank=True, db_column='CeldaColorBackFZ2', null=True)),
                ('celdacolorbackfz3', models.FloatField(blank=True, db_column='CeldaColorBackFZ3', null=True)),
                ('celdacolorforez1', models.FloatField(blank=True, db_column='CeldaColorForeZ1', null=True)),
                ('celdacolorforez2', models.FloatField(blank=True, db_column='CeldaColorForeZ2', null=True)),
                ('celdacolorforez3', models.FloatField(blank=True, db_column='CeldaColorForeZ3', null=True)),
                ('hojacolorfondo', models.FloatField(blank=True, db_column='HojaColorFondo', null=True)),
                ('hojacolorletra', models.FloatField(blank=True, db_column='HojaColorLetra', null=True)),
                ('hojacolorrow', models.FloatField(blank=True, db_column='HojaColorRow', null=True)),
                ('hojacolorrowletra', models.FloatField(blank=True, db_column='HojaColorRowLetra', null=True)),
                ('hojacolorodd', models.FloatField(blank=True, db_column='HojaColorOdd', null=True)),
                ('hojaoddeven', models.CharField(blank=True, db_column='HojaOddEven', max_length=1, null=True)),
                ('celdatipo', models.CharField(blank=True, db_column='CeldaTipo', max_length=1, null=True)),
                ('regeditables', models.FloatField(blank=True, db_column='RegEditables', null=True)),
                ('periodoedit', models.CharField(blank=True, db_column='PeriodoEdit', max_length=4, null=True)),
                ('ventana', models.SmallIntegerField(blank=True, db_column='Ventana', null=True)),
                ('paretocir', models.SmallIntegerField(blank=True, db_column='ParetoCir', null=True)),
                ('regvisiblestables', models.SmallIntegerField(blank=True, db_column='RegVisiblestables', null=True)),
                ('periodovisible', models.CharField(blank=True, db_column='PeriodoVisible', max_length=4, null=True)),
                ('maxmin', models.SmallIntegerField(blank=True, db_column='MaxMin', null=True)),
                ('histoxr', models.SmallIntegerField(blank=True, db_column='HistoXR', null=True)),
                ('xr', models.SmallIntegerField(blank=True, db_column='XR', null=True)),
                ('lambda_field', models.SmallIntegerField(blank=True, db_column='Lambda', null=True)),
                ('colorcritica', models.BigIntegerField(blank=True, db_column='ColorCritica', null=True)),
                ('vercritica', models.CharField(blank=True, db_column='VerCritica', max_length=1, null=True)),
                ('altobit', models.FloatField(blank=True, db_column='AltoBit', null=True)),
                ('defecto', models.SmallIntegerField(blank=True, null=True)),
                ('costo', models.SmallIntegerField(blank=True, null=True)),
                ('periodos', models.SmallIntegerField(blank=True, db_column='Periodos', null=True)),
                ('acomodabox', models.CharField(blank=True, db_column='AcomodaBox', max_length=1, null=True)),
                ('mdatos', models.CharField(blank=True, max_length=1, null=True)),
                ('ndatos', models.SmallIntegerField(blank=True, db_column='Ndatos', null=True)),
                ('vercpk', models.SmallIntegerField(blank=True, db_column='VerCPK', null=True)),
                ('tmcf', models.SmallIntegerField(blank=True, db_column='TMCF', null=True)),
                ('desvstd', models.CharField(blank=True, max_length=1, null=True)),
                ('arcoiris', models.CharField(blank=True, max_length=1, null=True)),
                ('tamcolvar', models.BigIntegerField(blank=True, null=True)),
                ('tamcoldispo', models.BigIntegerField(blank=True, null=True)),
                ('tamcollibre', models.BigIntegerField(blank=True, null=True)),
                ('headcert', models.CharField(blank=True, db_column='headCert', max_length=1, null=True)),
                ('hideoutlim', models.CharField(blank=True, db_column='HideOutLim', max_length=1, null=True)),
                ('grafuni', models.CharField(blank=True, db_column='GrafUni', max_length=1, null=True)),
                ('vermultilim', models.CharField(blank=True, db_column='Vermultilim', max_length=1, null=True)),
                ('tipovista', models.CharField(blank=True, db_column='Tipovista', max_length=1, null=True)),
                ('multilim', models.CharField(blank=True, max_length=1, null=True)),
                ('showclave', models.BooleanField(blank=True, null=True)),
                ('areaverde', models.FloatField(blank=True, db_column='AreaVerde', null=True)),
                ('bajocurva', models.CharField(blank=True, db_column='BajoCurva', max_length=1, null=True)),
            ],
            options={
                'db_table': 'Preferencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('productoid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=50, null=True)),
                ('consolidado', models.BooleanField(blank=True, db_column='Consolidado', null=True)),
                ('imagen', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Systemlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
                ('usuarioid', models.CharField(blank=True, db_column='UsuarioID', max_length=15, null=True)),
                ('modulo', models.CharField(blank=True, db_column='Modulo', max_length=50, null=True)),
                ('accion', models.CharField(blank=True, db_column='Accion', max_length=20, null=True)),
                ('comentarios', models.TextField(blank=True, db_column='Comentarios', null=True)),
            ],
            options={
                'db_table': 'SystemLogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, db_column='Version', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Axb',
            fields=[
                ('bitacoraid', models.OneToOneField(db_column='bitacoraid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.bitacoras')),
            ],
            options={
                'db_table': 'axb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bxf',
            fields=[
                ('formatoid', models.OneToOneField(db_column='formatoid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.formatos')),
            ],
            options={
                'db_table': 'bxf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cxc',
            fields=[
                ('caracteristicaid', models.OneToOneField(db_column='caracteristicaid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.caracteristicas')),
            ],
            options={
                'db_table': 'cxc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cxf',
            fields=[
                ('formatoid', models.OneToOneField(db_column='formatoid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.formatos')),
                ('posicion', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cxf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cxp',
            fields=[
                ('productoid', models.OneToOneField(db_column='productoid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.productos')),
                ('tipoanalisis', models.CharField(blank=True, max_length=1, null=True)),
                ('uni_o_bi', models.CharField(blank=True, max_length=1, null=True)),
                ('unidad', models.CharField(blank=True, max_length=10, null=True)),
                ('lse', models.FloatField(blank=True, null=True)),
                ('lie', models.FloatField(blank=True, null=True)),
                ('lsn', models.FloatField(blank=True, null=True)),
                ('lmn', models.FloatField(blank=True, null=True)),
                ('lin', models.FloatField(blank=True, null=True)),
                ('lsr', models.FloatField(blank=True, null=True)),
                ('lsc', models.FloatField(blank=True, null=True)),
                ('lic', models.FloatField(blank=True, null=True)),
                ('subgrupo', models.IntegerField(blank=True, null=True)),
                ('decimales', models.SmallIntegerField(blank=True, null=True)),
                ('critica', models.CharField(blank=True, max_length=1, null=True)),
                ('costo', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('captura', models.CharField(blank=True, max_length=1, null=True)),
                ('formula', models.CharField(blank=True, max_length=50, null=True)),
                ('instrumento', models.CharField(blank=True, max_length=8, null=True)),
                ('puerto', models.CharField(blank=True, max_length=2, null=True)),
                ('movimiento', models.CharField(blank=True, max_length=1, null=True)),
                ('busqueda', models.CharField(blank=True, max_length=1, null=True)),
                ('avisolimite', models.CharField(blank=True, max_length=12, null=True)),
                ('avisotendencia', models.CharField(blank=True, max_length=12, null=True)),
                ('avisoadhesion', models.CharField(blank=True, max_length=12, null=True)),
                ('avisoproceso', models.CharField(blank=True, max_length=12, null=True)),
                ('imagen', models.CharField(blank=True, max_length=20, null=True)),
                ('obligasubgpo', models.BooleanField(blank=True, db_column='ObligaSubGpo', null=True)),
                ('db', models.CharField(blank=True, db_column='DB', max_length=10, null=True)),
                ('query', models.TextField(blank=True, db_column='Query', null=True)),
                ('formatofecha', models.CharField(blank=True, db_column='Formatofecha', max_length=24, null=True)),
                ('aviso4', models.CharField(blank=True, db_column='AVISO4', max_length=12, null=True)),
                ('aviso5', models.CharField(blank=True, db_column='AVISO5', max_length=12, null=True)),
                ('aviso6', models.CharField(blank=True, db_column='AVISO6', max_length=12, null=True)),
                ('aviso7', models.CharField(blank=True, db_column='AVISO7', max_length=12, null=True)),
                ('aviso8', models.CharField(blank=True, db_column='AVISO8', max_length=12, null=True)),
                ('aviso9', models.CharField(blank=True, db_column='AVISO9', max_length=12, null=True)),
                ('bitaut', models.BooleanField(blank=True, db_column='BITAUT', null=True)),
                ('enviauser', models.CharField(blank=True, db_column='EnviaUser', max_length=200, null=True)),
                ('monitoreo', models.BooleanField(blank=True, null=True)),
                ('enviaemail', models.CharField(blank=True, db_column='Enviaemail', max_length=200, null=True)),
                ('resultados', models.BooleanField(blank=True, db_column='Resultados', null=True)),
                ('nresultados', models.IntegerField(blank=True, db_column='NResultados', null=True)),
                ('periodoresultados', models.CharField(blank=True, db_column='PeriodoResultados', max_length=4, null=True)),
                ('gageadmin', models.CharField(blank=True, db_column='GageAdmin', max_length=10, null=True)),
                ('tipotituloemail', models.IntegerField(blank=True, db_column='TipoTituloEmail', null=True)),
                ('tituloemail', models.CharField(blank=True, db_column='TituloEmail', max_length=20, null=True)),
                ('detalleemail', models.BooleanField(blank=True, db_column='DetalleEmail', null=True)),
                ('ncapest', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cxp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fxp',
            fields=[
                ('productoid', models.OneToOneField(db_column='productoid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.productos')),
            ],
            options={
                'db_table': 'fxp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fxu',
            fields=[
                ('favoritoid', models.OneToOneField(db_column='FavoritoID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.favoritos')),
            ],
            options={
                'db_table': 'FXU',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mxe',
            fields=[
                ('estacionid', models.OneToOneField(db_column='estacionid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.estaciones')),
            ],
            options={
                'db_table': 'mxe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pxm',
            fields=[
                ('maquinaid', models.OneToOneField(db_column='maquinaid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.maquinas')),
                ('prodteorico', models.IntegerField(blank=True, db_column='prodTeorico', null=True)),
                ('prodreal', models.IntegerField(blank=True, db_column='prodReal', null=True)),
                ('uproduccion', models.CharField(blank=True, db_column='uProduccion', max_length=4, null=True)),
            ],
            options={
                'db_table': 'pxm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reglasweco',
            fields=[
                ('productoid', models.OneToOneField(db_column='ProductoID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.productos')),
                ('status1', models.SmallIntegerField(db_column='Status1')),
                ('regla1n', models.SmallIntegerField(blank=True, db_column='Regla1n', null=True)),
                ('regla1m', models.SmallIntegerField(blank=True, db_column='Regla1m', null=True)),
                ('status2', models.SmallIntegerField(db_column='Status2')),
                ('regla2n', models.SmallIntegerField(blank=True, db_column='Regla2n', null=True)),
                ('regla2m', models.SmallIntegerField(blank=True, db_column='Regla2m', null=True)),
                ('status3', models.SmallIntegerField(db_column='Status3')),
                ('regla3n', models.SmallIntegerField(blank=True, db_column='Regla3n', null=True)),
                ('regla3m', models.SmallIntegerField(blank=True, db_column='Regla3m', null=True)),
                ('status4', models.SmallIntegerField(db_column='Status4')),
                ('regla4n', models.SmallIntegerField(blank=True, db_column='Regla4n', null=True)),
                ('regla4m', models.SmallIntegerField(blank=True, db_column='Regla4m', null=True)),
                ('status5', models.SmallIntegerField(db_column='Status5')),
                ('regla5n', models.SmallIntegerField(blank=True, db_column='Regla5n', null=True)),
                ('regla5m', models.SmallIntegerField(blank=True, db_column='Regla5m', null=True)),
                ('status6', models.SmallIntegerField(db_column='Status6')),
                ('regla6n', models.SmallIntegerField(blank=True, db_column='Regla6n', null=True)),
                ('regla6m', models.SmallIntegerField(blank=True, db_column='Regla6m', null=True)),
                ('status7', models.SmallIntegerField(db_column='Status7')),
                ('regla7n', models.SmallIntegerField(blank=True, db_column='Regla7n', null=True)),
                ('regla7m', models.SmallIntegerField(blank=True, db_column='Regla7m', null=True)),
                ('status8', models.SmallIntegerField(db_column='Status8')),
                ('regla8n', models.SmallIntegerField(blank=True, db_column='Regla8n', null=True)),
                ('regla8m', models.SmallIntegerField(blank=True, db_column='Regla8m', null=True)),
            ],
            options={
                'db_table': 'ReglasWECO',
                'managed': False,
            },
        ),
    ]

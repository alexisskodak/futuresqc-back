# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fxu(models.Model):
    favoritoid = models.OneToOneField(
        "Favoritos", models.DO_NOTHING, db_column="FavoritoID", primary_key=True
    )
    usuarioid = models.ForeignKey("user.User", models.DO_NOTHING, db_column="usuarioid")

    class Meta:
        managed = False
        db_table = "FXU"
        unique_together = (("favoritoid", "usuarioid"),)


class Favoritos(models.Model):
    favoritoid = models.AutoField(db_column="FavoritoID", primary_key=True)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    estacionid = models.ForeignKey("Estaciones", models.DO_NOTHING, db_column="estacionid")
    maquinaid = models.ForeignKey("Maquinas", models.DO_NOTHING, db_column="maquinaid")
    productoid = models.ForeignKey("Productos", models.DO_NOTHING, db_column="productoid")
    formatoid = models.ForeignKey("Formatos", models.DO_NOTHING, db_column="formatoid")

    class Meta:
        managed = False
        db_table = "Favoritos"


class Headgraf(models.Model):
    etiqueta = models.SmallIntegerField(db_column="Etiqueta", primary_key=True)
    status = models.BooleanField(db_column="Status", blank=True, null=True)
    posx = models.FloatField(db_column="PosX", blank=True, null=True)
    posy = models.FloatField(db_column="PosY", blank=True, null=True)
    alineacion = models.SmallIntegerField(db_column="Alineacion", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "HeadGraf"


class Idiomas(models.Model):
    cve_frm = models.CharField(db_column="Cve_frm", max_length=13)
    es = models.CharField(max_length=150, blank=True, null=True)
    en = models.CharField(max_length=150, blank=True, null=True)
    pt = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Idiomas"


class Limites(models.Model):
    productoid = models.ForeignKey("Productos", models.DO_NOTHING, db_column="productoid")
    caracteristicaid = models.ForeignKey(
        "Caracteristicas", models.DO_NOTHING, db_column="caracteristicaid"
    )
    fecha = models.DateTimeField(db_column="Fecha")
    lse = models.FloatField(blank=True, null=True)
    lie = models.FloatField(blank=True, null=True)
    lsn = models.FloatField(blank=True, null=True)
    lmn = models.FloatField(blank=True, null=True)
    lin = models.FloatField(blank=True, null=True)
    lsr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Limites"


class Preferencias(models.Model):
    usuarioid = models.OneToOneField(
        "user.User", models.DO_NOTHING, db_column="UsuarioID", primary_key=True
    )
    limi = models.CharField(db_column="Limi", max_length=2, blank=True, null=True)
    cols = models.TextField(db_column="Cols", blank=True, null=True)
    cltm = models.SmallIntegerField(db_column="ClTM", blank=True, null=True)
    coly = models.SmallIntegerField(db_column="ColY", blank=True, null=True)
    inte = models.SmallIntegerField(db_column="Inte", blank=True, null=True)
    sigm = models.FloatField(db_column="Sigm", blank=True, null=True)
    tpar = models.CharField(db_column="Tpar", max_length=1, blank=True, null=True)
    font = models.CharField(db_column="Font", max_length=25, blank=True, null=True)
    ptos = models.SmallIntegerField(db_column="Ptos", blank=True, null=True)
    negr = models.SmallIntegerField(db_column="Negr", blank=True, null=True)
    ital = models.SmallIntegerField(db_column="Ital", blank=True, null=True)
    pxgr = models.SmallIntegerField(db_column="PxGR", blank=True, null=True)
    tics = models.SmallIntegerField(db_column="Tics", blank=True, null=True)
    tesc = models.CharField(db_column="TEsc", max_length=2, blank=True, null=True)
    pesc = models.CharField(db_column="PEsc", max_length=6, blank=True, null=True)
    grid = models.CharField(db_column="Grid", max_length=1, blank=True, null=True)
    idio = models.CharField(db_column="Idio", max_length=2, blank=True, null=True)
    alrm = models.CharField(db_column="Alrm", max_length=1, blank=True, null=True)
    bita = models.CharField(db_column="Bita", max_length=1, blank=True, null=True)
    ccpk = models.CharField(db_column="CCpk", max_length=1, blank=True, null=True)
    norm = models.CharField(db_column="Norm", max_length=1, blank=True, null=True)
    corr = models.SmallIntegerField(db_column="Corr", blank=True, null=True)
    xfec = models.SmallIntegerField(db_column="xFec", blank=True, null=True)
    exac = models.SmallIntegerField(db_column="Exac", blank=True, null=True)
    fijl = models.SmallIntegerField(db_column="FijL", blank=True, null=True)
    colc = models.SmallIntegerField(db_column="ColC", blank=True, null=True)
    ngru = models.SmallIntegerField(db_column="Ngru", blank=True, null=True)
    tlot = models.FloatField(db_column="Tlot", blank=True, null=True)
    nins = models.SmallIntegerField(db_column="NIns", blank=True, null=True)
    naql = models.FloatField(db_column="NAQL", blank=True, null=True)
    tlov = models.FloatField(db_column="TloV", blank=True, null=True)
    ninv = models.SmallIntegerField(db_column="NInV", blank=True, null=True)
    naqv = models.FloatField(db_column="NAQV", blank=True, null=True)
    comentario = models.CharField(max_length=70, blank=True, null=True)
    colo1 = models.FloatField(blank=True, null=True)
    colo2 = models.FloatField(blank=True, null=True)
    fontable = models.CharField(db_column="Fontable", max_length=25, blank=True, null=True)
    ptostable = models.SmallIntegerField(blank=True, null=True)
    negrtable = models.SmallIntegerField(blank=True, null=True)
    italtable = models.SmallIntegerField(blank=True, null=True)
    p_por = models.SmallIntegerField(db_column="P_por", blank=True, null=True)
    mlims = models.CharField(db_column="MLims", max_length=1, blank=True, null=True)
    clpr = models.CharField(db_column="ClPr", max_length=50, blank=True, null=True)
    parte = models.CharField(db_column="Parte", max_length=50, blank=True, null=True)
    cort = models.CharField(db_column="Cort", max_length=50, blank=True, null=True)
    entr = models.CharField(db_column="Entr", max_length=50, blank=True, null=True)
    most = models.CharField(db_column="Most", max_length=50, blank=True, null=True)
    porc = models.CharField(db_column="Porc", max_length=50, blank=True, null=True)
    obje = models.CharField(db_column="Obje", max_length=50, blank=True, null=True)
    btndef = models.SmallIntegerField(blank=True, null=True)
    btnparte = models.SmallIntegerField(blank=True, null=True)
    cortecpk = models.IntegerField(blank=True, null=True)
    metacppp = models.IntegerField(db_column="Metacppp", blank=True, null=True)
    metacpk = models.FloatField(db_column="MetaCpK", blank=True, null=True)
    metacp = models.FloatField(db_column="MetaCp", blank=True, null=True)
    browserhtml = models.CharField(
        db_column="Browserhtml", max_length=50, blank=True, null=True
    )
    descripcion = models.CharField(
        db_column="Descripcion", max_length=1, blank=True, null=True
    )
    priograf = models.CharField(db_column="PrioGraf", max_length=1, blank=True, null=True)
    celdacolorbackz1 = models.FloatField(db_column="CeldaColorBackZ1", blank=True, null=True)
    celdacolorbackz2 = models.FloatField(db_column="CeldaColorBackZ2", blank=True, null=True)
    celdacolorbackz3 = models.FloatField(db_column="CeldaColorBackZ3", blank=True, null=True)
    celdacolorbackfz1 = models.FloatField(db_column="CeldaColorBackFZ1", blank=True, null=True)
    celdacolorbackfz2 = models.FloatField(db_column="CeldaColorBackFZ2", blank=True, null=True)
    celdacolorbackfz3 = models.FloatField(db_column="CeldaColorBackFZ3", blank=True, null=True)
    celdacolorforez1 = models.FloatField(db_column="CeldaColorForeZ1", blank=True, null=True)
    celdacolorforez2 = models.FloatField(db_column="CeldaColorForeZ2", blank=True, null=True)
    celdacolorforez3 = models.FloatField(db_column="CeldaColorForeZ3", blank=True, null=True)
    hojacolorfondo = models.FloatField(db_column="HojaColorFondo", blank=True, null=True)
    hojacolorletra = models.FloatField(db_column="HojaColorLetra", blank=True, null=True)
    hojacolorrow = models.FloatField(db_column="HojaColorRow", blank=True, null=True)
    hojacolorrowletra = models.FloatField(db_column="HojaColorRowLetra", blank=True, null=True)
    hojacolorodd = models.FloatField(db_column="HojaColorOdd", blank=True, null=True)
    hojaoddeven = models.CharField(
        db_column="HojaOddEven", max_length=1, blank=True, null=True
    )
    celdatipo = models.CharField(db_column="CeldaTipo", max_length=1, blank=True, null=True)
    regeditables = models.FloatField(db_column="RegEditables", blank=True, null=True)
    periodoedit = models.CharField(
        db_column="PeriodoEdit", max_length=4, blank=True, null=True
    )
    ventana = models.SmallIntegerField(db_column="Ventana", blank=True, null=True)
    paretocir = models.SmallIntegerField(db_column="ParetoCir", blank=True, null=True)
    regvisiblestables = models.SmallIntegerField(
        db_column="RegVisiblestables", blank=True, null=True
    )
    periodovisible = models.CharField(
        db_column="PeriodoVisible", max_length=4, blank=True, null=True
    )
    maxmin = models.SmallIntegerField(db_column="MaxMin", blank=True, null=True)
    histoxr = models.SmallIntegerField(db_column="HistoXR", blank=True, null=True)
    xr = models.SmallIntegerField(db_column="XR", blank=True, null=True)
    lambda_field = models.SmallIntegerField(db_column="Lambda", blank=True, null=True)
    colorcritica = models.BigIntegerField(db_column="ColorCritica", blank=True, null=True)
    vercritica = models.CharField(db_column="VerCritica", max_length=1, blank=True, null=True)
    altobit = models.FloatField(db_column="AltoBit", blank=True, null=True)
    defecto = models.SmallIntegerField(blank=True, null=True)
    costo = models.SmallIntegerField(blank=True, null=True)
    periodos = models.SmallIntegerField(db_column="Periodos", blank=True, null=True)
    acomodabox = models.CharField(db_column="AcomodaBox", max_length=1, blank=True, null=True)
    mdatos = models.CharField(max_length=1, blank=True, null=True)
    ndatos = models.SmallIntegerField(db_column="Ndatos", blank=True, null=True)
    vercpk = models.SmallIntegerField(db_column="VerCPK", blank=True, null=True)
    tmcf = models.SmallIntegerField(db_column="TMCF", blank=True, null=True)
    desvstd = models.CharField(max_length=1, blank=True, null=True)
    arcoiris = models.CharField(max_length=1, blank=True, null=True)
    tamcolvar = models.BigIntegerField(blank=True, null=True)
    tamcoldispo = models.BigIntegerField(blank=True, null=True)
    tamcollibre = models.BigIntegerField(blank=True, null=True)
    headcert = models.CharField(db_column="headCert", max_length=1, blank=True, null=True)
    hideoutlim = models.CharField(db_column="HideOutLim", max_length=1, blank=True, null=True)
    grafuni = models.CharField(db_column="GrafUni", max_length=1, blank=True, null=True)
    vermultilim = models.CharField(
        db_column="Vermultilim", max_length=1, blank=True, null=True
    )
    tipovista = models.CharField(db_column="Tipovista", max_length=1, blank=True, null=True)
    multilim = models.CharField(max_length=1, blank=True, null=True)
    showclave = models.BooleanField(blank=True, null=True)
    areaverde = models.FloatField(db_column="AreaVerde", blank=True, null=True)
    bajocurva = models.CharField(db_column="BajoCurva", max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Preferencias"


class Reglasweco(models.Model):
    productoid = models.OneToOneField(
        "Productos", models.DO_NOTHING, db_column="ProductoID", primary_key=True
    )
    caracteristicaid = models.ForeignKey(
        "Caracteristicas", models.DO_NOTHING, db_column="CaracteristicaID"
    )
    status1 = models.SmallIntegerField(db_column="Status1")
    regla1n = models.SmallIntegerField(db_column="Regla1n", blank=True, null=True)
    regla1m = models.SmallIntegerField(db_column="Regla1m", blank=True, null=True)
    status2 = models.SmallIntegerField(db_column="Status2")
    regla2n = models.SmallIntegerField(db_column="Regla2n", blank=True, null=True)
    regla2m = models.SmallIntegerField(db_column="Regla2m", blank=True, null=True)
    status3 = models.SmallIntegerField(db_column="Status3")
    regla3n = models.SmallIntegerField(db_column="Regla3n", blank=True, null=True)
    regla3m = models.SmallIntegerField(db_column="Regla3m", blank=True, null=True)
    status4 = models.SmallIntegerField(db_column="Status4")
    regla4n = models.SmallIntegerField(db_column="Regla4n", blank=True, null=True)
    regla4m = models.SmallIntegerField(db_column="Regla4m", blank=True, null=True)
    status5 = models.SmallIntegerField(db_column="Status5")
    regla5n = models.SmallIntegerField(db_column="Regla5n", blank=True, null=True)
    regla5m = models.SmallIntegerField(db_column="Regla5m", blank=True, null=True)
    status6 = models.SmallIntegerField(db_column="Status6")
    regla6n = models.SmallIntegerField(db_column="Regla6n", blank=True, null=True)
    regla6m = models.SmallIntegerField(db_column="Regla6m", blank=True, null=True)
    status7 = models.SmallIntegerField(db_column="Status7")
    regla7n = models.SmallIntegerField(db_column="Regla7n", blank=True, null=True)
    regla7m = models.SmallIntegerField(db_column="Regla7m", blank=True, null=True)
    status8 = models.SmallIntegerField(db_column="Status8")
    regla8n = models.SmallIntegerField(db_column="Regla8n", blank=True, null=True)
    regla8m = models.SmallIntegerField(db_column="Regla8m", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ReglasWECO"
        unique_together = (("productoid", "caracteristicaid"),)


class Systemlogs(models.Model):
    fecha = models.DateTimeField(db_column="Fecha", blank=True, null=True)
    usuarioid = models.CharField(db_column="UsuarioID", max_length=15, blank=True, null=True)
    modulo = models.CharField(db_column="Modulo", max_length=50, blank=True, null=True)
    accion = models.CharField(db_column="Accion", max_length=20, blank=True, null=True)
    comentarios = models.TextField(db_column="Comentarios", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "SystemLogs"


class Version(models.Model):
    version = models.CharField(db_column="Version", max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Version"


class Acciones(models.Model):
    accionid = models.CharField(primary_key=True, max_length=12)
    nombre1 = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "acciones"


class Axb(models.Model):
    bitacoraid = models.OneToOneField(
        "Bitacoras", models.DO_NOTHING, db_column="bitacoraid", primary_key=True
    )
    accionid = models.ForeignKey(Acciones, models.DO_NOTHING, db_column="accionid")

    class Meta:
        managed = False
        db_table = "axb"
        unique_together = (("bitacoraid", "accionid"),)


class Bitacoras(models.Model):
    bitacoraid = models.CharField(primary_key=True, max_length=12)
    nombre1 = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "bitacoras"


class Bxf(models.Model):
    formatoid = models.OneToOneField(
        "Formatos", models.DO_NOTHING, db_column="formatoid", primary_key=True
    )
    bitacoraid = models.ForeignKey(Bitacoras, models.DO_NOTHING, db_column="bitacoraid")

    class Meta:
        managed = False
        db_table = "bxf"
        unique_together = (("formatoid", "bitacoraid"),)


class Caracteristicas(models.Model):
    caracteristicaid = models.CharField(primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    tipoanalisis = models.CharField(
        db_column="Tipoanalisis", max_length=1, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "caracteristicas"


class Claves(models.Model):
    claveid = models.CharField(primary_key=True, max_length=24)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "claves"


class Cxc(models.Model):
    caracteristicaid = models.OneToOneField(
        Caracteristicas, models.DO_NOTHING, db_column="caracteristicaid", primary_key=True
    )
    claveid = models.ForeignKey(Claves, models.DO_NOTHING, db_column="claveid")

    class Meta:
        managed = False
        db_table = "cxc"
        unique_together = (("caracteristicaid", "claveid"),)


class Cxf(models.Model):
    formatoid = models.OneToOneField(
        "Formatos", models.DO_NOTHING, db_column="formatoid", primary_key=True
    )
    caracteristicaid = models.ForeignKey(
        Caracteristicas, models.DO_NOTHING, db_column="caracteristicaid"
    )
    posicion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cxf"
        unique_together = (("formatoid", "caracteristicaid"),)


class Cxp(models.Model):
    productoid = models.OneToOneField(
        "Productos", models.DO_NOTHING, db_column="productoid", primary_key=True
    )
    caracteristicaid = models.ForeignKey(
        Caracteristicas, models.DO_NOTHING, db_column="caracteristicaid"
    )
    tipoanalisis = models.CharField(max_length=1, blank=True, null=True)
    uni_o_bi = models.CharField(max_length=1, blank=True, null=True)
    unidad = models.CharField(max_length=10, blank=True, null=True)
    lse = models.FloatField(blank=True, null=True)
    lie = models.FloatField(blank=True, null=True)
    lsn = models.FloatField(blank=True, null=True)
    lmn = models.FloatField(blank=True, null=True)
    lin = models.FloatField(blank=True, null=True)
    lsr = models.FloatField(blank=True, null=True)
    lsc = models.FloatField(blank=True, null=True)
    lic = models.FloatField(blank=True, null=True)
    subgrupo = models.IntegerField(blank=True, null=True)
    decimales = models.SmallIntegerField(blank=True, null=True)
    critica = models.CharField(max_length=1, blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    captura = models.CharField(max_length=1, blank=True, null=True)
    formula = models.CharField(max_length=50, blank=True, null=True)
    instrumento = models.CharField(max_length=8, blank=True, null=True)
    puerto = models.CharField(max_length=2, blank=True, null=True)
    movimiento = models.CharField(max_length=1, blank=True, null=True)
    busqueda = models.CharField(max_length=1, blank=True, null=True)
    avisolimite = models.CharField(max_length=12, blank=True, null=True)
    avisotendencia = models.CharField(max_length=12, blank=True, null=True)
    avisoadhesion = models.CharField(max_length=12, blank=True, null=True)
    avisoproceso = models.CharField(max_length=12, blank=True, null=True)
    imagen = models.CharField(max_length=20, blank=True, null=True)
    obligasubgpo = models.BooleanField(db_column="ObligaSubGpo", blank=True, null=True)
    db = models.CharField(db_column="DB", max_length=10, blank=True, null=True)
    query = models.TextField(db_column="Query", blank=True, null=True)
    formatofecha = models.CharField(
        db_column="Formatofecha", max_length=24, blank=True, null=True
    )
    aviso4 = models.CharField(db_column="AVISO4", max_length=12, blank=True, null=True)
    aviso5 = models.CharField(db_column="AVISO5", max_length=12, blank=True, null=True)
    aviso6 = models.CharField(db_column="AVISO6", max_length=12, blank=True, null=True)
    aviso7 = models.CharField(db_column="AVISO7", max_length=12, blank=True, null=True)
    aviso8 = models.CharField(db_column="AVISO8", max_length=12, blank=True, null=True)
    aviso9 = models.CharField(db_column="AVISO9", max_length=12, blank=True, null=True)
    bitaut = models.BooleanField(db_column="BITAUT", blank=True, null=True)
    enviauser = models.CharField(db_column="EnviaUser", max_length=200, blank=True, null=True)
    monitoreo = models.BooleanField(blank=True, null=True)
    enviaemail = models.CharField(
        db_column="Enviaemail", max_length=200, blank=True, null=True
    )
    resultados = models.BooleanField(db_column="Resultados", blank=True, null=True)
    nresultados = models.IntegerField(db_column="NResultados", blank=True, null=True)
    periodoresultados = models.CharField(
        db_column="PeriodoResultados", max_length=4, blank=True, null=True
    )
    gageadmin = models.CharField(db_column="GageAdmin", max_length=10, blank=True, null=True)
    tipotituloemail = models.IntegerField(db_column="TipoTituloEmail", blank=True, null=True)
    tituloemail = models.CharField(
        db_column="TituloEmail", max_length=20, blank=True, null=True
    )
    detalleemail = models.BooleanField(db_column="DetalleEmail", blank=True, null=True)
    ncapest = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cxp"
        unique_together = (("productoid", "caracteristicaid"),)


class Estaciones(models.Model):
    estacionid = models.CharField(primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "estaciones"


class Exu(models.Model):
    usuarioid = models.OneToOneField(
        "user.User", models.DO_NOTHING, db_column="usuarioid", primary_key=True
    )
    estacionid = models.ForeignKey(Estaciones, models.DO_NOTHING, db_column="estacionid")

    class Meta:
        managed = False
        db_table = "exu"
        unique_together = (("usuarioid", "estacionid"),)


class Formatos(models.Model):
    formatoid = models.CharField(primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "formatos"


class Fxp(models.Model):
    productoid = models.OneToOneField(
        "Productos", models.DO_NOTHING, db_column="productoid", primary_key=True
    )
    formatoid = models.ForeignKey(Formatos, models.DO_NOTHING, db_column="formatoid")

    class Meta:
        managed = False
        db_table = "fxp"
        unique_together = (("productoid", "formatoid"),)


class GageAdmin(models.Model):
    clave = models.CharField(primary_key=True, max_length=10)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=20, blank=True, null=True)
    nserie = models.CharField(max_length=20, blank=True, null=True)
    gagestaid = models.CharField(db_column="GageStaId", max_length=15, blank=True, null=True)
    gagedepaid = models.ForeignKey(
        "GageDepartamentos", models.DO_NOTHING, db_column="GageDepaId", blank=True, null=True
    )
    gagetipoid = models.ForeignKey(
        "GageTipos", models.DO_NOTHING, db_column="GageTipoId", blank=True, null=True
    )
    frecuencia = models.IntegerField(db_column="Frecuencia", blank=True, null=True)
    ultimacalibracion = models.CharField(
        db_column="UltimaCalibracion", max_length=8, blank=True, null=True
    )
    proximacalibracion = models.CharField(
        db_column="ProximaCalibracion", max_length=8, blank=True, null=True
    )
    documento = models.CharField(db_column="Documento", max_length=50, blank=True, null=True)
    interfase = models.CharField(db_column="Interfase", max_length=50, blank=True, null=True)
    gagefabid = models.ForeignKey(
        "GageFabricantes", models.DO_NOTHING, db_column="GageFabId", blank=True, null=True
    )
    imagen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gage_admin"


class GageDepartamentos(models.Model):
    gagedepaid = models.CharField(db_column="GageDepaId", primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gage_departamentos"


class GageEstatus(models.Model):
    gagestaid = models.CharField(db_column="GageStaId", primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gage_estatus"


class GageFabricantes(models.Model):
    gagefabid = models.CharField(db_column="GageFabId", primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gage_fabricantes"


class GageTipos(models.Model):
    gagetipoid = models.CharField(db_column="GageTipoId", primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gage_tipos"


class Instrumentos(models.Model):
    instrumentoid = models.CharField(primary_key=True, max_length=12)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    parametros = models.CharField(max_length=10, blank=True, null=True)
    terminado = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    numcols = models.SmallIntegerField(db_column="NumCols", blank=True, null=True)
    validacon = models.CharField(db_column="ValidaCon", max_length=50, blank=True, null=True)
    envia = models.CharField(max_length=50, blank=True, null=True)
    posini = models.CharField(db_column="PosIni", max_length=250, blank=True, null=True)
    posfin = models.CharField(db_column="PosFin", max_length=250, blank=True, null=True)
    longitud = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "instrumentos"


class Maquinas(models.Model):
    maquinaid = models.CharField(primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "maquinas"


class Mxe(models.Model):
    estacionid = models.OneToOneField(
        Estaciones, models.DO_NOTHING, db_column="estacionid", primary_key=True
    )
    maquinaid = models.ForeignKey(Maquinas, models.DO_NOTHING, db_column="maquinaid")

    class Meta:
        managed = False
        db_table = "mxe"
        unique_together = (("estacionid", "maquinaid"),)


class Productos(models.Model):
    productoid = models.CharField(primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50, blank=True, null=True)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    consolidado = models.BooleanField(db_column="Consolidado", blank=True, null=True)
    imagen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "productos"


class Pxm(models.Model):
    maquinaid = models.OneToOneField(
        Maquinas, models.DO_NOTHING, db_column="maquinaid", primary_key=True
    )
    productoid = models.ForeignKey(Productos, models.DO_NOTHING, db_column="productoid")
    prodteorico = models.IntegerField(db_column="prodTeorico", blank=True, null=True)
    prodreal = models.IntegerField(db_column="prodReal", blank=True, null=True)
    uproduccion = models.CharField(
        db_column="uProduccion", max_length=4, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "pxm"
        unique_together = (("maquinaid", "productoid"),)

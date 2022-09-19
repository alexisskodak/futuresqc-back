from django.db import models


class Scenario(models.Model):
    idescenario = models.AutoField(db_column="IdEscenario", primary_key=True)
    nombreescenario = models.CharField(
        db_column="nombreEscenario", max_length=50, blank=True, null=True
    )
    idusuario = models.CharField(max_length=15, blank=True, null=True)
    idestacion = models.CharField(max_length=15, blank=True, null=True)
    idmaquina = models.CharField(max_length=15, blank=True, null=True)
    idproducto = models.CharField(max_length=15, blank=True, null=True)
    idformato = models.CharField(max_length=15, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    pausa = models.CharField(max_length=2, blank=True, null=True)
    columnas = models.CharField(max_length=500, blank=True, null=True)
    nombrepantalla = models.CharField(
        db_column="nombrePantalla", max_length=50, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Escenarios"


class Escenariosview(models.Model):
    idescenario = models.AutoField(db_column="IdEscenario", primary_key=True)
    nombreescenario = models.CharField(
        db_column="nombreEscenario", max_length=50, blank=True, null=True
    )
    idusuario = models.CharField(db_column="idUsuario", max_length=24, blank=True, null=True)
    idestacion = models.CharField(db_column="idEstacion", max_length=24, blank=True, null=True)
    idmaquina = models.CharField(db_column="idMaquina", max_length=24, blank=True, null=True)
    idproducto = models.CharField(db_column="idProducto", max_length=24, blank=True, null=True)
    idformato = models.CharField(db_column="idFormato", max_length=24, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    pausa = models.CharField(max_length=2, blank=True, null=True)
    columnas = models.CharField(max_length=500, blank=True, null=True)
    nombrepantalla = models.CharField(
        db_column="nombrePantalla", max_length=100, blank=True, null=True
    )
    status = models.BooleanField(blank=True, null=True)
    statusfavorito = models.BooleanField(db_column="statusFavorito", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "escenariosView"

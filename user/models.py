from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class UserManager(models.Manager):
    def get_by_natural_key(self, usuarioid):
        return self.get(usuarioid=usuarioid)


class User(AbstractBaseUser):
    objects = UserManager()
    last_login = None

    usuarioid = models.CharField(primary_key=True, max_length=15)
    nombre1 = models.CharField(max_length=50)
    password = models.CharField(db_column="contraseña", max_length=10, blank=True, null=True)
    opcion01 = models.BooleanField()
    opcion02 = models.BooleanField()
    opcion03 = models.BooleanField()
    opcion04 = models.BooleanField()
    opcion05 = models.BooleanField()
    opcion06 = models.BooleanField()
    opcion07 = models.BooleanField()
    opcion08 = models.BooleanField()
    opcion09 = models.BooleanField()
    opcion10 = models.BooleanField()
    opcion11 = models.BooleanField()
    opcion12 = models.BooleanField()
    opcion13 = models.BooleanField()
    opcion14 = models.BooleanField()
    opcion15 = models.BooleanField()
    opcion16 = models.BooleanField()
    opcion17 = models.BooleanField()
    opcion18 = models.BooleanField()
    opcion19 = models.BooleanField()
    opcion20 = models.BooleanField()
    opcion21 = models.BooleanField()
    opcion22 = models.BooleanField()
    opcion23 = models.BooleanField()
    opcion24 = models.BooleanField()
    opcion25 = models.BooleanField()
    opcion26 = models.BooleanField()
    opcion27 = models.BooleanField()
    opcion28 = models.BooleanField()
    poder01 = models.BooleanField()
    poder02 = models.BooleanField()
    poder03 = models.BooleanField()
    poder04 = models.BooleanField()
    poder05 = models.BooleanField()
    poder06 = models.BooleanField()
    poder07 = models.BooleanField()
    poder08 = models.BooleanField()
    poder09 = models.BooleanField()
    poder10 = models.BooleanField()
    poder11 = models.BooleanField()
    poder12 = models.BooleanField()
    poder13 = models.BooleanField()
    poder14 = models.BooleanField()
    poder15 = models.BooleanField()
    poder16 = models.BooleanField()
    poder17 = models.BooleanField()
    poder18 = models.BooleanField()
    poder19 = models.BooleanField()
    poder20 = models.BooleanField()
    poder21 = models.BooleanField()
    poder22 = models.BooleanField()
    poder23 = models.BooleanField()
    poder24 = models.BooleanField()
    poder25 = models.BooleanField()
    poder26 = models.BooleanField()
    poder27 = models.BooleanField()
    picture = models.CharField(db_column="Picture", max_length=50, blank=True, null=True)
    caducidadpwd = models.CharField(max_length=8, blank=True, null=True)
    lock = models.BooleanField(blank=True, null=True)
    bit_importar = models.BooleanField(db_column="Bit_Importar")
    bit_exportar = models.BooleanField(db_column="Bit_Exportar")
    bit_pwd = models.BooleanField(db_column="Bit_Pwd")
    bit_colorfontgraf = models.BooleanField(db_column="Bit_ColorFontGraf")
    email = models.CharField(max_length=200, blank=True, null=True)
    statususuario = models.BooleanField(db_column="statusUsuario")

    USERNAME_FIELD = "usuarioid"
    REQUIRED_FIELDS = ["nombre1"]

    def check_password(self, raw_password):
        return raw_password == self.password.rstrip()

    class Meta:
        managed = False
        db_table = "usuarios"

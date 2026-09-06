from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MinLengthValidator
class Accounts(models.Model):
    name                = models.CharField(verbose_name="Nombre",max_length=50)
    paternal_surname    = models.CharField(verbose_name="Apellido Paterno",max_length=50)
    maternal_surname    = models.CharField(verbose_name="Apellido Materno",blank=True)
    rfc                 = models.CharField(verbose_name="RFC",max_length=13,validators=[MinLengthValidator(13)])
    datebirth           = models.DateField(verbose_name="Fecha de nacimiento")
    email               = models.EmailField(verbose_name="Correo",max_length=254,unique=True)
    password            = models.CharField(verbose_name="Contraseña",max_length=128)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith("pbkdf2_"):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        print(raw_password)
        print(check_password(raw_password, self.password))
        return check_password(raw_password, self.password)

class Address(models.Model):
    account_id          = models.ForeignKey("accounts.Accounts", verbose_name="Cuenta", on_delete=models.CASCADE)
    address             = models.CharField(verbose_name="Dirección",max_length=250)
    internal_number     = models.CharField(verbose_name="Número interno",max_length=120)
    external_number     = models.CharField(verbose_name="Número externo",max_length=120)
    postal              = models.CharField(verbose_name="Código Postal",max_length=5)
    suburb              = models.CharField(verbose_name="Delegación",max_length=60)
    country             = models.CharField(verbose_name="País",max_length=60)

class CreditCard(models.Model):
    account_id          = models.ForeignKey("accounts.Accounts", verbose_name="Cuenta", on_delete=models.CASCADE)
    card_number         = models.CharField(verbose_name="Número de tarjeta",max_length=16)
    expiration          = models.CharField(verbose_name="Fecha de expiración",max_length=16)
    cvc                 = models.CharField(verbose_name="CVC",max_length=3)

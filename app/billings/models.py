from django.db import models

# Create your models here.
class Billing(models.Model):
    account_id      = models.ForeignKey("accounts.Accounts", verbose_name="Cuenta", on_delete=models.CASCADE)
    address_id      = models.ForeignKey("accounts.Address", verbose_name="Dirección de envio", on_delete=models.CASCADE)
    payment_id      = models.ForeignKey("accounts.CreditCard", verbose_name="Método de Pago", on_delete=models.CASCADE)
    total           = models.FloatField("Total de compra")
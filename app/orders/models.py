from django.db import models

# Create your models here.
class Orders(models.Model):
    billing_id      = models.ForeignKey("billings.Billing", verbose_name="Recibo", on_delete=models.CASCADE)
    product_id      = models.ForeignKey("products.Products",verbose_name="Producto", on_delete=models.CASCADE)
    count           = models.IntegerField(verbose_name="Cantidad")
    total           = models.FloatField(verbose_name="Total")


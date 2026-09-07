from django.db import models

# Create your models here.
class Orders(models.Model):
    billing         = models.ForeignKey("billings.Billing",related_name="orders", verbose_name="Recibo", on_delete=models.CASCADE)
    product         = models.ForeignKey("products.Products",verbose_name="Producto", on_delete=models.CASCADE)
    count           = models.IntegerField(verbose_name="Cantidad")
    total           = models.FloatField(verbose_name="Total")


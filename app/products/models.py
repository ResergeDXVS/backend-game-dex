from django.db import models

CATEGORY_CHOICES={
    ("consoles","Consolas"),
    ("games","Juegos"),
    ("controls","Controles"),
    ("passes","Pases"),
    ("accessories","Accesorios"),
}
# Create your models here.
class Companies(models.Model):
    name        = models.CharField(verbose_name="Nombre",max_length=40,unique=True)
    image_url   = models.URLField(verbose_name="URL",blank=False)

    def __str__(self):
        return self.name


class Products(models.Model):
    name            = models.CharField(verbose_name="Nombre",max_length=255,unique=True)
    image_url       = models.URLField(verbose_name="URL",blank=False)
    release_date    = models.DateField(verbose_name="Fecha de lanzamiento")
    description     = models.CharField(verbose_name="Descripción")
    price           = models.FloatField(verbose_name="Precio")
    promotion       = models.FloatField(verbose_name="Promoción")
    category        = models.CharField(verbose_name="Categoria",default="PENDING",choices=CATEGORY_CHOICES)
    company_id      = models.ForeignKey("products.Companies",verbose_name="Compañia", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
from django.db import models
from .product import Product  # Importación relativa del modelo Product
from .bodega import Bodega    # Importación relativa del modelo Bodega

class Inventario(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta:
        unique_together = ['product', 'bodega']

    def __str__(self):
        return f"{self.product.nombre} - {self.bodega.nombre} - {self.stock}"

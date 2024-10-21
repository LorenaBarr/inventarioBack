from django.db import models
from .product import Product  
from .bodega import Bodega    

class Inventario(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()  # Solo valores positivos

    class Meta:
        unique_together = ['product', 'bodega']

    def __str__(self):
        return f"{self.product.nombre} - {self.bodega.nombre} - {self.stock}"

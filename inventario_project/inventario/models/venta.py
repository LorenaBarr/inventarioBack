from django.db import models
from .product import Product  # Importación relativa del modelo Product
from .bodega import Bodega    # Importación relativa del modelo Bodega

class Venta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta: {self.product.nombre} - {self.bodega.nombre} - {self.cantidad}"

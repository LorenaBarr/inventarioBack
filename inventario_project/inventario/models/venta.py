from django.db import models, transaction
from .product import Product
from .bodega import Bodega
from .inventario import Inventario
from django.core.exceptions import ValidationError
from django.db.models import F

class Venta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta: {self.product.nombre} - {self.bodega.nombre} - {self.cantidad}"

    def clean(self):
        inventario = Inventario.objects.filter(product=self.product, bodega=self.bodega).first()
        if not inventario or inventario.stock < self.cantidad:
            raise ValidationError(f"No hay suficiente stock disponible para {self.product.nombre} en la bodega {self.bodega.nombre}. Disponible: {inventario.stock if inventario else 0}")

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.clean()
        super(Venta, self).save(*args, **kwargs)
        Inventario.objects.filter(product=self.product, bodega=self.bodega).update(stock=F('stock') - self.cantidad)

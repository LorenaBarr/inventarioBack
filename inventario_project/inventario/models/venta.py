from django.db import models, transaction
from .product import Product  # Importación relativa del modelo Product
from .bodega import Bodega    # Importación relativa del modelo Bodega
from .inventario import Inventario  # Asegúrate de importar Inventario
from django.core.exceptions import ValidationError
from django.db.models import F
from django.contrib.auth.models import User

class Venta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()  # Solo valores positivos
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con User

    def __str__(self):
        return f"Venta: {self.product.nombre} - {self.bodega.nombre} - {self.cantidad}"

    def clean(self):
        # Validación para asegurar que la cantidad vendida no exceda el stock disponible
        inventario = Inventario.objects.filter(product=self.product, bodega=self.bodega).first()
        if not inventario or inventario.stock < self.cantidad:
            raise ValidationError(f"No hay suficiente stock disponible para {self.product.nombre} en la bodega {self.bodega.nombre}. Disponible: {inventario.stock if inventario else 0}")

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.clean()  # Llamamos la validación antes de guardar

        # Guardamos la venta
        super(Venta, self).save(*args, **kwargs)

        # Reducir el stock después de realizar la venta
        Inventario.objects.filter(product=self.product, bodega=self.bodega).update(stock=F('stock') - self.cantidad)
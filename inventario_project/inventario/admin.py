from django.contrib import admin
from .models import Product, Bodega, Inventario, Venta

admin.site.register(Product)
admin.site.register(Bodega)
admin.site.register(Inventario)
admin.site.register(Venta)


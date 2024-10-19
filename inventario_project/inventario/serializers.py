from rest_framework import serializers
from .models import Product, Bodega, Inventario, Venta

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):  # Cambiar Warehouse a Bodega
    class Meta:
        model = Bodega  # Cambiar Warehouse a Bodega
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

from rest_framework import serializers
from .models import Product, Bodega, Inventario, Venta
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Bodega  
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    product_nombre = serializers.CharField(source="product.nombre", read_only=True)
    bodega_nombre = serializers.CharField(source="bodega.nombre", read_only=True)

    class Meta:
        model = Inventario
        fields = ['product', 'product_nombre', 'bodega', 'bodega_nombre', 'stock']

class VentaSerializer(serializers.ModelSerializer):
    product_nombre = serializers.CharField(source='product.nombre', read_only=True)
    bodega_nombre = serializers.CharField(source='bodega.nombre', read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'product', 'product_nombre', 'bodega', 'bodega_nombre', 'cantidad', 'fecha']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user
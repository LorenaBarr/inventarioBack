from rest_framework import serializers
from .models import Product, Bodega, Inventario, Venta
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):  # Cambiado a BodegaSerializer
    class Meta:
        model = Bodega  # Cambiado a Bodega
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    product_nombre = serializers.CharField(source="product.nombre", read_only=True)
    bodega_nombre = serializers.CharField(source="bodega.nombre", read_only=True)

    class Meta:
        model = Inventario
        fields = ['product', 'product_nombre', 'bodega', 'bodega_nombre', 'stock']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

    def create(self, validated_data):
        # Asigna el usuario autenticado a la venta
        validated_data['usuario'] = self.context['request'].user
        return super(VentaSerializer, self).create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}  # Asegúrate de que la contraseña no se exponga
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Guarda la contraseña de manera segura
        user.save()
        return user
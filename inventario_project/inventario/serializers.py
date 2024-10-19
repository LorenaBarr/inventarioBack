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
    class Meta:
        model = Inventario
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

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
from rest_framework import viewsets
from .models import Product, Bodega, Inventario, Venta
from .serializers import ProductSerializer, BodegaSerializer, InventarioSerializer, VentaSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class BodegaViewSet(viewsets.ModelViewSet):  # Cambiado de WarehouseViewSet a BodegaViewSet
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer  # Cambiado de WarehouseSerializer a BodegaSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
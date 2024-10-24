from rest_framework import viewsets
from .models import Product, Bodega, Inventario, Venta
from .serializers import ProductSerializer, BodegaSerializer, InventarioSerializer, VentaSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    #filter
    filterset_fields = ['nombre', 'precio']  # Campos que se pueden filtrar
    ordering_fields = ['nombre', 'precio'] 




class BodegaViewSet(viewsets.ModelViewSet):  
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer  

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['product__nombre', 'bodega__nombre']  # Filtro por producto y bodega
    ordering_fields = ['stock']  # Ordenar por cantidad de stock

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['product__nombre', 'bodega__nombre']  # Filtros por producto y bodega
    ordering_fields = ['cantidad', 'fecha']  # Ordenar por cantidad de venta o fecha

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReporteVentasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Sumar la cantidad total de ventas por producto y bodega
        ventas_por_producto = Venta.objects.values('product__nombre').annotate(total_vendido=Sum('cantidad'))
        ventas_por_bodega = Venta.objects.values('bodega__nombre').annotate(total_vendido=Sum('cantidad'))

        total_ingresos = Venta.objects.aggregate(ingresos_totales=Sum('product__precio'))

        return Response({
            "ventas_por_producto": ventas_por_producto,
            "ventas_por_bodega": ventas_por_bodega,
            "total_ingresos": total_ingresos,
        })
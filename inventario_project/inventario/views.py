from rest_framework import viewsets
from .models.product import Product
from .models.bodega import Bodega
from .models.inventario import Inventario
from .models.venta import Venta
from .serializers import ProductSerializer, WarehouseSerializer, InventorySerializer, SaleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = WarehouseSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventorySerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = SaleSerializer

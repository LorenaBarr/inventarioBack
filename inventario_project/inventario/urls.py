from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BodegaViewSet, InventoryViewSet, SaleViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'productos', ProductViewSet)
router.register(r'bodegas', BodegaViewSet)
router.register(r'inventarios', InventoryViewSet)
router.register(r'ventas', SaleViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

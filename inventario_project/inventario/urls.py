from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BodegaViewSet, InventarioViewSet, VentaViewSet, UserRegisterView

# Para autenticación JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Definir enrutador y registrar las vistas
router = DefaultRouter()
router.register(r'productos', ProductViewSet)
router.register(r'bodegas', BodegaViewSet)
router.register(r'inventarios', InventarioViewSet)
router.register(r'ventas', VentaViewSet)

# Definir las rutas URL
urlpatterns = [
    path('api/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token JWT
    path('', include(router.urls)),  # Incluir las rutas generadas por el enrutador
]
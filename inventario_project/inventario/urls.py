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
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),  
]

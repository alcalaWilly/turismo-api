from django.urls import path,include
from rest_framework import routers
from api import views
from django.conf import settings
from django.conf.urls.static import static
from .consultas import CartaDestinoView

router = routers.DefaultRouter()
router.register(r'categorias',views.CategoriaViewSet)
router.register(r'lugar',views.LugarViewSet)
router.register(r'destino',views.DestinoViewSet)
router.register(r'detalleCategoria',views.DetalleCategoriaViewSet)

router.register(r'ofrece',views.OfreceViewSet)
router.register(r'imagen',views.ImagenViewSet)
router.register(r'incluye',views.IncluyeViewSet)
router.register(r'noIncluye',views.NoIncluyeViewSet)
router.register(r'itinerario',views.ItinerarioViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('cartaDestino/<int:destino_id>/', CartaDestinoView.as_view(), name='destino-detalle'),
] 

# urlpatterns += router.urls
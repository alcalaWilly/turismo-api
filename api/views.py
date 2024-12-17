from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategoriaSerializer,LugarSerializer,DetalleCategoriaSerializer,DestinoSerializer, OfreceSerializer,ImagenSerializer,IncluyeSerializer,NoIncluyeSerializer,ItinerarioSerializer
from .models import Categoria,Lugar,DetalleCategoria,Destino,Ofrece,Imagen,Incluye,NoIncluye,Itinerario
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

class DetalleCategoriaViewSet(viewsets.ModelViewSet):
    queryset = DetalleCategoria.objects.all()
    serializer_class = DetalleCategoriaSerializer

class OfreceViewSet(viewsets.ModelViewSet):
    queryset = Ofrece.objects.all()
    serializer_class = OfreceSerializer

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class IncluyeViewSet(viewsets.ModelViewSet):
    queryset = Incluye.objects.all()
    serializer_class = IncluyeSerializer

class NoIncluyeViewSet(viewsets.ModelViewSet):
    queryset = NoIncluye.objects.all()
    serializer_class = NoIncluyeSerializer

class ItinerarioViewSet(viewsets.ModelViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = ItinerarioSerializer











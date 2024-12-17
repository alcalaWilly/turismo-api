from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Categoria,Lugar,DetalleCategoria,Destino,Ofrece,Imagen,Incluye,NoIncluye,Itinerario
from .serializer import CategoriaSerializer,LugarSerializer,DetalleCategoriaSerializer,DestinoSerializer, OfreceSerializer,ImagenSerializer,IncluyeSerializer,NoIncluyeSerializer,ItinerarioSerializer


class CartaDestinoView(APIView):
    """
    API personalizada para obtener todos los detalles de un destino específico.
    """

    def get(self, request, destino_id):
        # Obtener el destino
        destino = get_object_or_404(Destino, id=destino_id,lCurrent=True)

        # Obtener el detalle de categoría relacionado con el destino
        #detalle_categoria = DetalleCategoria.objects.filter(destino=destino).first()

        detalle_categoria = DetalleCategoria.objects.filter(destino=destino).first()

        # Obtener el lugar y la categoría del destino, si existen
        lugar = detalle_categoria.lugar.cDescription if detalle_categoria else None
        categoria = detalle_categoria.categoria.cDescription if detalle_categoria else None

        # Obtener imágenes y otros detalles relacionados con el destino
        imagenesDestino = Imagen.objects.filter(destino=destino)
        destinoOfrece = Ofrece.objects.filter(destino=destino)
        destinoIncluye = Incluye.objects.filter(destino=destino)
        destinoNoIncluye = NoIncluye.objects.filter(destino=destino)
        itinerariosDestino = Itinerario.objects.filter(destino=destino)

        # Construir la respuesta
        response_data = {
            "id": destino.id,
            "categoria": categoria,
            "lugar": lugar,
            "destino": destino.cNomDestino,
            "descripcion": destino.cDescriptionDestino,
            "precio": destino.price,
            "imagenes": [imagen.curl.url for imagen in imagenesDestino],
            "ofrece": [ofrece.cDescription for ofrece in destinoOfrece],
            "incluye": [incluye.cDescription for incluye in destinoIncluye],
            "noIncluye": [noIncluye.cDescription for noIncluye in destinoNoIncluye],
            "itinerario": [
                {"hora": itinerario.cHora, "descripcion": itinerario.cDescription}
                for itinerario in itinerariosDestino
            ],
        }

        return Response(response_data, status=status.HTTP_200_OK)
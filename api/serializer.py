from rest_framework import serializers
from .models import Categoria,Lugar,DetalleCategoria,Destino,Ofrece,Imagen,Incluye,NoIncluye,Itinerario

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

class DetalleCategoriaSerializer(serializers.ModelSerializer):
    # Campos para mostrar en la salida
    categoria = serializers.SerializerMethodField()
    lugar = serializers.SerializerMethodField()
    destino= serializers.SerializerMethodField()

    # Campos para la entrada (escritura)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), write_only=False)
    lugar_id = serializers.PrimaryKeyRelatedField(queryset=Lugar.objects.all(), write_only=False)
    destino_id = serializers.PrimaryKeyRelatedField(queryset=Destino.objects.all(), write_only=False)
    

    class Meta:
        model = DetalleCategoria
        fields = ['id', 'categoria', 'categoria_id', 'lugar', 'lugar_id','destino','destino_id','lCurrent']

    # Métodos para obtener descripciones en la salida
    def get_categoria(self, obj):
        return obj.categoria.cDescription

    def get_lugar(self, obj):
        return obj.lugar.cDescription
    
    def get_destino(self, obj):
        return obj.destino.cNomDestino


    # Método para crear
    def create(self, validated_data):
        categoria = validated_data.pop('categoria_id')
        lugar = validated_data.pop('lugar_id')
        destino = validated_data.pop('destino_id')
        return DetalleCategoria.objects.create(categoria=categoria, lugar=lugar,destino=destino, **validated_data)

    # Método para actualizar
    def update(self, instance, validated_data):
        if 'categoria_id' in validated_data:
            instance.categoria = validated_data.pop('categoria_id')
        if 'lugar_id' in validated_data:
            instance.lugar = validated_data.pop('lugar_id')
        if 'destino_id' in validated_data:
            instance.destino = validated_data.pop('destino_id')
        
        instance.lCurrent = validated_data.get('lCurrent', instance.lCurrent)
        instance.save()
        return instance

#################################################3

class OfreceSerializer(serializers.ModelSerializer):
    # Campos para mostrar en la salida
    destino= serializers.SerializerMethodField()
    # Campos para la entrada (escritura)
    destino_id = serializers.PrimaryKeyRelatedField(queryset=Destino.objects.all(), write_only=False)

    class Meta:
        model = Ofrece
        fields = ['id','destino','destino_id','cDescription']

    # Métodos para obtener descripciones en la salida
    def get_destino(self, obj):
        return obj.destino.cNomDestino
    # Método para crear
    def create(self, validated_data):
        destino = validated_data.pop('destino_id')
        return Ofrece.objects.create(destino=destino, **validated_data)

    # Método para actualizar
    def update(self, instance, validated_data):
        if 'destino_id' in validated_data:
            instance.destino = validated_data.pop('destino_id')
        instance.save()
        return instance

class ImagenSerializer(serializers.ModelSerializer):
    # Campos para mostrar en la salida
    destino = serializers.SerializerMethodField()

    # Campos para la entrada (escritura)
    destino_id = serializers.PrimaryKeyRelatedField(queryset=Destino.objects.all(), write_only=True)

    class Meta:
        model = Imagen
        fields = ['id', 'destino', 'destino_id', 'curl']

    # Método para mostrar el nombre del destino en lugar del objeto completo
    def get_destino(self, obj):
        return obj.destino.cNomDestino

    # Método para crear un objeto Imagen
    def create(self, validated_data):
        destino = validated_data.pop('destino_id')
        return Imagen.objects.create(destino=destino, **validated_data)

    # Método para actualizar un objeto Imagen
    def update(self, instance, validated_data):
        if 'destino_id' in validated_data:
            instance.destino = validated_data.pop('destino_id')
        instance.curl = validated_data.get('curl', instance.curl)
        instance.save()
        return instance

class IncluyeSerializer(serializers.ModelSerializer):
    # Campos para mostrar en la salida
    destino= serializers.SerializerMethodField()
    # Campos para la entrada (escritura)
    destino_id = serializers.PrimaryKeyRelatedField(queryset=Destino.objects.all(), write_only=False)

    class Meta:
        model = Incluye
        fields = ['id','destino','destino_id','cDescription']

    # Métodos para obtener descripciones en la salida
    def get_destino(self, obj):
        return obj.destino.cNomDestino
    # Método para crear
    def create(self, validated_data):
        destino = validated_data.pop('destino_id')
        return Incluye.objects.create(destino=destino, **validated_data)

    # Método para actualizar
    def update(self, instance, validated_data):
        if 'destino_id' in validated_data:
            instance.destino = validated_data.pop('destino_id')
        instance.save()
        return instance
    
class NoIncluyeSerializer(serializers.ModelSerializer):
    # Campos para mostrar en la salida
    destino= serializers.SerializerMethodField()
    # Campos para la entrada (escritura)
    destino_id = serializers.PrimaryKeyRelatedField(queryset=Destino.objects.all(), write_only=False)

    class Meta:
        model = NoIncluye
        fields = ['id','destino','destino_id','cDescription']

    # Métodos para obtener descripciones en la salida
    def get_destino(self, obj):
        return obj.destino.cNomDestino
    # Método para crear
    def create(self, validated_data):
        destino = validated_data.pop('destino_id')
        return NoIncluye.objects.create(destino=destino, **validated_data)

    # Método para actualizar
    def update(self, instance, validated_data):
        if 'destino_id' in validated_data:
            instance.destino = validated_data.pop('destino_id')
        instance.save()
        return instance

class ItinerarioSerializer(serializers.ModelSerializer):
    # Campos para mostrar en la salida
    destino= serializers.SerializerMethodField()
    # Campos para la entrada (escritura)
    destino_id = serializers.PrimaryKeyRelatedField(queryset=Destino.objects.all(), write_only=False)

    class Meta:
        model = Itinerario
        fields = ['id','destino','destino_id','cHora','cDescription']

    # Métodos para obtener descripciones en la salida
    def get_destino(self, obj):
        return obj.destino.cNomDestino
    # Método para crear
    def create(self, validated_data):
        destino = validated_data.pop('destino_id')
        return Itinerario.objects.create(destino=destino, **validated_data)

    # Método para actualizar
    def update(self, instance, validated_data):
        if 'destino_id' in validated_data:
            instance.destino = validated_data.pop('destino_id')
        instance.save()
        return instance









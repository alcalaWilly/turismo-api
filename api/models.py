from django.db import models

# Create your models here.
class Categoria(models.Model):
    cDescription = models.CharField(max_length=50)
    lCurrent = models.BooleanField()
    def __str__(self):
        return self.cDescription

class Lugar(models.Model):
    cDescription = models.CharField(max_length=50)
    lCurrent = models.BooleanField()
    def __str__(self):
        return self.cDescription

class Destino(models.Model):
    cNomDestino = models.CharField(max_length=50)
    cDescriptionDestino = models.TextField()
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    lCurrent = models.BooleanField()
    def __str__(self):
        return self.cNomDestino

class DetalleCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    lCurrent = models.BooleanField()
#####################################################################
class Ofrece(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    cDescription = models.CharField(max_length=100)

class Imagen(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    curl = models.ImageField(upload_to='imagenes/')

class Incluye(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    cDescription = models.CharField(max_length=250)

class NoIncluye(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    cDescription = models.CharField(max_length=100)

class Itinerario(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    cHora = models.CharField(max_length=10)
    cDescription = models.CharField(max_length=100)
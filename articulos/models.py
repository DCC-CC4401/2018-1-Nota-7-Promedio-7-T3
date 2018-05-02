from django.db import models

# Create your models here.
class Articulos(models.Model):

    nombre_articulo = models.CharField(max_length=200)
    descripcion_articulo = models.CharField(max_length=1500)
    id_articulo = models.IntegerField()
    estado_articulo = models.CharField(max_length=10, default="Disponible")
    foto_articulo = models.CharField(max_length=1000)
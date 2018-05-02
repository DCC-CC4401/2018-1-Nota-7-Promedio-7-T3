from django.db import models

# Create your models here.


class Espacios(models.Model):

    nombre_espacio = models.CharField(max_length=200)
    descripcion_espacio = models.CharField(max_length=1500)
    id_espacio = models.IntegerField()
    capacidad_espacio = models.IntegerField()
    estado_espacio = models.CharField(max_length=10,default="Disponible")
    foto_espacio = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre_espacio
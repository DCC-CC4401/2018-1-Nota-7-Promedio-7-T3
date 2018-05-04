from django.db import models


class Espacios(models.Model):

    ESTADOS_ESP = ((1, 'Disponible'), (2, 'Prestado'), (3, 'Reparación'))
    estado_espacio = models.IntegerField(choices=ESTADOS_ESP,default=1)
    nombre_espacio = models.CharField(max_length=200)
    descripcion_espacio = models.CharField(max_length=1500)
    id_espacio = models.IntegerField()
    capacidad_espacio = models.IntegerField()
    foto_espacio = models.ImageField()

    def __str__(self):
        return self.nombre_espacio
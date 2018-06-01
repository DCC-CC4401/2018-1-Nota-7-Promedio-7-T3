from django.db import models


class Espacios(models.Model):

    ESTADOS_ESP = ((1, 'Disponible'), (2, 'Prestado'), (3, 'Reparación'))
    estado_espacio = models.IntegerField(choices=ESTADOS_ESP,default=1)
    nombre_espacio = models.CharField(max_length=200)
    descripcion_espacio = models.CharField(max_length=1500,default="")
    capacidad_espacio = models.IntegerField(default=0)
    foto_espacio = models.ImageField(upload_to='uploads/fotos_espacios', default="")

    '''
    def __str__(self):
        return self.nombre_espacio
    '''
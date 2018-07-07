from django.db import models


class Articulos(models.Model):

    ESTADOS_ART = ((1, 'Disponible'), (2, 'Prestado'), (3, 'Reparación'), (4, 'Perdido'))
    estado_articulo = models.IntegerField(choices=ESTADOS_ART, default=1)
    nombre_articulo = models.CharField(max_length=200)
    descripcion_articulo = models.CharField(max_length=1500)
    foto_articulo = models.ImageField(upload_to='uploads/fotos_articulos')

    def __str__(self):
        return self.nombre_articulo
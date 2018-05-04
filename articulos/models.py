from django.db import models


class Articulos(models.Model):

    ESTADOS_ART = ((1, 'Disponible'), (2, 'Prestado'), (3, 'Reparación'), (4, 'Perdido'))
    estado_articulo = models.IntegerField(choices=ESTADOS_ART, default=1)
    nombre_articulo = models.CharField(max_length=200)
    descripcion_articulo = models.CharField(max_length=1500)
    id_articulo = models.IntegerField()
    foto_articulo = models.ImageField()
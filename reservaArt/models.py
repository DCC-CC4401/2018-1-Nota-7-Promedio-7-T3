from django.db import models
from articulos.models import Articulos


class ReservaArticulo(models.Model):

    id_articulo = models.ForeignKey(Articulos)
    fecha_inicio = models.TimeField()
    fecha_termino = models.TimeField()
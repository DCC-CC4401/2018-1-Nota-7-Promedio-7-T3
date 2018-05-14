from django.db import models
from articulos.models import Articulos


class ReservaArticulo(models.Model):


    id_articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()

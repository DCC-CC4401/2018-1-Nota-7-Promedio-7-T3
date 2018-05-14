from django.db import models
from articulos.models import Articulos
from espacios.models import Espacios

class ReservaArticulo(models.Model):
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    final = models.DateTimeField()

class ReservaEspacio(models.Model):
    id_espacio = models.ForeignKey(Espacios, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    final = models.DateTimeField()


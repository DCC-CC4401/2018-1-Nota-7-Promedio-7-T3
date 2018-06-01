from django.db import models
from articulos.models import Articulos
from espacios.models import Espacios
from userprofile.models import Perfil

class ReservaArticulo(models.Model):
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    ESTADOS_RES = ((1, 'Pendiente'), (2, 'Entregado'), (3, 'Rechazado'))
    estado_reserva = models.IntegerField(choices=ESTADOS_RES, default=1)

class ReservaEspacio(models.Model):
    espacio = models.ForeignKey(Espacios, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    ESTADOS_RES = ((1, 'Pendiente'), (2, 'Entregado'), (3, 'Rechazado'))
    estado_reserva = models.IntegerField(choices=ESTADOS_RES, default=1)


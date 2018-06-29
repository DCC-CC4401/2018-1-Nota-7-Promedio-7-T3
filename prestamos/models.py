from django.db import models
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from reservas.models import ReservaEspacio

class PrestamoArticulo(models.Model):
    reserva = models.ForeignKey(ReservaArticulo, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    ESTADOS_PRES = ((1, 'Vigente'), (2, 'Caducado'), (3, 'Perdido'))
    estado_reserva = models.IntegerField(choices=ESTADOS_PRES, default=1)

class PrestamoEspacio(models.Model):
    reserva = models.ForeignKey(ReservaEspacio, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    ESTADOS_PRES = ((1, 'Vigente'), (2, 'Caducado'), (3, 'Perdido'))
    estado_reserva = models.IntegerField(choices=ESTADOS_PRES, default=1)
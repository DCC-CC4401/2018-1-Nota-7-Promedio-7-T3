from django.contrib import admin
from .models import ReservaArticulo
from .models import ReservaEspacio
# Register your models here.

admin.site.register(ReservaEspacio)
admin.site.register(ReservaArticulo)
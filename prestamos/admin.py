from django.contrib import admin
from .models import PrestamoArticulo
from .models import PrestamoEspacio

admin.site.register(PrestamoEspacio)
admin.site.register(PrestamoArticulo)

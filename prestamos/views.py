from django.shortcuts import render
from django.views.generic import View
from .models import PrestamoArticulo
from .models import PrestamoEspacio

from django_tables2   import RequestConfig
from .tables  import  PrestamosArticulosTable
from .tables  import  PrestamosEspaciosTable
from .apps import PrestamosConfig


def prestamosView(request):
    table = PrestamosArticulosTable(PrestamoArticulo.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'grilla_Pres.html', {'table': table})

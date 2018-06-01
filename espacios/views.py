from django.shortcuts import render
from django.views.generic import View
from .models import Espacios

from django_tables2   import RequestConfig
from .tables  import EspaciosTable
from .apps import EspaciosConfig


def espaciosView(request):
    table = EspaciosTable(Espacios.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'grilla_Esp.html', {'table': table})
    #return render(request, 'grilla_Esp.html', {'espacio': EspaciosTable.objects.all()})


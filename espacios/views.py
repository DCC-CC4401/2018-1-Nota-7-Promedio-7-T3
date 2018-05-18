from django.shortcuts import render
from django.views.generic import View
from .models import Espacios

from django_tables2   import RequestConfig
from .tables  import EspaciosTable


def espaciosView(request):
    return render(request, 'templates/grilla_Esp.html', {'espacio': Espacios.objects.all()})


from django.shortcuts import render
from django.views.generic import View
from .models import Espacios

from django_tables2   import RequestConfig
from .tables  import EspaciosTable


class EspaciosView(View):
    def espaciosV():
        return render( 'grilla_Esp.html.html', {'people': Espacios.objects.all()})



import django_tables2 as tables
from django_tables2.utils import A
from .models import PrestamoArticulo
from .models import PrestamoEspacio


class PrestamosArticulosTable(tables.Table):
    class Meta:
        model = PrestamoArticulo
        template_name = 'django_tables2/bootstrap-responsive.html'


class PrestamosEspaciosTable(tables.Table):
    class Meta:
        model = PrestamoEspacio
        template_name = 'django_tables2/bootstrap-responsive.html'

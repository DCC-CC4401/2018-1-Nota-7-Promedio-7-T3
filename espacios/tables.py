import django_tables2 as tables
from django_tables2.utils import A
from .models import Espacios


class EspaciosTable(tables.Table):
    '''
    ESTADOS_ESP = tables.LinkColumn('espacios-detail', args=[A('pk')])
    estado_espacio = tables.LinkColumn('espacios-detail', args=[A('pk')])
    nombre_espacio = tables.LinkColumn('espacios-detail', args=[A('pk')])
    descripcion_espacio = tables.LinkColumn('espacios-detail', args=[A('pk')])
    id_espacio = tables.LinkColumn('espacios-detail', args=[A('pk')])
    capacidad_espacio = tables.LinkColumn('espacios-detail', args=[A('pk')])
    foto_espacio = tables.LinkColumn('espacios-detail', args=[A('pk')])

    class Meta:
        model = Espacios
        fields = ('ESTADOS_ESP', 'estado_espacio',
                  'nombre_espacio', 'descripcion_espacio', 'id_espacio',
                  'capacidad_espacio', 'foto_espacio')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no Espacios matching the search criteria..."

    class Meta:
        model = Espacios
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

    '''

    Estado = tables.Column()
    Nombre = tables.Column()
    Descripción = tables.Column()
    Capacidad = tables.Column()
    Foto = tables.Column()

    class Meta:
        attrs = {'class': 'table'}
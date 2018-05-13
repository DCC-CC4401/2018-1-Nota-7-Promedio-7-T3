from django.shortcuts import render
from .models import Articulos
# Create your views here.


def id_articulo(request, id_articulo):
    articulo = Articulos.objects.get(id_articulo=id_articulo)
    nombre = articulo.nombre_articulo
    estado = articulo.ESTADOS_ART[articulo.estado_articulo-1][1]
    descripcion = articulo.descripcion_articulo
    foto = articulo.foto_articulo
    id_art = articulo.id_articulo
    context = {'nombre': nombre, 'estado': estado, 'descripcion': descripcion, 'foto': foto, 'id': id_art}
    return render(request, 'vista_articulos.html', context)

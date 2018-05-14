from django.shortcuts import render
from .models import Articulos
# Create your views here.


def id_articulo(request, id_articulo):
    articulo = Articulos.objects.get(pk=id_articulo)
    nombre = articulo.nombre_articulo
    estado = articulo.ESTADOS_ART[articulo.estado_articulo-1][1]
    descripcion = articulo.descripcion_articulo
    foto = articulo.foto_articulo
    id_art = articulo.id
    context = {'nombre': nombre, 'estado': estado, 'descripcion': descripcion, 'foto': foto, 'id': id_art}
    if 'modificar' in request.POST:
        return render(request, 'vista_articulos_admin_edit.html', context)
    if request.user.is_superuser | ('guardar' in request.POST):
        return render(request, 'vista_articulos_admin.html', context)
    else:
        return render(request, 'vista_articulos_usuarios.html', context)


from django.shortcuts import render
from .models import Articulos
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.utils import timezone
from django.conf import settings

def id_articulo(request, id_articulo):
    if ('guardar' in request.POST) & request.user.is_superuser:
        articulo = Articulos.objects.get(pk=request.POST.get("ident",""))
        articulo.nombre_articulo = request.POST.get("new_name","")
        articulo.descripcion_articulo = request.POST.get("new_descr","")
        if len(request.FILES) != 0:
            old_path = articulo.foto_articulo
            myfile = request.FILES['new_foto']
            fs = FileSystemStorage()
            new_path = settings.MEDIA_ROOT + "/uploads/fotos_articulos/"+articulo.nombre_articulo
            articulo.foto_articulo = fs.save(new_path,myfile)
            fs.delete(old_path)
        articulo.save()
    elif 'pedir' in request.POST:
        dtinicio = datetime.strptime(request.POST.get("finicio",""), '%Y-%m-%dT%H:%M')
        dtfin = datetime.strptime(request.POST.get("ffin",""), '%Y-%m-%dT%H:%M')
        dtinicio = timezone.make_aware(dtinicio, timezone.get_current_timezone())
        dtfin = timezone.make_aware(dtfin, timezone.get_current_timezone())
        articulo = Articulos.objects.get(pk=request.POST.get("ident", ""))
        query = ReservaArticulo(articulo=articulo,inicio=dtinicio,final=dtfin)
        query.save()
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    reservas = ReservaArticulo.objects.filter(articulo=articulo, final__lt=timezone.make_aware(datetime.today(),timezone.get_current_timezone()))
    nombre = articulo.nombre_articulo
    estado = articulo.ESTADOS_ART[articulo.estado_articulo-1][1]
    descripcion = articulo.descripcion_articulo
    foto = articulo.foto_articulo
    id_art = articulo.id
    lista_reservas=list(reservas)
    context = {'nombre': nombre, 'estado': estado, 'descripcion': descripcion, 'foto': foto, 'id': id_art, 'perfil': perfil, 'lista_reservas': lista_reservas}
    if request.user.is_superuser | ('guardar' in request.POST):
        return render(request, 'vista_articulos_admin.html', context)
    else:
        return render(request, 'vista_articulos_usuarios.html', context)

def editar(request, id_articulo):
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    nombre = articulo.nombre_articulo
    estado = articulo.ESTADOS_ART[articulo.estado_articulo - 1][1]
    descripcion = articulo.descripcion_articulo
    foto = articulo.foto_articulo
    id_art = articulo.id
    context = {'nombre': nombre, 'estado': estado, 'descripcion': descripcion, 'foto': foto, 'id': id_art, 'perfil': perfil}
    return render(request, 'vista_articulos_admin_edit.html', context)
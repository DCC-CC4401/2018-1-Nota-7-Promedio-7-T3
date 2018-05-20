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
        old_path = articulo.foto_articulo
        myfile = request.FILES['new_foto']
        fs = FileSystemStorage()
        new_path = settings.MEDIA_ROOT + "/uploads/fotos_articulos/"+articulo.nombre_articulo
        articulo.foto_articulo = fs.save(new_path,myfile)
        fs.delete(old_path)
        articulo.save()
    elif 'pedir' in request.POST:
        str_inicial = request.POST.get("finicio","")+" "+request.POST.get("hinicio","")
        str_final = request.POST.get("ffin","")+" "+request.POST.get("hfin","")
        dtinicio = datetime.strptime(str_inicial, '%Y-%m-%d %H:%M')
        dtfin = datetime.strptime(str_final, '%Y-%m-%d %H:%M')
        dtinicio = timezone.make_aware(dtinicio, timezone.get_current_timezone())
        dtfin = timezone.make_aware(dtfin, timezone.get_current_timezone())
        articulo = Articulos.objects.get(pk=request.POST.get("ident", ""))
        query = ReservaArticulo(articulo=articulo,inicio=dtinicio,final=dtfin)
        query.save()
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    nombre = articulo.nombre_articulo
    estado = articulo.ESTADOS_ART[articulo.estado_articulo-1][1]
    descripcion = articulo.descripcion_articulo
    foto = articulo.foto_articulo
    id_art = articulo.id
    context = {'nombre': nombre, 'estado': estado, 'descripcion': descripcion, 'foto': foto, 'id': id_art, 'perfil': perfil}
    if 'modificar' in request.POST:
        return render(request, 'vista_articulos_admin_edit.html', context)
    if request.user.is_superuser | ('guardar' in request.POST):
        return render(request, 'vista_articulos_admin.html', context)
    else:
        return render(request, 'vista_articulos_usuarios.html', context)


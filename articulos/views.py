from django.shortcuts import render
from .models import Articulos
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.utils import timezone
from django.conf import settings


def id_articulo(request, id_articulo):
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    if request.method == 'POST':#Si es post tenemos varios casos
        if ('guardar' in request.POST) & request.user.is_superuser:
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
            articulo = Articulos.objects.get(id=request.POST.get("ident", ""))
            query = ReservaArticulo(perfil=perfil, articulo=articulo, inicio=dtinicio, final=dtfin)
            query.save()
            #Retornar una respuesta
    reservas = ReservaArticulo.objects.filter(articulo=articulo, final__lt=timezone.make_aware(datetime.today(),timezone.get_current_timezone()))
    lista_reservas=list(reservas)
    estado = articulo.ESTADOS_ART[articulo.estado_articulo - 1][1]
    context = {'articulo': articulo, 'perfil': perfil, 'lista_reservas': lista_reservas, 'estado': estado}
    if request.user.is_superuser | ('guardar' in request.POST):
        return render(request, 'vista_articulos_admin.html', context)
    else:
        return render(request, 'vista_articulos_usuarios.html', context)

def editar(request, id_articulo):
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    estado = articulo.ESTADOS_ART[articulo.estado_articulo - 1][1]
    context = {'articulo': articulo, 'estado': estado, 'perfil': perfil}
    return render(request, 'vista_articulos_admin_edit.html', context)
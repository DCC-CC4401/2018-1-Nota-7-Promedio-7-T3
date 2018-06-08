from django.shortcuts import render
from .models import Articulos
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from django.core.files.storage import FileSystemStorage
from datetime import datetime,timedelta
from django.utils import timezone
from django.conf import settings
from .forms import ReservaForm
from django.http import HttpResponseRedirect

def id_articulo(request, id_articulo):
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    reservas = ReservaArticulo.objects.filter(articulo=articulo, final__lt=timezone.make_aware(datetime.today(), timezone.get_current_timezone()))
    #sorted(reservas,key=lambda reserva : ReservaArticulo.final)
    lista_reservas=list(reservas)
    estado = articulo.ESTADOS_ART[articulo.estado_articulo - 1][1]
    if request.user.is_superuser:
        if request.method == 'POST':
            if 'guardar' in request.POST:
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
        context = {'articulo': articulo, 'perfil': perfil, 'lista_reservas': lista_reservas, 'estado': estado}
        return render(request, 'articulos/vista_articulos_admin.html', context)
    else:
        if request.method == 'POST':
            if 'pedir' in request.POST:
                form = ReservaForm(request.POST)
                if form.is_valid():
                    query = ReservaArticulo(perfil=perfil, articulo=articulo, inicio=form.cleaned_data['inicio'], final=form.cleaned_data['fin'])
                    query.save()
                    return HttpResponseRedirect('/home/')


        else:
            form = ReservaForm()
        context = {'articulo': articulo, 'perfil': perfil, 'lista_reservas': lista_reservas, 'estado': estado, 'form': form}
        return render(request, 'articulos/vista_articulos_usuarios.html', context)




def editar(request, id_articulo):
    perfil = Perfil.objects.get(correo=request.user.id)
    articulo = Articulos.objects.get(pk=id_articulo)
    estado = articulo.ESTADOS_ART[articulo.estado_articulo - 1][1]
    reservas = ReservaArticulo.objects.filter(articulo=articulo, final__lt=timezone.make_aware(datetime.today(), timezone.get_current_timezone()))
    lista_reservas = list(reservas)
    context = {'articulo': articulo, 'estado': estado, 'perfil': perfil, 'lista_reservas': lista_reservas}
    return render(request, 'articulos/vista_articulos_admin_edit.html', context)
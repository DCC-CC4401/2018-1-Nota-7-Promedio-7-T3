from django.shortcuts import render,redirect
from .models import Articulos
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from .forms import ReservaForm
from django.http import HttpResponseRedirect


def id_articulo(request, id_articulo):
    if not request.user.is_authenticated:
        return redirect('/home/')
    else:
        perfil = Perfil.objects.get(correo=request.user.id)
        articulo = Articulos.objects.get(pk=id_articulo)
        reservas = ReservaArticulo.objects.filter(articulo=articulo, final__lt=timezone.make_aware(datetime.now(), timezone.get_current_timezone()))
        lista_reservas=list(reservas)
        lista_reservas.sort(key=lambda x: x.final, reverse=True)
        lista_reservas = lista_reservas[:10]
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
            context = {'articulo': articulo, 'perfil': perfil, 'lista_reservas': lista_reservas}
            return render(request, 'articulos/vista_articulos_admin.html', context)
        else:
            if request.method == 'POST':
                if 'pedir' in request.POST:
                    form = ReservaForm(request.POST)
                    if form.is_valid():
                        query = ReservaArticulo(perfil=perfil, articulo=articulo, inicio=form.cleaned_data['inicio'], final=form.cleaned_data['fin'])
                        query.save()
                        return HttpResponseRedirect('/exito/')
            else:
                form = ReservaForm()
            context = {'articulo': articulo, 'perfil': perfil, 'lista_reservas': lista_reservas, 'form': form}
            return render(request, 'articulos/vista_articulos_usuarios.html', context)


def editar(request, id_articulo):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('/home/')
    else:
        perfil = Perfil.objects.get(correo=request.user.id)
        articulo = Articulos.objects.get(pk=id_articulo)
        reservas = ReservaArticulo.objects.filter(articulo=articulo, final__lt=timezone.make_aware(datetime.today(), timezone.get_current_timezone()))
        lista_reservas=list(reservas)
        lista_reservas.sort(key=lambda x: x.final, reverse=True)
        lista_reservas = lista_reservas[:10]
        context = {'articulo': articulo, 'perfil': perfil, 'lista_reservas': lista_reservas}
        return render(request, 'articulos/vista_articulos_admin_edit.html', context)


def exito(request):
    return render(request, 'Layouts/exito.html')

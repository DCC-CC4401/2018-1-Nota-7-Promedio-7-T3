from django.shortcuts import render
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from reservas.models import ReservaEspacio
from prestamos.models import PrestamoArticulo
from prestamos.models import PrestamoEspacio
from django.http import HttpResponseRedirect


def reservas(request):
    perfil = Perfil.objects.get(correo=request.user.id)
    reservas_articulos = ReservaArticulo.objects.filter(estado_reserva=1)
    reservas_espacios = ReservaEspacio.objects.filter(estado_reserva=1)
    prestamos_articulos = PrestamoArticulo.objects.all()
    prestamos_espacios = PrestamoEspacio.objects.all()
    lista_reservas = list(reservas_articulos)+list(reservas_espacios)
    lista_prestamos = list(prestamos_articulos)+list(prestamos_espacios)
    lista_reservas.sort(key=lambda x: x.inicio)
    lista_prestamos.sort(key=lambda x: x.reserva.inicio)
    if request.method == 'POST':
        if 'todos' in request.POST:
            prestamos_articulos = PrestamoArticulo.objects.all()
            prestamos_espacios = PrestamoEspacio.objects.all()
            lista_prestamos = list(prestamos_articulos) + list(prestamos_espacios)
            context = {'perfil': perfil, 'lista_reservas': lista_reservas, 'lista_prestamos': lista_prestamos}
            return render(request, 'admin_landing/admin_reservas.html', context)
        elif 'filtro' in request.POST:
            prestamos_articulos = PrestamoArticulo.objects.filter(estado_reserva=request.POST.get("filtro",""))
            prestamos_espacios = PrestamoEspacio.objects.filter(estado_reserva=request.POST.get("filtro",""))
            lista_prestamos = list(prestamos_articulos) + list(prestamos_espacios)
            context = {'perfil': perfil, 'lista_reservas': lista_reservas, 'lista_prestamos': lista_prestamos}
            return render(request, 'admin_landing/admin_reservas.html', context)
        elif 'entregar' in request.POST:
            presionados = request.POST.getlist('checks[]')
            for marcado in presionados:
                reserva=ReservaArticulo.objects.get(pk=marcado)
                reserva.estado_reserva = 2
                query = PrestamoArticulo(reserva=reserva, administrador=perfil, estado_reserva=1)
                query.save()
                reserva.save()
                return HttpResponseRedirect('/administracion/reservas/')
        elif 'rechazar' in request.POST:
            presionados = request.POST.getlist('checks[]')
            for marcado in presionados:
                reserva=ReservaArticulo.objects.get(pk=marcado)
                reserva.estado_reserva = 3
                reserva.save()
                return HttpResponseRedirect('/administracion/reservas/')
    else:
        context = {'perfil': perfil, 'lista_reservas': lista_reservas, 'lista_prestamos': lista_prestamos}
        return render(request, 'admin_landing/admin_reservas.html', context)

def grilla(request):
    return render(request, 'admin_landing/admin_grilla.html')
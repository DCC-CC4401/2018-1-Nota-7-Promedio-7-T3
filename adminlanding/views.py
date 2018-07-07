from django.shortcuts import render, redirect
from datetime import date
from datetime import timedelta
from datetime import datetime
from espacios.models import Espacios
from userprofile.models import Perfil
from reservas.models import ReservaArticulo
from reservas.models import ReservaEspacio
from prestamos.models import PrestamoArticulo
from prestamos.models import PrestamoEspacio
from django.http import HttpResponseRedirect

def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.

    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + timedelta(5)

    return (start_date, end_date)

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
                info = marcado.split(" ")
                if 'ReservaArticulo' in info:
                    reserva = ReservaArticulo.objects.get(pk=info[0])
                    reserva.estado_reserva = 2
                    query = PrestamoArticulo(reserva=reserva, administrador=perfil, estado_reserva=1)
                    query.save()
                    reserva.save()
                else:
                    reserva = ReservaEspacio.objects.get(pk=info[0])
                    reserva.estado_reserva = 2
                    query = PrestamoEspacio(reserva=reserva, administrador=perfil, estado_reserva=1)
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
    if not request.user.is_authenticated:
        return redirect('/home/')

    todo_espacios = Espacios.objects.all()

    reservas = ReservaEspacio.objects.all()
    delta = request.GET.get("delta")
    if not delta:
        delta = 0

    delta = int(delta)
    today = date.today()
    today_day = today.strftime("%A")

    mon = week_range(today)[0] + timedelta(days=(1 + 7 * delta))
    tue = mon + timedelta(days=1)
    wed = tue + timedelta(days=1)
    thu = wed + timedelta(days=1)
    fri = thu + timedelta(days=1)

    semana = "Semana del lunes " + str(mon.day) + "/" + str(mon.month) + "/" + str(mon.year)

    seleccion = request.GET.get("espacio")
    if seleccion and seleccion != "0":
        espacio_seleccionado = todo_espacios.get(id=seleccion)
    else:
        espacio_seleccionado = todo_espacios.first()

    reservas = reservas.filter(espacio=espacio_seleccionado)

    reservas_mon = reservas.filter(inicio__day=mon.day).filter(inicio__month=mon.month).filter(inicio__year=mon.year)
    reservas_tue = reservas.filter(inicio__day=tue.day).filter(inicio__month=tue.month).filter(inicio__year=tue.year)
    reservas_wed = reservas.filter(inicio__day=wed.day).filter(inicio__month=wed.month).filter(inicio__year=wed.year)
    reservas_thu = reservas.filter(inicio__day=thu.day).filter(inicio__month=thu.month).filter(inicio__year=thu.year)
    reservas_fri = reservas.filter(inicio__day=fri.day).filter(inicio__month=fri.month).filter(inicio__year=fri.year)

    perfil = Perfil.objects.get(correo=request.user.id)

    context = {'espacios': todo_espacios, 'seleccionado': espacio_seleccionado, 'deltaPlus': delta + 1,
               'deltaSub': delta - 1, 'semana': semana, 'lunes': reservas_mon, 'martes': reservas_tue,
               'miercoles': reservas_wed, 'jueves': reservas_thu, 'viernes': reservas_fri, 'perfil': perfil}

    return render(request, 'admin_landing/admin_grilla.html', context)
from django.shortcuts import render
from datetime import date
from datetime import timedelta
from datetime import datetime
from articulos.models import Articulos
from reservas.models import ReservaArticulo
from reservas.models import ReservaEspacio
from espacios.models import Espacios
from .forms import BusquedaForm
from django.db.models import Q


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


def busqueda(request):
    nombre = ""
    resultados = Articulos.objects.all()
    reservas = ReservaArticulo.objects.all()

    search_name = request.GET.get("nombre")
    if search_name:
        nombre = search_name
        resultados = resultados.filter(nombre_articulo__icontains=search_name)

    search_status = request.GET.get("estado")
    if search_status and search_status != '0':
        resultados = resultados.filter(estado_articulo=search_status)

    search_date_st = request.GET.get("fechaInicio")
    search_date_fn = request.GET.get("fechaFin")

    if search_date_fn and search_date_st:
        search_date_st = datetime.strptime(search_date_st, "%d/%m/%Y %H:%M").date()
        search_date_fn = datetime.strptime(search_date_fn, "%d/%m/%Y %H:%M").date()
        reservas = reservas.filter(
            Q(inicio__range=(search_date_st, search_date_fn)) | Q(final__range=(search_date_st, search_date_fn)))
        for res in reservas:
            resultados = resultados.exclude(id=res.articulo.id)

    search_id = request.GET.get("id")
    if search_id:
        resultados = Articulos.objects.all().filter(id=search_id)

    form = BusquedaForm()

    context = {'resultados': resultados, 'nombre': nombre, 'fecha_in': search_date_st, 'fecha_fn': search_date_fn,
               'reservas': reservas, 'form': form}
    return render(request, 'busqueda_articulos.html', context)


def espacios(request):
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

    context = {'espacios': todo_espacios, 'seleccionado': espacio_seleccionado, 'deltaPlus': delta + 1,
               'deltaSub': delta - 1, 'semana': semana, 'lunes': reservas_mon, 'martes': reservas_tue,
               'miercoles': reservas_wed, 'jueves': reservas_thu, 'viernes': reservas_fri}

    return render(request, 'busqueda_espacios/busqueda_espacios.html', context)

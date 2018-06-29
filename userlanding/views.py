from django.shortcuts import render
from datetime import date
from datetime import timedelta
from articulos.models import Articulos
from reservas.models import ReservaArticulo
from espacios.models import Espacios
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

    search_date_st = request.GET.get("fecha-inicio")
    search_date_fn = request.GET.get("fecha-fin")

    if search_date_fn and search_date_st:
        reservas = reservas.filter(
            Q(inicio__range=(search_date_st, search_date_fn)) | Q(final__range=(search_date_st, search_date_fn)))
        for res in reservas:
            resultados = resultados.exclude(id=res.articulo.id)

    context = {'resultados': resultados, 'nombre': nombre, 'fecha_in': search_date_st, 'fecha_fn': search_date_fn,
               'reservas': reservas}
    return render(request, 'busqueda_articulos.html', context)


def espacios(request):

    todo_espacios = Espacios.objects.all()
    delta = request.GET.get("delta")
    if not delta:
        delta = 0

    delta = int(delta)
    today = date.today()
    today_day = today.strftime("%A")

    monday = week_range(today)[0] + timedelta(days=(1 + 7*delta))
    friday = week_range(today)[1] + timedelta(days=7*delta)

    print("Hoy es", today_day)
    print("Lunes", monday.day, "del", monday.month)
    print("Viernes", friday.day, "del", friday.month)

    semana = "Semana del lunes " + str(monday.day)+"/"+str(monday.month)+"/"+str(monday.year)

    seleccion = request.GET.get("espacio")
    if seleccion:
        espacio_seleccionado = todo_espacios.get(id=seleccion)
    else:
        espacio_seleccionado = todo_espacios.first()

    context = {'espacios': todo_espacios, 'seleccionado': espacio_seleccionado, 'deltaPlus': delta+1, 'deltaSub': delta-1, 'semana': semana}

    return render(request, 'busqueda_espacios/busqueda_espacios.html', context)

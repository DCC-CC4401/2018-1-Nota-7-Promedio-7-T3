from django.shortcuts import render
from articulos.models import Articulos
from reservas.models import ReservaArticulo
from django.db.models import Q


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
    return render(request, 'busqueda_espacios.html')

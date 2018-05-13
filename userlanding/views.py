from django.shortcuts import render
from articulos.models import Articulos


def busqueda(request):

    resultados = Articulos.objects.all()

    search_name = request.GET.get("nombre")
    if search_name:
        resultados = resultados.filter(nombre_articulo__icontains=search_name)

    search_status = request.GET.get("estado")
    if search_status and search_status != '0':
        resultados = resultados.filter(estado_articulo=search_status)

    context = {'resultados' : resultados}
    return render(request, 'busqueda_articulos.html', context)
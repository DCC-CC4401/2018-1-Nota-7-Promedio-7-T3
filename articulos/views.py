from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def id_articulo(request, id_articulo):
    return HttpResponse("Hello, world. You're record is: "+str(id_articulo))
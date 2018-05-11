from django.shortcuts import render

# Create your views here.

def perfilUsuario(request):
    return render(request, 'vista_perfil.html')
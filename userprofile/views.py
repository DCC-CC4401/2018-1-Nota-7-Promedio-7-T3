from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from userprofile.forms import SignUpForm
from userprofile.models import Perfil
from userlanding.views import busqueda
from django.contrib.auth import views as auth_views
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def perfilUsuario(request):
    perfil = Perfil.objects.get(correo=request.user.id)
    context ={'perfil': perfil}
    return render(request, 'vista_perfil.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.perfil.nombre = form.cleaned_data.get('nombre')
            user.perfil.rut = form.cleaned_data.get('rut')
            user.save()
            return redirect('/exito/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return busqueda(request)
    else:
        return auth_views.login(request)

def redirectToHome(request):
    return redirect('/home/')
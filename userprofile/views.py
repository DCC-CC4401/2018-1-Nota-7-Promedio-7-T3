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
from reservas.models import ReservaArticulo
from prestamos.models import PrestamoArticulo

# Create your views here.

def perfilUsuario(request):

    if request.method == 'POST':
        if 'borrar' in request.POST:
            ReservaArticulo.objects.filter(pk=request.POST.get("id", "")).delete()


    perfil = Perfil.objects.get(correo=request.user.id)
    reservas = ReservaArticulo.objects.filter(perfil__correo=perfil.correo).order_by('inicio')
    lista_reservas = list(reservas)
    prestamos = PrestamoArticulo.objects.filter(reserva__perfil__correo=perfil.correo).order_by('reserva__inicio')
    lista_prestamos = list(prestamos)
    context ={'perfil': perfil, 'reservas': lista_reservas, 'prestamos':lista_prestamos}
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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
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
    return redirect('home')
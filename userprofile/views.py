from django.shortcuts import render, redirect
from userprofile.forms import SignUpForm
from userprofile.models import Perfil
from userlanding.views import busqueda
from adminlanding.views import reservas
from django.contrib.auth import views as auth_views
from reservas.models import ReservaArticulo
from reservas.models import ReservaEspacio
from prestamos.models import PrestamoArticulo
from prestamos.models import PrestamoEspacio
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect



def perfilUsuario(request):
    if request.method == 'POST':
        if 'borrar' in request.POST:
            ReservaArticulo.objects.filter(pk=request.POST.get("id", "")).delete()


    perfil = Perfil.objects.get(correo=request.user.id)
    reservasArticulos = ReservaArticulo.objects.filter(perfil__correo=perfil.correo).order_by('inicio')
    reservasEspacios = ReservaEspacio.objects.filter(perfil__correo=perfil.correo).order_by('inicio')
    lista_reservas = list(reservasArticulos) + list(reservasEspacios)
    lista_reservas = sorted(lista_reservas, key=lambda x: x.inicio)[0:10][::-1]
    prestamosArticulos = PrestamoArticulo.objects.filter(reserva__perfil__correo=perfil.correo).order_by('reserva__inicio')
    prestamosEspacios = PrestamoEspacio.objects.filter(reserva__perfil__correo=perfil.correo).order_by('reserva__inicio')
    lista_prestamos = list(prestamosArticulos) + list(prestamosEspacios)
    lista_prestamos = sorted(lista_prestamos, key=lambda x: x.reserva.inicio)[0:10][::-1]
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
            return redirect('/exito/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return reservas(request)
        else:
            return busqueda(request)
    else:
        return auth_views.login(request)


def redirectToHome(request):
    return redirect('/home/')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
"""Tarea3IS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articulos import views
from userlanding import views as user_views
from adminlanding import views as admin_views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.conf import settings
from userprofile import views as userprofileviews
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/busqueda/', user_views.busqueda, name='nombre_articulo'),
    path('user/espacios', user_views.espacios),
    path('administracion/reservas/', admin_views.reservas),
    path('administracion/grilla', admin_views.grilla),
    path('articulos/<int:id_articulo>/', views.id_articulo, name='id_articulo'),
    path('articulos/<int:id_articulo>/edit', views.editar, name='id_articulo'),
    path('exito/', views.exito),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('perfil/', userprofileviews.perfilUsuario, name = 'perfilUsuario'),
    path('register/', userprofileviews.signup, name = 'register'),
    path('home/', userprofileviews.index, name = 'home'),
    path('', userprofileviews.redirectToHome),
    path('change_password/', userprofileviews.change_password, name='change_password'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




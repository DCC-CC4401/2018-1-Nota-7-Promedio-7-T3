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
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.conf import settings
from userprofile import views as userprofileviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/busqueda/', user_views.busqueda, name='nombre_articulo'),
    path('articulos/<int:id_articulo>/', views.id_articulo, name='id_articulo'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('perfil/', userprofileviews.perfilUsuario, name = 'perfilUsuario'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
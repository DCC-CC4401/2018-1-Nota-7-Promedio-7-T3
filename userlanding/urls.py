from django.urls import path
from . import views

urlpatterns = [
    path('/busqueda/', views.busqueda),
    path('/espacios/', views.espacios),
]
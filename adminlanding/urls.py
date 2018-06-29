from django.urls import path
from . import views

urlpatterns = [
    path('/reservas/', views.reservas),
    path('/grilla/', views.grilla),
]
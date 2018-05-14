from django.urls import path
from . import views

urlpatterns = [
    path('/<int:id_articulo>/', views.id_articulo, name='id_articulo'),
    path('/<int:id_articulo>/edit', views.modificar, name='editar'),
]
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", curso),
    path("familiares/", familiares, name='familiares '),
    path("", inicio, name='inicio'),
    path("estudiantes/", estudiantes, name='estudiantes'),
    path("entregables/", entregables, name='entregables'),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("busquedaModelo/", busquedaModelo, name="busquedaModelo"),
    path("vehiculos/", vehiculos, name="vehiculos"),
    path("mascotas/", mascotas, name="mascotas"),
    path("vestimenta/", vestimenta, name="vestimenta"),
    path("busqueda/", busqueda, name="busqueda"),

]
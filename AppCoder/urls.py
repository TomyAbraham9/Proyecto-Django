from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", curso),
    path("familiares/", familiares, name='familiares '),
    path("", inicio, name='inicio'),
    path("estudiantes/", estudiantes, name='estudiantes'),
    path("cursos/", cursos, name='cursos'),
    path("profesores/", profesores, name='profesores'),
    path("entregables/", entregables, name='entregables'),
    
]

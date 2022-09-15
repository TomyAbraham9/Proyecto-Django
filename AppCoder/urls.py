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
    path("leerProfesores/", leerProfesores, name="leerProfesores"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),

    ### CBV ###

    path("estudiante/list/", EstudianteList.as_view(), name="estudiante_listar"),
    path("estudiante/<pk>", EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path("estudiante/nuevo/", EstudianteCreacion.as_view(), name="estudiante_crear"),
    path("estudiante/editar/<pk>", EstudianteUpdate.as_view(), name="estudiante_editar"),
    path("estudiante/borrar/<pk>", EstudianteDelete.as_view(), name="estudiante_borrar"),


]
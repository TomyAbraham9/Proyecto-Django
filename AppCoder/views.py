from http.client import HTTPResponse
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso=Curso(nombre="JS" , comision=24800)
    curso.save()
    texto=f"Curso creado, nombre del curso: {curso.nombre}. Numero de comision: {curso.comision}"
    return HttpResponse(texto)


from http.client import HTTPResponse
from django.shortcuts import render
from .models import Curso , Familiares
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def curso(request):
    curso=Curso(nombre="JS" , comision=24800)
    curso.save()
    texto=f"Curso creado, nombre del curso: {curso.nombre}. Numero de comision: {curso.comision}"
    return HttpResponse(texto)

def familiares(request):
    familiar_1=Familiares(nombre="Rosana" , apellido= "Sanchez" , edad=54 , nacimiento= "1968-1-22")
    familiar_2=Familiares(nombre="Jose Luis" , apellido= "Abraham" , edad=57 , nacimiento= "1965-3-3")
    familiar_3=Familiares(nombre="Joaquin" , apellido= "Febre" , edad=17 , nacimiento= "2004-6-13")
    familiar_4=Familiares(nombre="Matias" , apellido= "Garcia" , edad=18 , nacimiento= "2003-10-23")
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    familiar_4.save()
    datos1=f" Nombre completo: {familiar_1.nombre} {familiar_1.apellido}. Edad: {familiar_1.edad}. Fecha de nacimiento: {familiar_1.nacimiento}."
    datos2=f" Nombre completo: {familiar_2.nombre} {familiar_2.apellido}. Edad: {familiar_2.edad}. Fecha de nacimiento: {familiar_2.nacimiento}."
    datos3=f" Nombre completo: {familiar_3.nombre} {familiar_3.apellido}. Edad: {familiar_3.edad}. Fecha de nacimiento: {familiar_3.nacimiento}."
    datos4=f" Nombre completo: {familiar_4.nombre} {familiar_4.apellido}. Edad: {familiar_4.edad}. Fecha de nacimiento: {familiar_4.nacimiento}."
    diccionario={"datos_1": datos1 , "datos_2": datos2 , "datos_3": datos3 , "datos_4": datos4}
    plantilla=loader.get_template("template2.html")
    texto=plantilla.render(diccionario)
    return HttpResponse(texto)

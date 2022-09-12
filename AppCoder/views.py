from http.client import HTTPResponse
from django.shortcuts import render
from .models import Curso , Familiares, Mascotas , Profesor, Vehiculo, Vestimenta
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import CursoForm, ProfeForm, VehiculoForm, VestimentaForm, MascotaForm

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
    return HttpResponse("texto")


def inicio(request):
    return render (request, "AppCoder/inicio.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def cursos(request):
    return render (request, "AppCoder/cursos.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")

"""def cursoFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")
    else:
        return render (request, "AppCoder/cursoFormulario.html")
"""

def cursos(request):
    if request.method == "POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso=Curso(nombre=nombre , comision=comision)
            curso.save()
            return render (request, "AppCoder/inicio.html")


    else:
        formulario=CursoForm()
        return render (request, "AppCoder/cursos.html" , {"formulario": formulario})


def profesores(request):
    if request.method == "POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profe = Profesor(nombre=nombre , apellido=apellido , email=email , profesion=profesion)
            profe.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form= ProfeForm()
        return render(request, "AppCoder/profesores.html", {"formulario":form})

def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):

    if request.GET["comision"]:
        comision=request.GET["comision"]
        cursos=Curso.objects.filter(comision=comision)
        return render (request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos})

    else:
        return render (request, "AppCoder/busquedaComision.html", {"mensaje":"Ingrese una comision"})


def vehiculos(request):
    if request.method == "POST":
        form=VehiculoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            tipo=info["tipo"]
            marca=info["marca"]
            modelo=info["modelo"]
            vehiculo = Vehiculo(tipo=tipo , marca=marca , modelo=modelo)
            vehiculo.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form= VehiculoForm()
        return render (request, "AppCoder/vehiculos.html", {"formulario":form})

def mascotas(request):
    if request.method == "POST":
        form=MascotaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            tipo=info["tipo"]
            edad=info["edad"]
            mascota = Mascotas(nombre=nombre , tipo=tipo , edad=edad)
            mascota.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form= MascotaForm()
        return render (request, "AppCoder/mascotas.html", {"formulario":form})

def vestimenta(request):
    if request.method == "POST":
        form=VestimentaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            tipo=info["tipo"]
            material=info["material"]
            marca=info["marca"]
            vestimenta = Vestimenta(tipo=tipo , material=material , marca=marca)
            vestimenta.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form= VestimentaForm()
        return render (request, "AppCoder/vestimenta.html", {"formulario":form})

def busquedaModelo(request):
    return render(request, "AppCoder/busquedaModelo.html")

def busqueda(request):
    modelo=request.GET["modelo"]
    modelos=Vehiculo.objects.filter(modelo=modelo)
    return render(request, "AppCoder/resultadoModelo.html" , {"modelos":modelos})


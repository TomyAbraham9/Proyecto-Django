from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfeForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)

class VehiculoForm(forms.Form):
    tipo= forms.CharField(max_length=50)
    marca= forms.CharField(max_length=50)
    modelo= forms.IntegerField()

class MascotaForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    tipo= forms.CharField(max_length=50)
    edad= forms.IntegerField()

class VestimentaForm(forms.Form):
    tipo= forms.CharField(max_length=50)
    material= forms.CharField(max_length=50)
    marca= forms.CharField(max_length=50)


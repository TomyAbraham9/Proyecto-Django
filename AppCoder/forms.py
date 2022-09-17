from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Perfil, Inmueble

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control text-center'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control text-center'})
    )

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('tipo_usuario','rut','direccion','cuidad','telefono', 'correo' )

class InmuebleForm(forms.ModelForm):
    #id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class Meta:

        model = Inmueble
        fields = (
            'id_tipo_inmueble','id_comuna','id_region', 
            'nombre_inmueble', 'm2_construido', 'numero_banos', 
            'numero_hab','direccion', 'descripcion'
            )   #registra todos los campos disponibles

        labels = {
            'id_tipo_inmueble':'Tipo de Inmueble',
            'id_comuna':'Comuna',
            'id_region':'Region', 
            'nombre_inmueble':'Nombre Inmueble',
            'm2_construido':'Metros cuadrados construidos', 
            'numero_banos':'Numero de Baños', 
            'numero_hab':'Numero de habitaciones',
            'direccion':'Direccion',
            'descripcion':'Descripcion',
            }   #registra todos los campos disponibles

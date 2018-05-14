from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(help_text='Requerido')
    rut = forms.CharField(help_text='Requerido: sin puntos ni guion')

    class Meta:
        model = User
        fields = ('username', 'nombre', 'rut', 'password1', 'password2', )
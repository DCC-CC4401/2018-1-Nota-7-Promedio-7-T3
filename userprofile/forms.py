from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(help_text='Requerido')
    rut = forms.IntegerField(label= "RUT", help_text='Requerido: sin puntos ni guion')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Su contraseña no puede asemejarse tanto a su otra información personal. "\
                                             "Su contraseña debe contener al menos 8 caracteres. " \
                                             "Su contraseña no puede ser completamente numérica."

    class Meta:
        model = User
        fields = ('username', 'nombre', 'rut', 'password1', 'password2',)
        labels = {
            'username': "Correo (Nombre de usuario)",
        }

        widgets = {
            'username': forms.EmailInput(),
            'rut': forms.NumberInput(),
        }


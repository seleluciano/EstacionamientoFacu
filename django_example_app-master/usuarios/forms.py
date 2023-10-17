from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class ClienteCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cliente
        fields = UserCreationForm.Meta.fields + ('nombre','apellido','DNI','telefono','username','password')


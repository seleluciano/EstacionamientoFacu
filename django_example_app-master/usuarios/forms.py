from django import forms
from .models import Cliente

class ClienteCreationForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','DNI','telefono','username','password')


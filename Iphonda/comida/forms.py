from django import forms
from .models import Comida , Categoria

class Nueva_Categoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','descripcion']

class Nueva_Comida(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre','descripcion','imagen','precio','categoria']

from django import forms
from .models import Categoria

class Nueva_Categoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','descripcion']

from django import forms
from .models import Comida , Categoria

class Nueva_Comida(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre','descripcion','imagen','precio','categoria']

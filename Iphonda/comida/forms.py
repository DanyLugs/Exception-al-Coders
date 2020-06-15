from django import forms
from .models import Comida , Categoria
from usuarios.models import *

class Nueva_Categoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','descripcion','imagen']
        widgets = {
            'nombre' : forms.TextInput(
            attrs={'class' : 'form-group' , 'placeholder' : 'Sopa , ..'}
            ),
            'descripcion' : forms.TextInput(
            attrs={'class' : 'form-group' , 'placeholder' : 'Esta mojada'}
            )}

class Nueva_Comida(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre','descripcion','imagen','precio','categoria']
        widgets = {
            'nombre' : forms.TextInput(
            attrs={'class' : 'form-group' , 'placeholder' : 'Caldito de pollo , ..'}
            ),
            'descripcion' : forms.TextInput(
            attrs={'class' : 'form-group' , 'placeholder' : 'Justo como el de mama'}
            ),
            }

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    """
    Form para que el usuario elija la cantidad del prodcuto
    cantidadComida: permite al usuario elegir entre 1 - 20, usa TypeChoiceField con coerce = int para
            convertir el input del usuario a int.

    update: (False) = permite indicar si la cantidad debe ser agregada a una cantidad ya existente en el carrito para ese producot
            (True) = la cantidad existente debe ser actualizada con la cantidad dada por el usuario
    """
    model = cantidadComidaOrden
    cantidadComida = forms.TypedChoiceField(
                                choices = PRODUCT_QUANTITY_CHOICES,
                                coerce = int)
    update = forms.BooleanField(required = False,
                                initial = False,
                                widget = forms.HiddenInput()) # No queremos que el usuario vea el campo update

    class Meta:
        fields = ('cantidad','update')
        labels = {
            'cantidad' : ('Cantidad'),
            'update':(''),
        }                            

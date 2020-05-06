from django import forms
from .models import Comida , Categoria

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


def editarComida(request, comida_id):
    comidaMod=Comida.objects.get(id=comida_id)
    form=Nueva_Comida(instance=comidaMod)
    if(request.method=='POST'):
        form =Nueva_Comida(request.POST, instance=comidaMod)
        if(form.is_valid()):
            comidaMod=form.save(commit=False)
            comidaMod.save()
    return render(request,"editarComida",{'form':form})

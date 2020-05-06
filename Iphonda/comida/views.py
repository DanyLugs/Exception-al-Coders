"""Views de Comida."""
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

#Models
from .models import Comida, Categoria

#Forms
from .forms import Nueva_Categoria, Nueva_Comida

# Create your views here.
class ComidaVista(View):

    template = "comida/vercomida.html"

    def get(self, request, categoryName):
        """GET method."""
        id = Categoria.objects.filter(slug = categoryName).first()
        comidas = Comida.objects.filter(categoria = id)
        print(id)
        context = {"comidas": comidas}
        return render(request, self.template, context)

class AgregarCategoria(View):

    template ="categoria/agregar_categoria.html"

    def get(self,request):
        form = Nueva_Categoria()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = Nueva_Categoria(request.POST, request.FILES)

        try:
            if form.is_valid():
                categoria_nueva = form.save(commit=False)
                categoria_nueva.save()
                messages.success(request, 'Categoria Agregada !')

            context = {"form": form}
            return render(request, self.template, context)
        except:
            messages.success(request, 'Hubo un error agregando la Categoria')
            context = {"form": form}
            return render(request, self.template, context)

class AgregarComida(View):

    template ="comida/agregar_comida.html"

    def get(self,request):
        form = Nueva_Comida()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = Nueva_Comida(request.POST, request.FILES)

        try:
            if form.is_valid():
                comida_nueva = form.save(commit=False)
                comida_nueva.save()
                messages.success(request, 'Comida Agregada !')

            context = {"form": form}
            return render(request, self.template, context)
        except:
            messages.success(request, 'Hubo un error agregando la Comida')
            context = {"form": form}
            return render(request, self.template, context)


class CategoriaVista(View):

    template = "comida/vercategorias.html"

    def get(self, request):
        """GET method."""
        categorias = Categoria.objects.all()
        context = {"categorias": categorias}
        return render(request, self.template, context)

class EliminarComida(View):

    def get(self,request,comida_id):
        print("Si llego aqui")
        comidaMod=Comida.objects.get(id=comida_id)
        categoria=comidaMod.categoria
        url="/comida/categorias/"+str(categoria)+"/"
        comidaMod.delete()
        print(url)
        return redirect(url)




def editarComida(request, comida_id):
    comidaMod=Comida.objects.get(id=comida_id)
    form=Nueva_Comida(instance=comidaMod)
    if(request.method=='POST'):
        form =Nueva_Comida(request.POST, instance=comidaMod)
        if(form.is_valid()):
            comidaMod=form.save(commit=False)
            comidaMod.save()
    return render(request,"comida/editarComida.html",{'form':form})

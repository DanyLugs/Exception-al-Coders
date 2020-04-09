"""Views de Comida."""
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Categoria
from .forms import Nueva_Categoria

#Models
from comida.models import Comida

#Forms
from comida.forms import        #Cambiar por el nombre del form

# Create your views here.
class Comida(View):

    template = "comida/categorias/menu.html"

    def get(self, request):
        """GET method."""
        comida = Comida.objects.all()
        context = {"comida": comida}
        return render(request, self.template, context)

class AgregarCategoria(View):

    template ="categoria/agregar_categoria.html"

    def get(self,request):
        form = Nueva_Categoria()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):

        form = Nueva_Categoria(request.POST)

        if form.is_valid():
            categoria_nueva = form.save(commit=False)
            categoria_nueva.save()
            return HttpResponse("<h>AQui debe de ir la reedireccion a comida</h1>")

        context = {"form": form}
        return render(request, self.template, context)

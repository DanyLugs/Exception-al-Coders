"""Views de Comida."""
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

#Models
from comida.models import Comida
from .models import Categoria

#Forms
from .forms import Nueva_Categoria, Nueva_Comida



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
        form = Nueva_Comida(request.POST)

class AgregarComida(View):

    template ="comida/agregar_comida.html"

    def get(self,request):
        form = Nueva_Comida()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        form = Nueva_Comida(request.POST)
        if form.is_valid():
            comida_nueva = form.save(commit=False)
            comida_nueva.save()
            return HttpResponse("<h1>Artista Agregado21!</h1>")

        context = {"form": form}
        return render(request, self.template, context)

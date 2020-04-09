from django.shortcuts import render
from django.views import View
from .models import Categoria
from .forms import Nueva_Categoria
from django.http import HttpResponse

# Create your views here.
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

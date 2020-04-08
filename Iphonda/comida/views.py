"""Views de Comida."""
from django.shortcuts import render, redircet
from django.views import View
from django.http import HttpResponse

#Models
from comida.models import Categoria

#Forms
from comida.forms import CategoryForm       #Cambiar por el nombre del form

# Create your views here.
class Categoria(View)

    template = "comida/vercategorias.html"

    def get(self, request):
        """GET method."""
        categoria = Categoria.objects.all()
        context = {"categoria": categoria}
        return render(request, self.template, context)
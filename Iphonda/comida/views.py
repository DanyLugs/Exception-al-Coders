"""Views de Comida."""
from django.shortcuts import render, redircet
from django.views import View
from django.http import HttpResponse

#Models
from comida.models import Comida

#Forms
from comida.forms import FoodForm       #Cambiar por el nombre del form

# Create your views here.
class Comida(View)

    template = "comida/categorias/menu.html"

    def get(self, request):
        """GET method."""
        comida = Comida.objects.all()
        context = {"comida": comida}
        return render(request, self.template, context)
 



from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Orden
from django.template import loader
# Create your views here.

class Pedidos(View):
    """docstring forPedidos."""

    def get(self,request):
        template=loader.get_template("usuario/pedidos.html")
        lista_pedidos= Orden.objects.all()
        context={
        'lista_pedidos':lista_pedidos,
        }

        return render(request,"usuario/pedidos.html",context)
    def post(request):
        return HttpResponse("<h1> no debiste llegar aqui </h1>")
        pass

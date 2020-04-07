from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Pedidos(View):
    """docstring forPedidos."""
    template="usuario/pedidos.html"

    def get(self,request):
        context={}

        return render(request,self.template,context)

    def post(request):
        return HttpResponse("<h1> no debiste llegar aqui </h1>")
        pass
##Comentario solo para subirlo agit

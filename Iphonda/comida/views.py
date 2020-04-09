from django.shortcuts import render
from django.views import View
from .models import Comida
from .forms import Nueva_Comida
from django.http import HttpResponse

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

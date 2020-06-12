from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View
from django.template import loader
from django.http import HttpResponse

from .forms import SignUpForm
from .models import Orden
from .mixins import *

class Admin(LoginRequiredMixin,AdminMixin,View):
    """ Home del administrador """
    login_url = '/login/'

    def get(self, request):
        context = {
            "title": "Administrador"
        }
        return render(request, "admin-dashboard.html", context)

# Create your views here.
class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
            'title': 'Inicio de sesión'
        }
        return render(request, "login.html", context)

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username'],
        password = request.POST['password'],
        user = authenticate(request, username=username[0], password=password[0])

        context = {
            'form': form,
            'title': 'Inicio de sesión'
        }

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Falló la autenticación de usuario. Intenta ingresar nuevamente.')
            return render(request, "login.html", context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

class Pedidos(View):
    """docstring forPedidos."""

    def get(self,request):
        template = loader.get_template("pedidos.html")
        lista_pedidos = Orden.objects.all()
        pedidos=[]
        for pedido in lista_pedidos:
            lisCom=[]
            for comida in pedido.comida.all():
                lisCom.append(comida)
            diCo={
                "id": pedido.id,
                "fecha": pedido.fecha,
                "usuario":pedido.usuario,
                "comidas": lisCom
            }
            pedidos.append(diCo)


        context = {
            'lista_pedidos':lista_pedidos,
            'lista_comida':pedidos,
            "title": "Pedidos"
        }

        return render(request,"pedidos.html",context)

    def post(self, request):
        return HttpResponse("<h1> no debiste llegar aqui </h1>")


class Signup(View):
    def get(self, request):
        context = {
            'form': SignUpForm(),
            'title': 'Registro de usuarios'
        }
        return render(request, "signup.html", context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Clientes')

            user.groups.add(group)

            return redirect('/login/')

        context = {
            'form': form,
            'title': 'Registro de usuarios'
        }
        return render(request, "signup.html", context)

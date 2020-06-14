from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Orden,cantidadComidaOrden
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

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
        lista_cantidad =cantidadComidaOrden.objects.all()
        lista_entrega=Orden.objects.filter(estado="Preparando")
        cantidades=[]
        pedidos=[]
        for pedido in lista_entrega:
            lisCom=[]
            cantidad=cantidadComidaOrden.objects.filter(idOrden=pedido.id)
            diCo={
                "id": pedido.id,
                "fecha": pedido.fecha,
                "usuario":pedido.usuario,
                "comidas": cantidad,
                "estado": pedido.estado,
            }
            pedidos.append(diCo)
        context = {
            'lista_pedidos':pedidos,
            'lisCom':lista_cantidad,
            "title": "Pedidos",

        }
        return render(request,"pedidos.html",context)

    def post(self, request):
        return HttpResponse("<h1> no debiste llegar aqui </h1>")

class Pedidos_usuarios(View):
    """docstring forPedidos."""

    def get(self,request):
        lista_pedidos = Orden.objects.all()
        lista_cantidad =cantidadComidaOrden.objects.all()
        cantidades=[]
        pedidos=[]
        cliente=request.user
        print(cliente.id)
        historial=Orden.objects.filter(usuario=cliente.id)
        print(historial)
        #pedido_cliente=lista_pedidos.objects.filter(id=)
        for pedido in historial:
            lisCom=[]
            cantidad=cantidadComidaOrden.objects.filter(idOrden=pedido.id)
            diCo={
                "id": pedido.id,
                "fecha": pedido.fecha,
                "usuario":pedido.usuario,
                "comidas": cantidad,
                "estado": pedido.estado,
            }
            pedidos.append(diCo)


        context = {
            'lista_pedidos':pedidos,
            'lisCom':lista_cantidad,
            "title": "Pedidos",
        }

        return render(request,"pedido_cliente.html",context)

    def post(self, request):
        return HttpResponse("<h1> no debiste llegar aqui </h1>")


class Pedidos_repartidor(View):
    """docstring forPedidos."""
    def get(self,request):
        lista_cantidad =cantidadComidaOrden.objects.all()
        lista_entrega=Orden.objects.filter(estado="LT")
        cantidades=[]
        pedidos=[]
        for pedido in lista_entrega:
            lisCom=[]
            cantidad=cantidadComidaOrden.objects.filter(idOrden=pedido.id)
            diCo={
                "id": pedido.id,
                "fecha": pedido.fecha,
                "usuario":pedido.usuario,
                "comidas": cantidad,
                "estado": pedido.estado,
            }
            pedidos.append(diCo)
        context = {
            'lista_pedidos':pedidos,
            'lisCom':lista_cantidad,
            "title": "Pedidos",

        }
        return render(request,"pedidos_reapartidor.html",context)

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
            form.save()
            return redirect('/login/')

        context = {
            'form': form,
            'title': 'Registro de usuarios'
        }
        return render(request, "signup.html", context)

class Proceso(View):
    """docstring forProceso."""
    def get(self,request,ordenid):
        orden = Orden.objects.get(id = ordenid)
        orden.estado = 'LT'
        orden.save()
        return redirect( reverse_lazy('pedido_admin'))


class Entrega(View):
    """docstring forProceso."""
    def get(self,request,ordenid):
        orden = Orden.objects.get(id = ordenid)
        orden.estado = 'Entregado'
        orden.save()
        return redirect(reverse_lazy('pedido_rep') )

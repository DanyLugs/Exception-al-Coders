from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import SignUpForm
from .models import Orden,cantidadComidaOrden
from .mixins import *

class Admin(LoginRequiredMixin,AdminMixin,View):
    """ Home del administrador """
    login_url = '/login/'

    def get(self, request):
        context = {
            "title": "Administrador"
        }
        return render(request, "admin-dashboard.html", context)

class AgregarRepartidor(LoginRequiredMixin,AdminMixin,View):
    """ Vista para agregar un nuevo repartidor """
    login_url = '/login/'

    def get(self, request):

        context = {
            "repartidores": User.objects.filter(groups__name="repartidor"),
            "clientes": User.objects.filter(groups__name="cliente"),
            "title": "Agregar repartidor"
        }
        return render(request, "agregar-repartidor.html", context)

class AgregarRepartidorConId(AdminMixin,View):
    """ Actualiza el usuario con el id seleccionado para ser repartidor """

    def get(self, request, idUser):
        try:
            usuario = User.objects.get(id=idUser)
            grupoClientes = Group.objects.get(name="cliente")
            grupoRepartidores = Group.objects.get(name="repartidor")
            usuario.groups.remove(grupoClientes)
            usuario.groups.add(grupoRepartidores)
            msj = "Haz agregado a " + str(usuario.username) + " como repartidor."
            messages.add_message(request,messages.SUCCESS, msj)
        except:
            msj = "El usuario seleccionado es inválido o no existe."
            messages.add_message(request,messages.ERROR, msj)
        finally:
            return redirect('/admin')

class QuitarRepartidorConId(AdminMixin,View):
    """ Actualiza el usuario con el id seleccionado para ya no ser repartidor """

    def get(self, request, idUser):
        try:
            usuario = User.objects.get(id=idUser)
            grupoClientes = Group.objects.get(name="cliente")
            grupoRepartidores = Group.objects.get(name="repartidor")
            usuario.groups.add(grupoClientes)
            usuario.groups.remove(grupoRepartidores)
            msj = "Haz eliminado a " + str(usuario.username) + " como repartidor."
            messages.add_message(request,messages.SUCCESS, msj)
        except:
            msj = "El usuario seleccionado es inválido o no existe."
            messages.add_message(request,messages.ERROR, msj)
        finally:
            return redirect('/admin')

from .forms import SignUpForm
from .models import Orden
from .mixins import *

class Admin(LoginRequiredMixin,AdminMixin,View):
    """ Home del administrador """
    login_url = '/login/'

    def get(self, request):
        context = {
            "title": "Administrador",
            "grupo": str(request.user.groups.all().first())
        }
        return render(request, "admin-dashboard.html", context)

class AgregarRepartidor(LoginRequiredMixin,AdminMixin,View):
    """ Vista para agregar un nuevo repartidor """
    login_url = '/login/'


    def get(self, request):

        context = {
            "repartidores": User.objects.filter(groups__name="repartidor"),
            "clientes": User.objects.filter(groups__name="cliente"),
            "title": "Agregar repartidor"
        }
        return render(request, "agregar-repartidor.html", context)

class AgregarRepartidorConId(AdminMixin,View):
    """ Actualiza el usuario con el id seleccionado para ser repartidor """

    def get(self, request, idUser):
        try:
            usuario = User.objects.get(id=idUser)
            grupoClientes = Group.objects.get(name="cliente")
            grupoRepartidores = Group.objects.get(name="repartidor")
            usuario.groups.remove(grupoClientes)
            usuario.groups.add(grupoRepartidores)
            msj = "Haz agregado a " + str(usuario.username) + " como repartidor."
            messages.add_message(request,messages.SUCCESS, msj)
        except:
            msj = "El usuario seleccionado es inválido o no existe."
            messages.add_message(request,messages.ERROR, msj)
        finally:
            return redirect('/admin')

class CalificarServicio(View):
    def get(self, request, idOrden):
        orden = Orden.objects.get(id=idOrden)
        usuario = User.objects.get(id=orden.usuario_id)
        if orden.usuario_id != request.user.id:
            return redirect('/')
        return render(request, "calificar-servicio.html", {"title": "Calificar servicio"})

    def post(self, request, idOrden):
        orden = Orden.objects.get(id=idOrden)
        calif = int(request.POST['calif'])
        return None

class QuitarRepartidorConId(AdminMixin,View):
    """ Actualiza el usuario con el id seleccionado para ya no ser repartidor """

    def get(self, request, idUser):
        try:
            usuario = User.objects.get(id=idUser)
            grupoClientes = Group.objects.get(name="cliente")
            grupoRepartidores = Group.objects.get(name="repartidor")
            usuario.groups.add(grupoClientes)
            usuario.groups.remove(grupoRepartidores)
            msj = "Haz eliminado a " + str(usuario.username) + " como repartidor."
            messages.add_message(request,messages.SUCCESS, msj)
        except:
            msj = "El usuario seleccionado es inválido o no existe."
            messages.add_message(request,messages.ERROR, msj)
        finally:
            return redirect('/admin')

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
        lista_entrega=Orden.objects.filter(estado="PD")
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
                "dirrecion":pedido.dirr.dirrec
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
                "dirrecion":pedido.dirr.dirrec,
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
                "dirrecion":pedido.dirr.dirrec,
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
            user = form.save()
            group = Group.objects.get(name='cliente')

            user.groups.add(group)

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
        orden.estado = 'ET'
        orden.save()
        return redirect(reverse_lazy('pedido_rep') )

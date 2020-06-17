"""Views de Comida."""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.template.defaultfilters import slugify
import datetime
from django.views.decorators.http import require_POST
from usuarios.models import Orden, cantidadComidaOrden
from comida.models import Comida, Categoria
from .cart import Cart
from .forms import CartAddProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import *
from .forms import *
from .mixins import *

#Models
from .models import Comida, Categoria
from usuarios.models import cantidadComidaOrden, Orden

#Forms
from .forms import Nueva_Categoria, Nueva_Comida

# Create your views here.
class ComidaVista(View):

    template = "comida/vercomida.html"
    model = Comida
    login_url = 'users: login'

    def get(self, request, categoryName):
        """GET method."""
        id = Categoria.objects.filter(slug = categoryName).first()
        comidas = Comida.objects.filter(categoria = id)
        form = CartAddProductForm()
        print(id)
        context = {
            "comidas": comidas,
            "title": id.nombre,
            "form": form,
            "grupo": str(request.user.groups.all().first())
        }
        return render(request, self.template, context)

class AgregarCategoria(LoginRequiredMixin,AdminMixin,View):
    login_url = '/login/'
    redirect_url = '/comida/categorias/'

    template ="categoria/agregar_categoria.html"
    title = "Agregar categorías"

    def get(self,request):
        form = Nueva_Categoria()
        context = {
            "form": form,
            "title": self.title,
            "grupo": str(request.user.groups.all().first())
        }
        return render(request, self.template, context)

    def post(self, request):
        form = Nueva_Categoria(request.POST, request.FILES)

        try:
            if form.is_valid():
                categoria_nueva = form.save(commit=False)
                categoria_nueva.save()
                messages.success(request, 'Categoria Agregada !')
                context = {
                    "form": Nueva_Categoria(),
                    "title": self.title,
                    "grupo": str(request.user.groups.all().first())
                }
                return render(request, self.template, context)

            context = {
                "form": form,
                "title": self.title,
                "grupo": str(request.user.groups.all().first())
            }
            return render(request, self.template, context)
        except:
            messages.success(request, 'Hubo un error agregando la Categoria')
            context = {
                "form": form,
                "title": self.title,
                "grupo": str(request.user.groups.all().first())
            }
            return render(request, self.template, context)

class AgregarComida(LoginRequiredMixin,AdminMixin,View):
    login_url = '/login/'
    redirect_url = '/comida/categorias/'

    template ="comida/agregar_comida.html"
    title = "Agregar comida"

    def get(self,request):
        form = Nueva_Comida()
        context = {
            "form": form,
            "title": self.title,
            "grupo": str(request.user.groups.all().first())
        }

        return render(request, self.template, context)

    def post(self, request):
        form = Nueva_Comida(request.POST, request.FILES)

        try:
            if form.is_valid():
                comida_nueva = form.save(commit=False)
                comida_nueva.save()
                messages.success(request, 'Comida Agregada !')
                context = {
                    "form": Nueva_Comida(),
                    "title": self.title,
                    "grupo": str(request.user.groups.all().first())
                }
                return render(request, self.template, context)

            context = {
                "form": form,
                "title": self.title,
                "grupo": str(request.user.groups.all().first())
            }
            return render(request, self.template, context)

        except:
            messages.success(request, 'Hubo un error agregando la Comida')
            context = {
                "form": form,
                "title": self.title,
                "grupo": str(request.user.groups.all().first())
            }
            return render(request, self.template, context)


class CategoriaVista(View):

    template = "comida/vercategorias.html"

    def get(self, request):
        """GET method."""
        categorias = Categoria.objects.all()
        context = {
            "categorias": categorias,
            "title": "Explora nuestro menú",
            "grupo": str(request.user.groups.all().first())
        }
        return render(request, self.template, context)

class EliminarComida(View):
    def get(self,request,comida_id):
        comidaMod = Comida.objects.get(id=comida_id)
        categoria = slugify(comidaMod.categoria)
        url = "/comida/categorias/" + str(categoria) + "/"
        comidaMod.delete()
        return redirect(url)


class EliminarCategoria(View):
    def get(self,request,categoria_id):
        categoriaMod=Categoria.objects.get(id=categoria_id)
        url = "/comida/categorias/"
        categoriaMod.delete()
        return redirect(url)


class EditarComida(LoginRequiredMixin,AdminMixin,View):
    login_url = '/login/'
    redirect_url = '/comida/categorias/'

    def get(self, request, comida_id):
        comidaMod = Comida.objects.get(id = comida_id)
        form = Nueva_Comida(instance = comidaMod)
        context = {
            "form": form,
            "title": "Editar comida " + comidaMod.nombre,
            "grupo": str(request.user.groups.all().first())
        }
        return render(request, "comida/editarComida.html", context)

    def post(self, request, comida_id):
        comidaMod  =Comida.objects.get(id = comida_id)
        form = Nueva_Comida(request.POST, request.FILES , instance=comidaMod)
        context = {
            "form": form,
            "title": "Editar comida " + comidaMod.nombre,
            "grupo": str(request.user.groups.all().first())
        }
        if(form.is_valid()):
            comidaMod=form.save(commit=False)
            comidaMod.save()
            return redirect("/comida/categorias/" + slugify(comidaMod.categoria) + "/")
        return render(request,"comida/editarComida.html", context)

class EditarCategoria(LoginRequiredMixin,AdminMixin,View):
    login_url = '/login/'
    redirect_url = '/comida/categorias/'

    def get(self, request, categoria_id):
        categoriaMod = Categoria.objects.get(id=categoria_id)
        form = Nueva_Categoria(instance=categoriaMod)
        context = {
            "form": form,
            "title": "Editar categoría " + categoriaMod.nombre,
            "grupo": str(request.user.groups.all().first())
        }
        return render(request,"categoria/editarCategoria.html", context)

    def post(self, request, categoria_id):
        categoriaMod=Categoria.objects.get(id=categoria_id)
        form =Nueva_Categoria(request.POST, request.FILES, instance=categoriaMod)
        context = {
            "form": form,
            "title": "Editar categoría " + categoriaMod.nombre,
            "grupo": str(request.user.groups.all().first())
        }
        if(form.is_valid()):
            categoriaMod=form.save(commit=False)
            categoriaMod.save()
            return redirect("/comida/categorias/")
        return render(request,"categoria/editarCategoria.html", context)


# INICIA clases de la vista carrito

class CartView(LoginRequiredMixin,ClienteMixin,ListView):
    """
    Clase CartView, regresa la vista del carrito.
    """
    login_url = '/login/'
    redirect_url = '/'

    model = cantidadComidaOrden
    template= 'comida/carrito.html'

    def get(self, request):
        """GET method."""
        user = request.user.id
        objetos = []
        if Orden.objects.filter(usuario= user, estado = 'CT').exists():
            orden = Orden.objects.get(usuario= user, estado = 'CT')
            objetos = cantidadComidaOrden.objects.filter(idOrden = orden)

            context = {
                "objetos": objetos,
                "title":"carrito",
                "orden" : orden
                }
        else:
            context = {
                "objectos": objetos,
                "title":"carrito",
            }

        return render(request, self.template, context)

class AddToCart(LoginRequiredMixin, View):
    """
    Clase AddToCart, se encarga de la cantidad del alimento en la vista de las comidas
    """
    template_name = 'comida/vercomida.html'
    login_url = '/login/'

    def post(self, request, *args, **kwargs):
        """
        Validacion del form para añadir al carrito
        """
        form = CartAddProductForm(request.POST)
        cart, is_new_cart = Orden.objects.get_or_create(usuario = self.request.user, estado = 'CT')

        idComida = Comida.objects.get(id = self.kwargs.get('comida_id'))

        context = {}

        if form.is_valid():
            cantidadComida = form.cleaned_data.get("cantidadComida")
            cart.add_item(idComida,cantidadComida)

        context = {"form":form}
        comida_id = idComida.categoria.id
        return redirect( reverse_lazy('comida:categorias'))


class DeleteFromCart(LoginRequiredMixin, DeleteView):
    """
    Clase DeleteFromCart que elimina un solo elemento del carrito,
    implementado mediante un botón que borra todos los atributos de ese item
    por lo tanto lo elimina de la tabla del carrito
    """

    login_url = '/login/'
    model = cantidadComidaOrden
    success_url = reverse_lazy('comida:cart')
    slug_url_kwarg = 'comida_id'
    pk_url_kwarg = 'comida_id'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# FIN clases de la vista carrito

class Ordenar(View):
    def get(self,request,orden_id,dir_id):
        orden = Orden.objects.get(id = orden_id)
        orden.estado = 'PD'
        orden.fecha = datetime.datetime.now()
        orden.dirr = direccion.objects.get(id = dir_id)
        orden.save()
        return redirect( reverse_lazy('comida:categorias'))

class Direccion(LoginRequiredMixin,ClienteMixin,View):
    login_url = '/login/'
    redirect_url = '/'

    template = "comida/direccion.html"

    def get(self, request, orden_id):
        """GET method."""
        direcciones = direccion.objects.filter(email = request.user)
        orden = Orden.objects.get(id = orden_id)
        form = DireccionForm()
        context = {
            "direcciones": direcciones,
            "orden" : orden ,
            "title": "Elige tu direccion",
            "form": form,
        }
        return render(request, self.template, context)

    def post(self, request, orden_id):
        form = DireccionForm(request.POST)

        try:
            if form.is_valid():
                texto = form.cleaned_data['dir']
                direccion_nueva = direccion.objects.create(email = request.user , dirrec = texto)
                direccion_nueva.save()
                messages.success(request, 'Direccion Agregada !')
                direcciones = direccion.objects.filter(email = request.user)
                orden = Orden.objects.get(id = orden_id)
                form = DireccionForm()
                context = {
                    "direcciones": direcciones,
                    "orden" : orden ,
                    "title": "Elige tu direccion",
                    "form": form,
                }
                return render(request, self.template, context)

            direcciones = direccion.objects.filter(email = request.user)
            orden = Orden.objects.get(id = orden_id)
            form = DireccionForm()
            context = {
                "direcciones": direcciones,
                "orden" : orden ,
                "title": "Elige tu direccion",
                "form": form,
            }
            return render(request, self.template, context)

        except:
            messages.success(request, 'Hubo un error agregando la Categoria')
            direcciones = direccion.objects.filter(email = request.user)
            orden = Orden.objects.get(id = orden_id)
            form = DireccionForm()
            context = {
                "direcciones": direcciones,
                "orden" : orden ,
                "title": "Elige tu direccion",
                "form": form,
            }
            return render(request, self.template, context)

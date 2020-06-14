
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
            "form": form
        }
        return render(request, self.template, context)

class AgregarCategoria(View):

    template ="categoria/agregar_categoria.html"
    title = "Agregar categorías"

    def get(self,request):
        form = Nueva_Categoria()
        context = {
            "form": form,
            "title": self.title
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
                    "title": self.title
                }
                return render(request, self.template, context)

            context = {
                "form": form,
                "title": self.title
            }
            return render(request, self.template, context)
        except:
            messages.success(request, 'Hubo un error agregando la Categoria')
            context = {
                "form": form,
                "title": self.title
            }
            return render(request, self.template, context)

class AgregarComida(View):

    template ="comida/agregar_comida.html"
    title = "Agregar comida"

    def get(self,request):
        form = Nueva_Comida()
        context = {
            "form": form,
            "title": self.title
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
                    "title": self.title
                }
                return render(request, self.template, context)

            context = {
                "form": form,
                "title": self.title
            }
            return render(request, self.template, context)

        except:
            messages.success(request, 'Hubo un error agregando la Comida')
            context = {
                "form": form,
                "title": self.title
            }
            return render(request, self.template, context)


class CategoriaVista(View):

    template = "comida/vercategorias.html"

    def get(self, request):
        """GET method."""
        categorias = Categoria.objects.all()
        context = {
            "categorias": categorias,
            "title": "Explora nuestro menú"
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


class EditarComida(View):
    def get(self, request, comida_id):
        comidaMod = Comida.objects.get(id = comida_id)
        form = Nueva_Comida(instance = comidaMod)
        context = {
            "form": form,
            "title": "Editar comida " + comidaMod.nombre
        }
        return render(request, "comida/editarComida.html", context)

    def post(self, request, comida_id):
        comidaMod  =Comida.objects.get(id = comida_id)
        form = Nueva_Comida(request.POST, request.FILES,  instance=comidaMod) ,
        context = {
            "form": form,
            "title": "Editar comida " + comidaMod.nombre
        }
        if(form.is_valid()):
            comidaMod=form.save(commit=False)
            comidaMod.save()
            return redirect("/comida/categorias/" + slugify(comidaMod.categoria) + "/")

        return render(request,"comida/editarComida.html", context)

class EditarCategoria(View):
    def get(self, request, categoria_id):
        categoriaMod = Categoria.objects.get(id=categoria_id)
        form = Nueva_Categoria(instance=categoriaMod)
        context = {
            "form": form,
            "title": "Editar categoría " + categoriaMod.nombre
        }
        return render(request,"categoria/editarCategoria.html", context)

    def post(self, request, categoria_id):
        categoriaMod=Categoria.objects.get(id=categoria_id)
        form =Nueva_Categoria(request.POST, request.FILES, instance=categoriaMod)
        context = {
            "form": form,
            "title": "Editar categoría " + categoriaMod.nombre
        }
        if(form.is_valid()):
            categoriaMod=form.save(commit=False)
            categoriaMod.save()
            return redirect("/comida/categorias/")
        return render(request,"categoria/editarCategoria.html", context)

# class AddToCart(View):
#     def get(self,request,comida_id):
#         user = request.user
#         comida = Comida.objects.get(id= comida_id)
#         if Orden.objects.filter(usuario=user.id).exists():
#             orden = Orden.objects.get(usuario= user.id)
#             #EStoy pensando en hacer un if no se si aqui on en el template para que no cree otro si ya esta
#             comida_ord ,status = cantidadComidaOrden.objects.get_or_create(idComida = comida,cantidadComida = 1,idOrden= orden)
#         else:
#             orden = Orden.objects.create(usuario= user,fecha= datetime.datetime.now(),estado="carrito")
#             comida_ord ,status = cantidadComidaOrden.objects.get_or_create(idComida = comida,cantidadComida = 1,idOrden= orden)
#         #DUda sobre si lo que agregamos a orden es la comida o la cantidad comida orden @.@
#         #Por ahora hare la comida
#         orden.comida.add(comida)
#         if status:
#             orden.save()
#             comida_ord.save()

#         messages.success(request, 'Categoria Agregada !')
#         return redirect('comida:categorias')


class CartView(LoginRequiredMixin,ListView):

    model = cantidadComidaOrden
    template= 'comida/carrito.html'

    def get(self, request):
        """GET method."""
        user = request.user.id
        orden = Orden.objects.filter(usuario= user).first()
        objetos = cantidadComidaOrden.objects.filter(idOrden = orden)
        context = {
            "objetos": objetos,
            "orden" : orden
        }
        return render(request, self.template, context)

class AddToCart(LoginRequiredMixin, View):
    template_name = 'comida/vercomida.html'
    login_url = 'user:login'

    def post(self, request, *args, **kwargs):
        """
        Validacion del form para añadir al carrito
        """
        form = CartAddProductForm(request.POST)
        cart, is_new_cart = Orden.objects.get_or_create(usuario = self.request.user, estado = 'CT')

        idComida = Comida.objects.get(id = self.kwargs.get('comida_id'))
        # comida = Comida.objects.get(id= comida_id)

        context = {}

        if form.is_valid():
            cantidadComida = form.cleaned_data.get("cantidadComida")
            cart.add_element(idComida,cantidadComida)

        context = {"form":form}
        comida_id = idComida.categoria.id
        return redirect( reverse_lazy('comida:categorias'))


class DeleteFromCart(LoginRequiredMixin, DeleteView):

    login_url = 'users:login'
    model = cantidadComidaOrden
    success_url = reverse_lazy('comida:cart')
    slug_url_kwarg = 'comida_id'
    pk_url_kwarg = 'comida_id'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class Ordenar(View):
    def get(self,request,orden_id):
        orden = Orden.objects.get(id = orden_id)
        orden.estado = 'PD'
        orden.save()
        return redirect( reverse_lazy('comida:categorias'))


# @require_POST
# def cart_add(request, comida_id):
#     """
#     Funcion que agrega productos al carrito o actualiza cantidades de productos existentes en el carrito
#     require_POST: se usa este decorador para solo admitir POST request, ya que esta view cambiará datos
#     Se recibe el id de la comida como parametro, se obtiene y se valida con el form, si el form es válido
#     se agrega o se actualiza el producto en el carrito
#     Esta view redirecciona a cart_detail URL
#     """
#     cart = Cart(request)
#     product = get_object_or_404(Comida, id = comida_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product = product,
#                  quantity = cd['quantity'],
#                  update_quantity = cd['update'])
#     return redirect('cart: cart_detail')

# def cart_remove(request, comida_id):
#     """
#     Funcion que quita in producto del carrito
#     Recibe el id de la comida que serpa removida, se obtiene y se elimina del carrito.
#     Se redirecciona a la URL cart_detail
#     """
#     cart = Cart(request)
#     product = get_object_or_404(Comida, id = comida_id)
#     cart.remove(product)
#     return redirect('cart: cart_detail')

# def cart_detail(request):
#     """
#     View que despliega el carrito y sus elementos
#     """
#     cart = Cart(request)
#     return render(request, 'comida/carrito.html', {'cart':cart})


# def product_detail(request, id, slug):
#     product = get_object_or_404(Comida, id=id,
#                                         slug=slug,
#                                         available=True)
#     cart_product_form = CartAddProductForm()
#     context = {
#         'product': product,
#         'cart_product_form': cart_product_form
#     }
#     return render(request, 'comida/vercomida.html', context)

"""Comida URL configuration."""

# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Views
from . import views

app_name = "comida"
urlpatterns = [
    path('', views.ComidaVista.as_view(), name = 'comida'),
    path('agregar-categoria/', views.AgregarCategoria.as_view(), name='agregar-categoria'),
    path('agregar-comida/', views.AgregarComida.as_view(), name='agregar-comida'),
    path('categorias/', views.CategoriaVista.as_view(), name = 'categorias'),
    path('categorias/<str:categoryName>/', views.ComidaVista.as_view(), name = 'comida'),
    path('editarComida/<int:comida_id>',views.EditarComida.as_view()),
    path('eliminarComida/<int:comida_id>',views.EliminarComida.as_view()),
    path('editarCategoria/<int:categoria_id>',views.EditarCategoria.as_view()),
    path('eliminarCategoria/<int:categoria_id>',views.EliminarCategoria.as_view()),
    path('add_to_cart/<int:comida_id>', views.AddToCart.as_view()),
    path('carrito/', views.cart_detail, name='cart_detail'),
    path('add/<int:comida_id>/', views.cart_add, name = 'cart_add'),
    path('remove/<int:comida_id>/', views.cart_remove, name = 'cart_remove'),
]

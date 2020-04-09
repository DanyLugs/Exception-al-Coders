"""Comida URL configuration."""

# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


# Views
from comida import views

app_name = "comida"
urlpatterns = [
    path('categorias/comida/', views.Comida.as_view(), name = 'comida'),
    path('agregar-categoria/', AgregarCategoria.as_view(), name='agregar-categoria'),
     path('agregar-comida/', AgregarComida.as_view(), name='agregar-comida'),
]

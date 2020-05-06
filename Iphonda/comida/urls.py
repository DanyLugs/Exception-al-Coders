"""Comida URL configuration."""

# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Views
from comida import views

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
    path('eliminarCategoria/<int:categoria_id>',views.EliminarCategoria.as_view())
]

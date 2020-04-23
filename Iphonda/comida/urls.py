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
    path('', views.ComidaVista.as_view(), name = 'comida'),
    path('agregar-categoria/', views.AgregarCategoria.as_view(), name='agregar-categoria'),
    path('agregar-comida/', views.AgregarComida.as_view(), name='agregar-comida'),
    path('categorias/', views.CategoriaVista.as_view(), name = 'categorias'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

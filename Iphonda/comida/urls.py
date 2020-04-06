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
    path('categorias/comida/', views.Comida.as_view(), name = 'comida')
]
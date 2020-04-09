from django.contrib import admin
from django.urls import include, path

# Views
from comida.views import AgregarCategoria

app_name = "comida"
urlpatterns = [
    path('agregar-categoria/', AgregarCategoria.as_view(), name='agregar-categoria'),
]

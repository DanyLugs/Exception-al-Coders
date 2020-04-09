from django.contrib import admin
from django.urls import include, path

# Views
from comida.views import AgregarComida

app_name = "comida"
urlpatterns = [
    path('agregar-comida/', AgregarComida.as_view(), name='agregar-comida'),
]

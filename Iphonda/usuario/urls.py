from django.urls import include,path
from django.contrib import admin
from .models import *
from .views import *
from usuario import views
app_name="usuario"
urlpatterns=[
    path("pedidos",views.Pedidos.as_view(),name="pedidos")
]

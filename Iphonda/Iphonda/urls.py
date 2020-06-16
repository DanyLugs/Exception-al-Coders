"""Iphonda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from usuarios.views import *
from pages.views import HomePage

urlpatterns = [
    path('', HomePage.as_view()),
    path('django/', admin.site.urls),
    path('comida/', include('comida.urls')),
    path('admin/', include('usuarios.admin-urls')),
    path('repartidor/', Repartidor.as_view()),
    path('usuario/', Cliente.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', Signup.as_view()),
    path('pedidos-administrador/', Pedidos.as_view(),name='pedido_admin'),
    path('pedidos-usuarios/', Pedidos_usuarios.as_view()),
    path('pedidos-repartidor/', Pedidos_repartidor.as_view(),name="pedido_rep"),
    path('pedido_proceso/<int:ordenid>',Proceso.as_view(),name= 'proceso'),
    path('pedido_entrega/<int:ordenid>',Entrega.as_view(),name= 'entrega'),
    path('calificar-servicio/<int:idOrden>', CalificarServicio.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

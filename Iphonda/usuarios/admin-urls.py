from django.urls import include, path
from usuarios import views

app_name = "usuarios"

urlpatterns = [
    path('', views.Admin.as_view(), name='dashboard'),
    path('agregar-repartidor/', views.AgregarRepartidor.as_view(), name='addRepartidor'),
    path('agregar-repartidor/<int:idUser>', views.AgregarRepartidorConId.as_view(), name='addRepartidorConId'),
    path('revocar-repartidor/<int:idUser>', views.QuitarRepartidorConId.as_view(), name='remRepartidorConId'),
]

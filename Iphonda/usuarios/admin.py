from django.contrib import admin
from .models import Orden, cantidadComidaOrden

# Register your models here.
admin.site.register(Orden)
admin.site.register(cantidadComidaOrden)


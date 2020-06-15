from django.contrib import admin
from .models import Orden , direccion, cantidadComidaOrden

# Register your models here.
admin.site.register(Orden)
admin.site.register(direccion)
admin.site.register(cantidadComidaOrden)

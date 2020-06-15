from django.db import models
from django.conf import settings
from django.db.models import Field
from decimal import Decimal

# Create your models here.
class Orden(models.Model):
    """docstring forOrden."""

    ORDER_STATES = [
        ('CT','EN CARRITO'),
        ('PD','PENDIENTE'),
        ('LT','LISTA'),
        ('EC','EN CAMINO'),
        ('ET','ENTREGADO'),
        ('CF','CALIFICADO')
    ]

    id      = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    comida  = models.ManyToManyField('comida.Comida', through="cantidadComidaOrden" )
    fecha   = models.DateField(null=True)
    estado  = models.CharField(choices=ORDER_STATES, max_length=2)
    califi  = models.IntegerField(null=True)

    def add_item(self, new_item, cantidadComida):
        """
        Funcion que agrega la comida seleccionada de la visa de comida al carrito
        """
        idComida, is_new = self.order_id.get_or_create(idComida = new_item)
        if is_new:
            idComida.cantidadComida = cantidadComida
        else:
            idComida.cantidadComida += cantidadComida
        idComida.save()

    def get_total_price(self):
        """
        Funcion que calcula el total del carrito, toma en cuenta la funcion
        get_subtotal, realiza una suma de todos los subtotales en el carrito
        """
        total = 0
        for item in self.order_id.all():
            total += item.get_subtotal()
        return total      
    class Meta:
        verbose_name_plural = "Órdenes"

    def __str__(self):
        return str (self.id)

    def __repr__(self):
        return self.__str__()

class direccion(models.Model):
    id        = models.AutoField(primary_key=True)
    email     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    dirrec    = models.TextField()



class cantidadComidaOrden(models.Model):
    cantidadComida= models.IntegerField(default = 1)
    idComida = models.ForeignKey("comida.Comida",on_delete = models.CASCADE)
    idOrden = models.ForeignKey("Orden", on_delete = models.CASCADE, related_name = 'order_id')

    def get_subtotal(self):
        """
        Funcion que realiza el subtotal de un item agregado al carrito
        multiplica el precio del porducto por la cantidad del mismo
        """
        return self.cantidadComida * self.idComida.precio

    
from django.db import models
from django.conf import settings
from django.db.models import Field
# Create your models here.
class Orden(models.Model):
    """docstring forOrden."""

    ORDER_STATES = [
        ('CT','CARRITO'),
        ('PD','PENDIENTE'),
        ('LT','LISTA'),
        ('EC','EN CAMINO'),
        ('ET','ENTREGADO'),
    ]

    id      = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    comida  = models.ManyToManyField('comida.Comida', through="cantidadComidaOrden" )
    fecha   = models.DateField(null=True)
    estado  = models.CharField(choices=ORDER_STATES, max_length=2)
    califi  = models.IntegerField(null=True)

    def add_element(self, new_element, cantidadComida):
        idComida, is_new = self.order_elems.get_or_create(idComida = new_element)
        if is_new:
            idComida.cantidadComida = cantidadComida
        else:
            idComida.cantidadComida += cantidadComida
        idComida.save()        
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
    idOrden = models.ForeignKey("Orden", on_delete = models.CASCADE, related_name = 'order_elems')

    def get_subtotal(self):
        return self.cantidadComida * self.comida.precio

    def get_total_price(self):
        """
        Calcula el precio total de todos los elementos del carrito
        """
        return sum(Decimal(comida['precio']) * cantidadComidaOrden['cantidadComida'] for comida in self.cart.values())      

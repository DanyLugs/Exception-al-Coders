from django.db import models
from django.conf import settings

# Create your models here.
class Orden(models.Model):
    """docstring forOrden."""
    id      = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    comida  = models.ManyToManyField('comida.Comida')
    fecha   = models.DateField()
    total   = models.DecimalField(max_digits = 9, decimal_places = 2)

    class Meta:
        verbose_name_plural = "Órdenes"

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.__str__()

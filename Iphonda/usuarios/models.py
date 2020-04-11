from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Orden(models.Model):
    """docstring forOrden."""
    id     = models.AutoField(primary_key=True)
    # id_usuario  = models.ForeignKey('User.username', on_delete = models.PROTECT)
    comida = models.ForeignKey('comida.Comida', on_delete = models.PROTECT)
    fecha  = models.DateField()
    total  = models.DecimalField(max_digits = 9, decimal_places = 2)

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.__str__()

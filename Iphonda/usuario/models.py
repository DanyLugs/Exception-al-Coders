from django.db import models
#from Iphonda.comida.models import Comida
# Create your models here.
class Usuario(models.Model):
    """docstring forUsuario."""
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.email
    def __repr__(self):
        return self.__str__()

class Orden(models.Model):
    """docstring forOrden."""
    id=models.AutoField(primary_key=True)
    email= models.ForeignKey('Usuario',on_delete=models.PROTECT)
    comida=models.ForeignKey('comida.Comida',on_delete= models.PROTECT)
    fecha=models.DateField()
    total=models.DecimalField(max_digits=9,decimal_places=2)
    def __str__(self):
        return self.id
    def __repr__(self):
        return self.__str__()

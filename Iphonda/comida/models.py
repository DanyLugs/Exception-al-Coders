from django.db import models

# Create your models here.
class Comida(models.Model):
    """docstring for ."""
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=200)
    imagen=models.ImageField(blank=True,null=True)
    precio=models.DecimalField(max_digits=9,decimal_places=2)
        #Relacion :V
    categoria=models.ForeignKey('Categoria',on_delete= models.CASCADE)
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.__str__()

class Categoria(models.Model):
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.__str__()

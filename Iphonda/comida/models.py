from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Comida(models.Model):
    """docstring for ."""
    nombre      = models.CharField(max_length = 40, unique=True)
    descripcion = models.CharField(max_length = 200)
    imagen      = models.ImageField(upload_to = 'comida/static/images')
    precio      = models.DecimalField(max_digits=9,decimal_places=2)
        #Relacion
    categoria=models.ForeignKey('Categoria',on_delete= models.CASCADE)
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.__str__()

class Categoria(models.Model):
    nombre      = models.CharField(max_length=40, unique=True)
    slug        = models.SlugField(max_length=40, unique=True)
    descripcion = models.CharField(max_length=255)
    imagen      = models.ImageField(upload_to = 'categoria/static/images')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)

        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.__str__()

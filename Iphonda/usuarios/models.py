from django.db import models
from django.conf import settings
from django.db.models import Field
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()
# Create your models here.
class Orden(models.Model):
    """docstring forOrden."""
    id      = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    comida  = models.ManyToManyField('comida.Comida', through="cantidadComidaOrden" )
    fecha   = models.DateField()
    estado  = models.CharField(max_length=10)
    califi  = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Órdenes"

    def __str__(self):
        return str (self.id)

    def __repr__(self):
        return self.__str__()

# # Cada vez que un usuario se registre, se creará un perfil para ese usuario
# def post_save_profile_create(sender, instance, created, *args, **kwargs):
#     if created:
#         Orden.objects.get_or_create(usuario=instance)   

# post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)             

class direccion(models.Model):
    id        = models.AutoField(primary_key=True)
    email     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    dirrec    = models.TextField()



class cantidadComidaOrden(models.Model):
    cantidadComida= models.IntegerField()
    idComida = models.ForeignKey("comida.Comida",on_delete = models.CASCADE)
    idOrden = models.ForeignKey("Orden", on_delete = models.CASCADE)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    correo = models.OneToOneField(User, on_delete=models.CASCADE)
    habilitado = models.BooleanField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(correo=instance, habilitado=1)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #se elimina uno y se elimina el otro en forma de cascada
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

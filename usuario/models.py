from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=11, blank=True, null=True)
    foto = models.ImageField(upload_to='usuario/img', blank=True, null=True)


    def __str__(self):
        return self.first_name

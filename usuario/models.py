from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

def rename_user_image(instance, filename):
    ext = filename.split('.')[-1]
    nome_slug = slugify(instance.username or "usuario")
    filename = f"{nome_slug}_{uuid4().hex[:8]}.{ext}"
    return os.path.join("usuario/img", filename)

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=11, blank=True, null=True)
    foto = models.ImageField(upload_to=rename_user_image, blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name
    

    


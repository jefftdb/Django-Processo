from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def rename_user_image(instance, filename):
    ext = filename.split('.')[-1]
    nome_slug = slugify(instance.username or "usuario")
    filename = f"{nome_slug}_{uuid4().hex[:8]}.{ext}"
    return os.path.join("usuario/img", filename)

class processo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    


from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuario.models import Usuario

def rename_protoloco_image(instance, filename):
    ext = filename.split('.')[-1]
    nome_slug = slugify(instance.username or "usuario")
    filename = f"{nome_slug}_{uuid4().hex[:8]}.{ext}"
    return os.path.join("processo/img", filename)

class Processo(models.Model):
    id=models.AutoField(primary_key=True)    
    titulo = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    estado = models.CharField(max_length=11, blank=True, null=True, default='Analizando')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="relacionamento")
    
    

class ImagemProtocolo(models.Model):
    processo = models.ForeignKey("processo", on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to="processo/img/")
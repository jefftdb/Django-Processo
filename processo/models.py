from django.db import models
import os
from uuid import uuid4
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuario.models import Usuario
from abc import ABC, abstractmethod

def rename_protoloco_image(instance, filename):
    ext = filename.split('.')[-1]
    nome_slug = slugify(instance.processo or "nome")
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
    cor = models.CharField(blank=True, null= True,default='rgb(248, 51, 84)')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="relacionamento")
    
    
    def _obter_estado_do_modelo(self):
        estado_map = {
            "Analisando": Analisando(),
            "Aceito": Aceito(),
            "Pronto": Pronto(),
        }
        return estado_map.get(self.estado, Analisando())

    def avancar_estado(self):
        estado_atual = self._obter_estado_do_modelo()
        estado_atual.proximo_estado(self)

    def status_atual(self):
        return self.estado()

    def atualizar_estado_modelo(self):
        self.processo.estado = self.status_atual()
        self.processo.save()
    

class ImagemProtocolo(models.Model):
    processo = models.ForeignKey("processo", on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to=rename_protoloco_image)
    
    
 
class Estado(ABC):
    @abstractmethod
    def proximo_estado(self, contexto):
        pass

    @abstractmethod
    def status(self):
        pass


class Analisando(Estado):
    def proximo_estado(self, contexto):        
        contexto.estado = "Aceito"
        contexto.cor = "orange"

    def status(self):
        return "Analisando"

class Aceito(Estado):
    def proximo_estado(self, contexto):       
        contexto.estado = "Pronto"
        contexto.cor = "green"

    def status(self):
        return "Aceito"

class Pronto(Estado):
    def proximo_estado(self, contexto):
        print("Já está pronto. Não é possível avançar.")

    def status(self):
        return "Pronto"





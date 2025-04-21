from django.urls import path
from .views import  RegistrarProtocolo 

urlpatterns = [
    path("registrar_protocolo/",  RegistrarProtocolo.as_view(),name=" RegistrarProtocolo"),
]

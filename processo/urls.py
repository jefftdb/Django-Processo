from django.urls import path
from .views import  RegistrarProtocolo,Protocolos_por_usuario,AlteraEstado

urlpatterns = [
    path("registrar_protocolo/",  RegistrarProtocolo.as_view(),name=" RegistrarProtocolo"),
    path("protocolos_por_usuario/<int:id>/",  Protocolos_por_usuario.as_view(),name=" Protocolos_por_usuario"),
    path('altera_estado/<int:id>/', AlteraEstado.as_view(), name='altera_estado'),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProtocoloSerializer
from .models import Processo
from django.shortcuts import get_object_or_404
from django.http import FileResponse
import os
from django.conf import settings

class RegistrarProtocolo(APIView):
    def post(self, request):
        serializer = ProtocoloSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "Protocolo registrado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Protocolos_por_usuario(APIView):
     def get(self, request, id):
        protocolos = Processo.objects.filter(id_usuario=id).order_by('-id')
        serializer = ProtocoloSerializer(protocolos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class AlteraEstado(APIView):
    def post(self, request, id):
        processo = get_object_or_404(Processo, id=id)        
        processo.avancar_estado()        
        processo.save()
        
        return Response({
            "mensagem": "Estado alterado com sucesso",
            "estado_atual": processo.estado
        }, status=status.HTTP_200_OK)
    
class ExibeProtocolo(APIView):
    def post(self, request, id):
        protocolo = get_object_or_404(Processo, id=id)
        serializer = ProtocoloSerializer(protocolo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DownloadBD(APIView):
    def post(self, request):
        caminho_banco = os.path.join(settings.BASE_DIR, 'db.sqlite3')

        if os.path.exists(caminho_banco):
            response = FileResponse(open(caminho_banco, 'rb'), as_attachment=True, filename='db.sqlite3')
            return response
        else:
            return Response({'error': 'Arquivo não encontrado'}, status=404) 
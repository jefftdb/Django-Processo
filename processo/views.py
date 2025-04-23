from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProtocoloSerializer
from .models import Processo

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
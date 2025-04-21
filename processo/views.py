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

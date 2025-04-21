from django.shortcuts import render
from .models import Usuario
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class addUsuario(APIView):
    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUsuario(APIView):
    def post(self, request):
        email = request.data.get("email")
        senha = request.data.get("senha")
        
        usuario = Usuario.objects.get(email=email)
        print(usuario)
        
        try:
            usuario = Usuario.objects.get(email=email)
            
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(request, username=email, password=senha)
        

        if user is not None:
            return Response({"message": "Login bem-sucedido!", "usuario_id": user.id})
        else:
            return Response({"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

def perfil(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'usuario/perfil.html', {'usuario': usuario})
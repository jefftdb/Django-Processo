from django.shortcuts import render
from .models import Usuario


def perfil(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'usuario/perfil.html', {'usuario': usuario})

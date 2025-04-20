from django.shortcuts import render
from django.http import HttpResponse

def add_protocolo(request):
    return HttpResponse("Adicionou o protocolo!")

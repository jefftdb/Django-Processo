from django.urls import path
from . import views 

urlpatterns = [
    path("add_protocolo/", views.add_protocolo, name="add_protocolo"),
]

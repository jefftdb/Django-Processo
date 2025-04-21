from django.urls import path
from .views import LoginUsuario, addUsuario,perfil

urlpatterns = [
    path("<int:id>/", perfil, name="perfil"),
    path("add/", addUsuario.as_view(), name="addUsuario"),
    path("login/", LoginUsuario.as_view(), name="LoginUsuario"),
]

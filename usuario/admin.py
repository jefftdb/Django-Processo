from django.contrib import admin
from usuario.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "telefone", "email")

    search_fields = ("id", "username","email")



admin.site.register(Usuario, UsuarioAdmin)
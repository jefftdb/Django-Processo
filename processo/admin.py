from django.contrib import admin
from processo.models import Processo,ImagemProtocolo

class Processo_admin(admin.ModelAdmin):
    list_display=('id', 'titulo', 'nome', 'cpf', 'email', 'telefone', 'descricao',
            'latitude', 'longitude', 'id_usuario','estado')
    
    
class ImagemProtocolo_Admin(admin.ModelAdmin):
    list_display = ('processo','imagem')

admin.site.register(Processo, Processo_admin)
admin.site.register(ImagemProtocolo, ImagemProtocolo_Admin)


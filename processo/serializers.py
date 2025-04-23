from rest_framework import serializers
from .models import Processo, ImagemProtocolo

class ImagemProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemProtocolo
        fields = ['imagem']

class ProtocoloSerializer(serializers.ModelSerializer):
    imagens = serializers.ListField(  # para envio no POST
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    imagens_urls = ImagemProtocoloSerializer(source='imagens', many=True, read_only=True)  # para retorno no GET

    class Meta:
        model = Processo
        fields = [
            'id', 'titulo', 'nome', 'cpf', 'email', 'telefone', 'descricao',
            'latitude', 'longitude', 'id_usuario', 'imagens', 'imagens_urls'
        ]

    def create(self, validated_data):
        imagens = validated_data.pop('imagens', [])
        processo = Processo.objects.create(**validated_data)

        for imagem in imagens:
            ImagemProtocolo.objects.create(processo=processo, imagem=imagem)

        return processo

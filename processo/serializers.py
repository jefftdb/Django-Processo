from rest_framework import serializers
from .models import Processo, ImagemProtocolo

class ImagemProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemProtocolo
        fields = ['imagem']

class ProtocoloSerializer(serializers.ModelSerializer):
    imagens = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Processo
        fields = ['titulo', 'nome', 'cpf', 'email', 'telefone', 'descricao', 'latitude', 'longitude', 'id_usuario', 'imagens']

    def create(self, validated_data):
        imagens = validated_data.pop('imagens', [])
        processo = Processo.objects.create(**validated_data)

        for imagem in imagens:
            ImagemProtocolo.objects.create(processo=processo, imagem=imagem)

        return processo

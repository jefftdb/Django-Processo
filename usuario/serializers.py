from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'telefone', 'password', 'foto','CPF']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            CPF=validated_data.get('CPF',''),
            telefone=validated_data.get('telefone', ''),
            password=validated_data['password'],
            foto=validated_data.get('foto', None)            
           
        )
        print(user.CPF)
        return user

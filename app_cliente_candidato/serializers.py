from rest_framework import serializers
from app_usuarios.models import Usuario
from .models import ClienteCandidato

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'telefono', 'ubicacion', 'rol', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user

class ClienteCandidatoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()  # serializer anidado

    class Meta:
        model = ClienteCandidato
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = UsuarioSerializer.create(UsuarioSerializer(), validated_data=usuario_data)
        candidato = ClienteCandidato.objects.create(usuario=usuario, **validated_data)
        return candidato

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)

        if usuario_data:
            usuario_instance = instance.usuario
            for attr, value in usuario_data.items():
                setattr(usuario_instance, attr, value)
            usuario_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


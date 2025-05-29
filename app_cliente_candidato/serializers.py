from rest_framework import serializers
from .models import ClienteCandidato
from app_usuarios.models import Usuario  # Importa el modelo correcto
from app_usuarios.serializers import UsuarioSerializer

class ClienteCandidatoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = ClienteCandidato
        fields = ['id', 'usuario']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['rol'] = 'candidato'  # Asegura que el rol sea 'candidato'
        usuario = UsuarioSerializer().create(validated_data=usuario_data)
        candidato = ClienteCandidato.objects.create(usuario=usuario, **validated_data)
        return candidato

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)
        if usuario_data:
            usuario_serializer = UsuarioSerializer(instance.usuario, data=usuario_data, partial=True)
            if usuario_serializer.is_valid(raise_exception=True):
                usuario_serializer.save()
        return super().update(instance, validated_data)

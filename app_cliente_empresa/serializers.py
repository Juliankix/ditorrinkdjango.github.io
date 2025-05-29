from rest_framework import serializers
from .models import ClienteEmpresa
from app_usuarios.serializers import UsuarioSerializer

class ClienteEmpresaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()  # Mostrar datos del usuario anidados

    class Meta:
        model = ClienteEmpresa
        fields = ['id', 'usuario', 'datos_extra']

class ClienteEmpresaRegistroSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()  # Para crear usuario anidado

    class Meta:
        model = ClienteEmpresa
        fields = ['usuario', 'datos_extra']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['rol'] = 'empresa'  # Forzar rol empresa
        usuario = UsuarioSerializer().create(validated_data=usuario_data)
        cliente_empresa = ClienteEmpresa.objects.create(usuario=usuario, **validated_data)
        return cliente_empresa

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)
        if usuario_data:
            usuario_serializer = UsuarioSerializer(instance.usuario, data=usuario_data, partial=True)
            usuario_serializer.is_valid(raise_exception=True)
            usuario_serializer.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


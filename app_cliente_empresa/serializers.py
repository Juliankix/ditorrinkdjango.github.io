from rest_framework import serializers
from app_cliente_empresa.models import ClienteEmpresa
from app_usuarios.serializers import UsuarioSerializer

class ClienteEmpresaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = ClienteEmpresa
        fields = ['id', 'usuario', 'certificado_existencia', 'rut', 'nit', 'acta_constitucion', 'ubicaciones']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        usuario_serializer.is_valid(raise_exception=True)
        usuario = usuario_serializer.save()
        cliente_empresa = ClienteEmpresa.objects.create(usuario=usuario, **validated_data)
        return cliente_empresa

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)
        if usuario_data:
            usuario_serializer = UsuarioSerializer(instance.usuario, data=usuario_data, partial=True)
            usuario_serializer.is_valid(raise_exception=True)
            usuario_serializer.save()
        return super().update(instance, validated_data)


from rest_framework import serializers
from app_usuarios.models import Usuario
from .models import Administrador

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'telefono', 'ubicacion', 'rol', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class AdministradorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Administrador
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = UsuarioSerializer().create(usuario_data)
        return Administrador.objects.create(usuario=usuario, **validated_data)

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)
        if usuario_data:
            UsuarioSerializer().update(instance.usuario, usuario_data)

        return super().update(instance, validated_data)

from rest_framework import serializers
from .models import Administrador  # o el modelo correspondiente

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

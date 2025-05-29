from django.db import models
from app_usuarios.models import Usuario

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_administrador')

    def __str__(self):
        return f"Administrador: {self.usuario.email}"

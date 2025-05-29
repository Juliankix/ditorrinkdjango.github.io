from django.db import models
from app_usuarios.models import Usuario  # asegúrate de que el nombre del modelo es 'Usuario'

class ClienteCandidato(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_candidato')

    def __str__(self):
        return f"Candidato: {self.usuario.email}"

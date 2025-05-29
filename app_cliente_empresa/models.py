from django.db import models
from app_usuarios.models import Usuario

class ClienteEmpresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    # Campos específicos de la empresa (si alguno no está ya en Usuario)
    datos_extra = models.JSONField(blank=True, null=True)  # si aplica
    # Puedes agregar más campos propios de la empresa aquí si los necesitas

    def __str__(self):
        return self.usuario.email

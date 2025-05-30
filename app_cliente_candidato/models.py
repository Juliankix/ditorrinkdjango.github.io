from django.db import models
from app_usuarios.models import Usuario

class ClienteCandidato(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    hoja_vida = models.FileField(upload_to='hojas_vida/', null=True, blank=True)
    certificados_discapacidad = models.FileField(upload_to='certificados_discapacidad/', null=True, blank=True)
    certificados_estudio = models.FileField(upload_to='certificados_estudio/', null=True, blank=True)
    datos_extra = models.CharField(max_length=255, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=100)
    experiencia = models.TextField(blank=True)

    def __str__(self):
        return self.usuario.email

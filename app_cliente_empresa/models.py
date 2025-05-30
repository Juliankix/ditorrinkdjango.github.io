from django.db import models
from app_usuarios.models import Usuario

class ClienteEmpresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    certificado_existencia = models.FileField(upload_to='certificados_empresa/', null=True, blank=True)
    rut = models.FileField(upload_to='certificados_empresa/', null=True, blank=True)
    nit = models.CharField(max_length=30)
    acta_constitucion = models.FileField(upload_to='certificados_empresa/', null=True, blank=True)
    ubicaciones = models.TextField(blank=True, help_text="Direcciones de los locales, separadas por comas o en lista.")

    def __str__(self):
        return self.usuario.email

from django.contrib.auth.models import AbstractUser  # Importa la clase base para usuarios personalizables
from django.db import models  # Importa el módulo de modelos de Django

# Define un modelo personalizado de usuario que hereda de AbstractUser
class Usuario(AbstractUser):
    # Opciones de roles disponibles para el usuario
    ROLES = (
        ('admin', 'Administrador'),
        ('empresa', 'Empresa'),
        ('candidato', 'Candidato'),
    )

    # Campos adicionales personalizados para el modelo de usuario
    email = models.EmailField(unique=True)  # Campo de email único, será el identificador principal
    telefono = models.CharField(max_length=20, blank=True)  # Teléfono, opcional
    imagen = models.FileField(upload_to='imagen/', null=True, blank=True)  # Ruta o URL de imagen, opcional
    ubicacion = models.CharField(max_length=255, blank=True)  # Dirección o ubicación del usuario
    certificados_legales = models.FileField(upload_to='certificados_legales/', null=True, blank=True)  # Archivos legales del usuario
    certificados_discapacidad = models.FileField(upload_to='certificados_discapacidad/', null=True, blank=True)  # Certificados de discapacidad
    hoja_vida = models.FileField(upload_to='hojas_vida/', null=True, blank=True)
    certificados_estudio = models.FileField(upload_to='certificados_estudio/', null=True, blank=True)  # Certificados académicos
    identificacion = models.CharField(max_length=50, blank=True)  # Número o documento de identidad
    datos_extra = models.CharField(max_length=255, blank=True)  # Información adicional
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Fecha de nacimiento del usuario

    # Campo de rol con opciones limitadas definidas en ROLES
    rol = models.CharField(max_length=20, choices=ROLES)

    # Especifica que el campo 'email' será usado para iniciar sesión en lugar de 'username'
    USERNAME_FIELD = 'email'

    # Campos requeridos al crear un usuario (además del USERNAME_FIELD)
    REQUIRED_FIELDS = ['username']

    # Representación en texto del objeto (por ejemplo en el admin o shell)
    def __str__(self):  
        return f"{self.email} ({self.get_rol_display()})"  # Muestra el email y el nombre legible del rol
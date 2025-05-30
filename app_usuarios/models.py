from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('empresa', 'Empresa'),
        ('candidato', 'Candidato'),
    )

    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.get_rol_display()})"

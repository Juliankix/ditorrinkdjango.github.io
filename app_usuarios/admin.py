from django.contrib import admin
from .models import Usuario
from app_cliente_candidato.models import ClienteCandidato
from app_cliente_empresa.models import ClienteEmpresa
from app_administrador.models import Administrador  # Asegúrate de importar bien

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telefono', 'rol')
    search_fields = ('username', 'email')

@admin.register(ClienteCandidato)
class ClienteCandidatoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'profesion', 'fecha_nacimiento')
    search_fields = ('usuario__email', 'profesion')

@admin.register(ClienteEmpresa)
class ClienteEmpresaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nit', 'ubicaciones')
    search_fields = ('usuario__email', 'nit')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    search_fields = ('usuario__email',)
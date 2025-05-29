from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'telefono', 'imagen', 'ubicacion')  # Opcional, puedes ajustar la lista que ves en la tabla
    list_filter = ()  # Si no quieres filtros, déjalo vacío o ajusta según convenga
    
    fieldsets = (
        (None, {'fields': (
            'email',
            'telefono',
            'imagen',
            'ubicacion',
            'certificados_legales',
            'certificados_discapacidad',
            'hoja_vida',
            'certificados_estudio',
            'identificacion',
            'datos_extra',
            'fecha_nacimiento',
        )}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'telefono',
                'imagen',
                'ubicacion',
                'certificados_legales',
                'certificados_discapacidad',
                'hoja_vida',
                'certificados_estudio',
                'identificacion',
                'datos_extra',
                'fecha_nacimiento',
                'password1',
                'password2',
            )
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)


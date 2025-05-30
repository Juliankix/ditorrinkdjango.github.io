from rest_framework import generics
from .models import Administrador
from .serializers import AdministradorSerializer

# Crear administrador (POST)
class AdministradorCreateView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Listar administradores (GET)
class AdministradorListView(generics.ListAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Ver detalle de un administrador específico (GET)
class AdministradorDetailView(generics.RetrieveAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Actualizar administrador (PUT/PATCH)
class AdministradorUpdateView(generics.UpdateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Eliminar administrador (DELETE)
class AdministradorDeleteView(generics.DestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
